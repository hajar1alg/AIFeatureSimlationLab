import streamlit as st
import pandas as pd
import joblib

# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="AI Feature Simulation Lab",
    page_icon="🤖",
    layout="wide"
)

# =========================================================
# DESIGN
# =========================================================

st.markdown("""
<style>

.block-container {
    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}

.hero {
    padding: 32px;
    border-radius: 20px;
    background: linear-gradient(135deg, #111827, #374151);
    color: white;
    margin-bottom: 28px;
}

.hero h1 {
    font-size: 38px;
    margin-bottom: 8px;
}

.hero p {
    font-size: 17px;
    color: #d1d5db;
}

.card {
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #e5e7eb;
    background: white;
    min-height: 120px;
}

.card-title {
    font-size: 14px;
    color: #6b7280;
}

.card-value {
    font-size: 30px;
    font-weight: 700;
    margin-top: 8px;
}

.section-title {
    font-size: 25px;
    font-weight: 700;
    margin-top: 30px;
    margin-bottom: 18px;
}

.issue-box {
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #e5e7eb;
    background: #f9fafb;
    margin-bottom: 12px;
}

.insight-box {
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #e5e7eb;
    background: #f8fafc;
    margin-bottom: 18px;
    line-height: 1.7;
}

.scenario-card {
    padding: 24px;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
    background: white;
    margin-top: 15px;
    margin-bottom: 15px;
}

.scenario-title {
    font-size: 23px;
    font-weight: 700;
}

.segment-box {
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #e5e7eb;
    background: white;
    margin-bottom: 15px;
}

.small-text {
    color: #6b7280;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD DATA + MODELS
# =========================================================

df = pd.read_csv("users_segmented.csv")

adoption_model = joblib.load("adoption_model.pkl")
purchase_model = joblib.load("purchase_model.pkl")
late_payment_model = joblib.load("late_payment_model.pkl")
retention_model = joblib.load("retention_model.pkl")


# =========================================================
# FEATURES
# =========================================================

prediction_features = [
    "monthly_purchases",
    "avg_purchase_amount",
    "late_payment_count",
    "on_time_payment_rate",
    "cancellation_rate",
    "offer_click_rate",
    "avg_installments",
    "monthly_spending",
    "user_segment"
]


# =========================================================
# SEGMENTS
# =========================================================

segment_info = {
    0: {
        "name": "High Engagement Users",
        "icon": "🟢",
        "description": "Frequent users with strong interaction and purchasing activity."
    },
    1: {
        "name": "Regular Users",
        "icon": "🔵",
        "description": "Users with moderate purchasing and engagement behavior."
    },
    2: {
        "name": "Price-Sensitive Users",
        "icon": "🟠",
        "description": "Users who may respond strongly to payment flexibility and offers."
    },
    3: {
        "name": "Higher Payment-Risk Users",
        "icon": "🔴",
        "description": "Users showing patterns associated with higher payment risk."
    }
}


# =========================================================
# AI INSIGHT GENERATOR
# =========================================================

def generate_insights(
    adoption_change,
    purchase_change,
    payment_change,
    retention_change,
    installments
):

    insights = []

    # Adoption
    if adoption_change > 2:

        insights.append(
            f"Feature adoption is projected to increase by "
            f"{adoption_change:.1f}% under the {installments}-installment scenario."
        )

    elif adoption_change < -2:

        insights.append(
            f"Feature adoption is projected to decrease by "
            f"{abs(adoption_change):.1f}% compared with the current baseline."
        )

    else:

        insights.append(
            "Feature adoption shows no significant simulated change."
        )

    # Purchase
    if purchase_change > 2:

        insights.append(
            f"Purchase completion shows a projected increase of "
            f"{purchase_change:.1f}%."
        )

    elif purchase_change < -2:

        insights.append(
            f"Purchase completion shows a projected decrease of "
            f"{abs(purchase_change):.1f}%."
        )

    else:

        insights.append(
            "Purchase completion remains relatively stable."
        )

    # Payment risk
    if payment_change > 2:

        insights.append(
            f"Late-payment risk increases by approximately "
            f"{payment_change:.1f}%, creating a potential risk area."
        )

    elif payment_change < -2:

        insights.append(
            f"Late-payment risk decreases by approximately "
            f"{abs(payment_change):.1f}% in the simulation."
        )

    else:

        insights.append(
            "The simulation shows limited change in payment risk."
        )

    # Retention
    if retention_change > 2:

        insights.append(
            f"30-day retention is projected to increase by "
            f"{retention_change:.1f}%."
        )

    elif retention_change < -2:

        insights.append(
            f"30-day retention is projected to decrease by "
            f"{abs(retention_change):.1f}%."
        )

    else:

        insights.append(
            "30-day retention remains relatively stable."
        )

    return insights


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 🤖 Simulation Lab")

    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Create Experiment",
            "Scenario Comparison",
            "User Segments",
            "Experiment History"
        ]
    )

    st.markdown("---")

    st.caption("AI Feature Simulation Lab")
    st.caption("Prototype v7.0")


# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">

<h1>AI Feature Simulation Lab</h1>

<p>
Simulate how different user behaviors may respond
to a new product feature before real-world deployment.
</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# DASHBOARD
# =========================================================

if page == "Dashboard":

    st.markdown(
        '<div class="section-title">Simulation Overview</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="card">
        <div class="card-title">Simulated Users</div>
        <div class="card-value">20,000</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <div class="card-title">Behavioral Segments</div>
        <div class="card-value">4</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <div class="card-title">AI Models</div>
        <div class="card-value">4</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="card">
        <div class="card-title">Simulation Engine</div>
        <div class="card-value">Active</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">What can the lab analyze?</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.info(
            "💳 **Feature Adoption**\n\n"
            "Estimate feature adoption."
        )

    with col2:
        st.info(
            "🛒 **Purchase Completion**\n\n"
            "Estimate purchase behavior."
        )

    with col3:
        st.info(
            "⚠️ **Payment Risk**\n\n"
            "Detect potential payment-risk changes."
        )

    with col4:
        st.info(
            "🔄 **Retention**\n\n"
            "Estimate potential retention impact."
        )


# =========================================================
# CREATE EXPERIMENT
# =========================================================

elif page == "Create Experiment":

    st.markdown(
        '<div class="section-title">Create New Experiment</div>',
        unsafe_allow_html=True
    )

    feature_name = st.text_input(
        "Feature name",
        placeholder="Example: Flexible 8-installment option"
    )

    feature_type = st.selectbox(
        "Feature type",
        [
            "Installments",
            "Offers & Promotions",
            "Checkout",
            "Payments",
            "Notifications"
        ]
    )

    st.markdown("### Feature Configuration")

    if feature_type == "Installments":

        installments = st.select_slider(
            "Number of installments",
            options=[4, 6, 8, 10, 12],
            value=6
        )

        st.info(
            f"Testing a **{installments}-installment** option."
        )

    else:

        feature_description = st.text_area(
            "Describe the feature",
            placeholder="Describe how the new feature works..."
        )

    st.markdown("---")

    if st.button(
        "🚀 Run AI Simulation",
        use_container_width=True
    ):

        if not feature_name:

            st.warning(
                "Please enter a feature name first."
            )

        else:

            # BASELINE

            baseline = df.copy()

            X_baseline = baseline[
                prediction_features
            ]

            baseline_adoption = (
                adoption_model
                .predict_proba(X_baseline)[:, 1]
                .mean() * 100
            )

            baseline_purchase = (
                purchase_model
                .predict_proba(X_baseline)[:, 1]
                .mean() * 100
            )

            baseline_payment = (
                late_payment_model
                .predict_proba(X_baseline)[:, 1]
                .mean() * 100
            )

            baseline_retention = (
                retention_model
                .predict_proba(X_baseline)[:, 1]
                .mean() * 100
            )

            # SCENARIO

            scenario = df.copy()

            if feature_type == "Installments":

                scenario["avg_installments"] = installments

            X_scenario = scenario[
                prediction_features
            ]

            scenario_adoption = (
                adoption_model
                .predict_proba(X_scenario)[:, 1]
                .mean() * 100
            )

            scenario_purchase = (
                purchase_model
                .predict_proba(X_scenario)[:, 1]
                .mean() * 100
            )

            scenario_payment = (
                late_payment_model
                .predict_proba(X_scenario)[:, 1]
                .mean() * 100
            )

            scenario_retention = (
                retention_model
                .predict_proba(X_scenario)[:, 1]
                .mean() * 100
            )

            # DELTAS

            adoption_delta = (
                scenario_adoption - baseline_adoption
            )

            purchase_delta = (
                scenario_purchase - baseline_purchase
            )

            payment_delta = (
                scenario_payment - baseline_payment
            )

            retention_delta = (
                scenario_retention - baseline_retention
            )

            # RESULTS

            st.markdown(
                '<div class="section-title">'
                '🧠 AI Simulation Results'
                '</div>',
                unsafe_allow_html=True
            )

            st.success(
                f"Simulation completed for: {feature_name}"
            )

            # =================================================
            # AI INSIGHTS
            # =================================================

            st.markdown(
                '<div class="section-title">'
                '🧠 AI Insights'
                '</div>',
                unsafe_allow_html=True
            )

            insights = generate_insights(
                adoption_delta,
                purchase_delta,
                payment_delta,
                retention_delta,
                installments
                if feature_type == "Installments"
                else "selected"
            )

            st.markdown(
                '<div class="insight-box">',
                unsafe_allow_html=True
            )

            for insight in insights:

                st.write(
                    "• " + insight
                )

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )

            # =================================================
            # METRICS
            # =================================================

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "Feature Adoption",
                    f"{scenario_adoption:.1f}%",
                    f"{adoption_delta:+.1f}%"
                )

            with col2:
                st.metric(
                    "Purchase Completion",
                    f"{scenario_purchase:.1f}%",
                    f"{purchase_delta:+.1f}%"
                )

            with col3:
                st.metric(
                    "Payment Risk",
                    f"{scenario_payment:.1f}%",
                    f"{payment_delta:+.1f}%"
                )

            with col4:
                st.metric(
                    "30-Day Retention",
                    f"{scenario_retention:.1f}%",
                    f"{retention_delta:+.1f}%"
                )

            # =================================================
            # POTENTIAL ISSUES
            # =================================================

            st.markdown(
                '<div class="section-title">'
                '🔎 Potential Issues Detected'
                '</div>',
                unsafe_allow_html=True
            )

            issues = []

            if adoption_delta < -2:
                issues.append(
                    "⚠️ Adoption may decrease."
                )

            if purchase_delta < -2:
                issues.append(
                    "🛒 Purchase completion may decrease."
                )

            if payment_delta > 2:
                issues.append(
                    "🔴 Payment risk may increase."
                )

            if retention_delta < -2:
                issues.append(
                    "🔄 Retention may decrease."
                )

            if not issues:

                issues.append(
                    "🟢 No significant negative change detected."
                )

            for issue in issues:

                st.markdown(
                    f"""
                    <div class="issue-box">
                    {issue}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            # =================================================
            # BASELINE TABLE
            # =================================================

            st.markdown("### 📊 Baseline vs Scenario")

            comparison = pd.DataFrame({

                "Metric": [
                    "Feature Adoption",
                    "Purchase Completion",
                    "Payment Risk",
                    "30-Day Retention"
                ],

                "Current": [
                    round(baseline_adoption, 1),
                    round(baseline_purchase, 1),
                    round(baseline_payment, 1),
                    round(baseline_retention, 1)
                ],

                "Scenario": [
                    round(scenario_adoption, 1),
                    round(scenario_purchase, 1),
                    round(scenario_payment, 1),
                    round(scenario_retention, 1)
                ],

                "Change": [
                    round(adoption_delta, 1),
                    round(purchase_delta, 1),
                    round(payment_delta, 1),
                    round(retention_delta, 1)
                ]
            })

            st.dataframe(
                comparison,
                use_container_width=True,
                hide_index=True
            )


# =========================================================
# SCENARIO COMPARISON
# =========================================================

elif page == "Scenario Comparison":

    st.markdown(
        '<div class="section-title">'
        '🔬 Scenario Comparison'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Explore how different installment configurations "
        "may affect simulated user behavior."
    )

    # BASELINE

    X_baseline = df[
        prediction_features
    ]

    baseline_adoption = (
        adoption_model
        .predict_proba(X_baseline)[:, 1]
        .mean() * 100
    )

    baseline_purchase = (
        purchase_model
        .predict_proba(X_baseline)[:, 1]
        .mean() * 100
    )

    baseline_payment = (
        late_payment_model
        .predict_proba(X_baseline)[:, 1]
        .mean() * 100
    )

    baseline_retention = (
        retention_model
        .predict_proba(X_baseline)[:, 1]
        .mean() * 100
    )

    scenarios = [4, 6, 8, 10, 12]

    results = []

    for option in scenarios:

        scenario = df.copy()

        scenario["avg_installments"] = option

        X_scenario = scenario[
            prediction_features
        ]

        adoption = (
            adoption_model
            .predict_proba(X_scenario)[:, 1]
            .mean() * 100
        )

        purchase = (
            purchase_model
            .predict_proba(X_scenario)[:, 1]
            .mean() * 100
        )

        payment = (
            late_payment_model
            .predict_proba(X_scenario)[:, 1]
            .mean() * 100
        )

        retention = (
            retention_model
            .predict_proba(X_scenario)[:, 1]
            .mean() * 100
        )

        adoption_change = (
            adoption - baseline_adoption
        )

        purchase_change = (
            purchase - baseline_purchase
        )

        payment_change = (
            payment - baseline_payment
        )

        retention_change = (
            retention - baseline_retention
        )

        issues = []

        if adoption_change < -2:
            issues.append(
                "Adoption decrease"
            )

        if purchase_change < -2:
            issues.append(
                "Purchase decrease"
            )

        if payment_change > 2:
            issues.append(
                "Payment risk increase"
            )

        if retention_change < -2:
            issues.append(
                "Retention decrease"
            )

        if not issues:
            issues.append(
                "No significant negative change"
            )

        results.append({

            "Installments": option,

            "Adoption": round(
                adoption,
                1
            ),

            "Purchase Completion": round(
                purchase,
                1
            ),

            "Payment Risk": round(
                payment,
                1
            ),

            "Retention": round(
                retention,
                1
            ),

            "Adoption Change": round(
                adoption_change,
                1
            ),

            "Purchase Change": round(
                purchase_change,
                1
            ),

            "Payment Change": round(
                payment_change,
                1
            ),

            "Retention Change": round(
                retention_change,
                1
            ),

            "Issues": " • ".join(
                issues
            )
        })

    comparison = pd.DataFrame(
        results
    )

    # =====================================================
    # TABLE
    # =====================================================

    st.markdown("### 📊 Scenario Overview")

    st.dataframe(
        comparison,
        use_container_width=True,
        hide_index=True
    )

    # =====================================================
    # AI INSIGHTS
    # =====================================================

    st.markdown(
        '<div class="section-title">'
        '🧠 AI Scenario Insights'
        '</div>',
        unsafe_allow_html=True
    )

    for _, row in comparison.iterrows():

        option = int(
            row["Installments"]
        )

        insights = generate_insights(
            row["Adoption Change"],
            row["Purchase Change"],
            row["Payment Change"],
            row["Retention Change"],
            option
        )

        st.markdown(
            f"""
            <div class="scenario-card">

            <div class="scenario-title">
            💳 {option} Installments
            </div>

            <br>

            <b>Adoption:</b>
            {row["Adoption"]:.1f}%
            ({row["Adoption Change"]:+.1f}%)

            &nbsp;&nbsp;&nbsp;

            <b>Purchase:</b>
            {row["Purchase Completion"]:.1f}%
            ({row["Purchase Change"]:+.1f}%)

            <br><br>

            <b>Payment Risk:</b>
            {row["Payment Risk"]:.1f}%
            ({row["Payment Change"]:+.1f}%)

            &nbsp;&nbsp;&nbsp;

            <b>Retention:</b>
            {row["Retention"]:.1f}%
            ({row["Retention Change"]:+.1f}%)

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="insight-box">',
            unsafe_allow_html=True
        )

        for insight in insights:

            st.write(
                "• " + insight
            )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

    # =====================================================
    # CHARTS
    # =====================================================

    st.markdown("### 📈 Adoption")

    st.line_chart(
        comparison.set_index(
            "Installments"
        )["Adoption"]
    )

    st.markdown("### 🛒 Purchase Completion")

    st.line_chart(
        comparison.set_index(
            "Installments"
        )["Purchase Completion"]
    )

    st.markdown("### ⚠️ Payment Risk")

    st.line_chart(
        comparison.set_index(
            "Installments"
        )["Payment Risk"]
    )

    st.markdown("### 🔄 Retention")

    st.line_chart(
        comparison.set_index(
            "Installments"
        )["Retention"]
    )


# =========================================================
# USER SEGMENTS
# =========================================================

elif page == "User Segments":

    st.markdown(
        '<div class="section-title">'
        '👥 Simulated User Segments'
        '</div>',
        unsafe_allow_html=True
    )

    for segment_id, info in segment_info.items():

        segment = df[
            df["user_segment"] == segment_id
        ]

        if len(segment) == 0:
            continue

        st.markdown(
            f"""
            <div class="segment-box">

            <h3>
            {info["icon"]} {info["name"]}
            </h3>

            <p class="small-text">
            {info["description"]}
            </p>

            <b>Users:</b>
            {len(segment):,}

            &nbsp;&nbsp;&nbsp;

            <b>Avg. Monthly Spending:</b>
            {segment["monthly_spending"].mean():.0f}

            &nbsp;&nbsp;&nbsp;

            <b>On-Time Payment:</b>
            {segment["on_time_payment_rate"].mean() * 100:.1f}%

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# EXPERIMENT HISTORY
# =========================================================

elif page == "Experiment History":

    st.markdown(
        '<div class="section-title">'
        '🧪 Experiment History'
        '</div>',
        unsafe_allow_html=True
    )

    st.info(
        "Experiment history will be connected "
        "to the simulation engine next."
    )

    st.write(
        "Previous simulations will appear here "
        "once experiment history is connected."
    )