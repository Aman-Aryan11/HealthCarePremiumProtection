import streamlit as st

from prediction_helper import predict


st.set_page_config(
    page_title="Health Insurance Cost Predictor",
    page_icon=None,
    layout="wide",
)


CATEGORICAL_OPTIONS = {
    "Gender": ["Male", "Female"],
    "Marital Status": ["Unmarried", "Married"],
    "BMI Category": ["Normal", "Obesity", "Overweight", "Underweight"],
    "Smoking Status": ["No Smoking", "Regular", "Occasional"],
    "Employment Status": ["Salaried", "Self-Employed", "Freelancer", ""],
    "Region": ["Northwest", "Southeast", "Northeast", "Southwest"],
    "Medical History": [
        "No Disease",
        "Diabetes",
        "High blood pressure",
        "Diabetes & High blood pressure",
        "Thyroid",
        "Heart disease",
        "High blood pressure & Heart disease",
        "Diabetes & Thyroid",
        "Diabetes & Heart disease",
    ],
    "Insurance Plan": ["Bronze", "Silver", "Gold"],
}


st.markdown(
    """
    <style>
        :root {
            --app-bg:
                radial-gradient(circle at top left, rgba(34, 211, 238, 0.12), transparent 30%),
                radial-gradient(circle at top right, rgba(45, 212, 191, 0.11), transparent 26%),
                linear-gradient(180deg, #071118 0%, #0b1721 48%, #0e1d27 100%);
            --surface-bg: rgba(14, 24, 38, 0.82);
            --surface-bg-strong: rgba(18, 30, 46, 0.94);
            --surface-border: rgba(125, 211, 252, 0.14);
            --surface-shadow: rgba(2, 8, 23, 0.34);
            --title-color: #e6f1ff;
            --body-color: #c6d5e3;
            --muted-color: #93a9bd;
            --accent-color: #5eead4;
            --label-color: #7dd3fc;
            --input-bg: rgba(9, 18, 29, 0.96);
            --input-border: rgba(100, 116, 139, 0.58);
            --input-text: #ecf6ff;
            --metric-bg: rgba(9, 18, 29, 0.72);
            --metric-border: rgba(125, 211, 252, 0.12);
            --button-bg: linear-gradient(135deg, #0ea5e9 0%, #14b8a6 100%);
            --button-bg-hover: linear-gradient(135deg, #38bdf8 0%, #2dd4bf 100%);
            --button-shadow: rgba(20, 184, 166, 0.26);
            --focus-ring: rgba(56, 189, 248, 0.22);
        }

        .stApp {
            background: var(--app-bg);
        }

        [data-testid="stAppViewContainer"] {
            color: var(--body-color);
        }

        [data-testid="stHeader"] {
            background: rgba(7, 17, 24, 0.88) !important;
            border-bottom: 1px solid var(--surface-border);
        }

        [data-testid="stToolbar"] button,
        [data-testid="stDecoration"] {
            color: var(--input-text) !important;
        }

        .hero-card,
        .info-card,
        .result-card {
            background: var(--surface-bg);
            border: 1px solid var(--surface-border);
            border-radius: 24px;
            box-shadow: 0 20px 50px var(--surface-shadow);
            backdrop-filter: blur(10px);
        }

        .hero-card {
            padding: 2rem 2.2rem;
            margin-bottom: 1.25rem;
        }

        .hero-eyebrow {
            display: inline-block;
            font-size: 0.8rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: var(--accent-color);
            margin-bottom: 0.75rem;
        }

        .hero-title {
            font-size: 2.4rem;
            line-height: 1.1;
            font-weight: 800;
            color: var(--title-color);
            margin-bottom: 0.65rem;
        }

        .hero-copy {
            font-size: 1rem;
            color: var(--body-color);
            max-width: 680px;
            margin-bottom: 0;
        }

        .info-card,
        .result-card {
            padding: 1.2rem 1.4rem;
            margin-top: 1rem;
        }

        .card-label {
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: var(--label-color);
            margin-bottom: 0.35rem;
        }

        .card-value {
            font-size: 1.9rem;
            font-weight: 800;
            color: var(--title-color);
            margin-bottom: 0.35rem;
        }

        .card-copy {
            color: var(--muted-color);
            margin-bottom: 0;
        }

        div[data-testid="stForm"] {
            background: var(--surface-bg-strong);
            border: 1px solid var(--surface-border);
            border-radius: 24px;
            padding: 1.2rem 1.2rem 0.6rem;
            box-shadow: 0 18px 45px var(--surface-shadow);
        }

        div[data-testid="stForm"] h3 {
            margin-top: 0.2rem;
            margin-bottom: 0.9rem;
            color: var(--title-color);
        }

        .stMarkdown,
        .stText,
        .stCaption {
            color: var(--body-color) !important;
        }

        label,
        .stSlider label,
        .stNumberInput label,
        .stSelectbox label {
            color: var(--title-color) !important;
            font-weight: 600;
        }

        div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div,
        div[data-baseweb="base-input"] > div {
            background: var(--input-bg) !important;
            border: 1px solid var(--input-border) !important;
            border-radius: 14px !important;
            box-shadow: none !important;
        }

        div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div,
        div[data-baseweb="base-input"] > div,
        .stNumberInput input,
        .stTextInput input,
        .stSelectbox div[data-baseweb="select"] * {
            color: var(--input-text) !important;
        }

        .stNumberInput input,
        .stTextInput input {
            background: transparent !important;
        }

        .stNumberInput button {
            background: var(--input-bg) !important;
            border: 1px solid var(--input-border) !important;
        }

        .stNumberInput button:hover {
            background: rgba(22, 78, 99, 0.78) !important;
            border-color: var(--label-color) !important;
        }

        .stSelectbox svg,
        .stNumberInput button,
        .stNumberInput svg {
            color: var(--input-text) !important;
            fill: var(--input-text) !important;
        }

        .stCaption {
            color: var(--muted-color) !important;
        }

        .stSlider [data-baseweb="slider"] {
            padding-top: 0.35rem;
        }

        .stSlider [role="slider"] {
            background: var(--label-color) !important;
            box-shadow: 0 0 0 4px var(--focus-ring);
        }

        .stSlider [data-testid="stTickBar"],
        .stSlider div[data-baseweb="slider"] > div > div {
            background: rgba(148, 163, 184, 0.28) !important;
        }

        div[data-baseweb="popover"] > div,
        div[role="listbox"] {
            background: var(--surface-bg-strong) !important;
            color: var(--input-text) !important;
            border: 1px solid var(--surface-border) !important;
        }

        div[role="option"] {
            color: var(--input-text) !important;
        }

        div[role="option"]:hover {
            background: var(--focus-ring) !important;
        }

        div[data-testid="metric-container"] {
            background: var(--metric-bg);
            border: 1px solid var(--metric-border);
            border-radius: 18px;
            padding: 0.95rem 1rem;
        }

        div[data-testid="stMetricLabel"] {
            color: var(--muted-color) !important;
        }

        div[data-testid="stMetricValue"] {
            color: var(--title-color) !important;
        }

        .stButton > button,
        div[data-testid="stFormSubmitButton"] button {
            width: 100%;
            border-radius: 999px;
            border: none;
            padding: 0.78rem 1rem;
            font-weight: 700;
            background: var(--button-bg);
            color: white;
            box-shadow: 0 14px 30px var(--button-shadow);
        }

        .stButton > button:hover,
        div[data-testid="stFormSubmitButton"] button:hover {
            background: var(--button-bg-hover);
        }

        .stButton > button:focus,
        div[data-testid="stFormSubmitButton"] button:focus {
            outline: none;
            box-shadow: 0 0 0 4px var(--focus-ring);
        }
    </style>
    """,
    unsafe_allow_html=True,
)


def format_inr(value: int) -> str:
    return f"Rs. {value:,.0f}"


st.markdown(
    """
    <div class="hero-card">
        <div class="hero-eyebrow">Premium Intelligence</div>
        <div class="hero-title">Estimate health insurance cost in a cleaner, faster workflow.</div>
        <p class="hero-copy">
            Fill in the applicant profile, lifestyle factors, and plan preference to get an instant premium estimate.
            The prediction logic is unchanged; this update improves the experience, layout, and readability.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

top_stats = st.columns(3)
with top_stats[0]:
    st.markdown(
        """
        <div class="info-card">
            <div class="card-label">Coverage Inputs</div>
            <div class="card-value">12</div>
            <p class="card-copy">Structured fields grouped into a single guided form.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with top_stats[1]:
    st.markdown(
        """
        <div class="info-card">
            <div class="card-label">Risk Signals</div>
            <div class="card-value">Medical + Lifestyle</div>
            <p class="card-copy">Smoking, BMI, medical history, and genetical risk are captured clearly.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with top_stats[2]:
    st.markdown(
        """
        <div class="info-card">
            <div class="card-label">Output</div>
            <div class="card-value">Instant Estimate</div>
            <p class="card-copy">One-click prediction with a more polished result presentation.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


with st.form("premium_prediction_form"):
    st.markdown("### Personal details")
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Age", min_value=18, max_value=100, value=30, step=1)
    with col2:
        gender = st.selectbox("Gender", CATEGORICAL_OPTIONS["Gender"])
    with col3:
        marital_status = st.selectbox("Marital Status", CATEGORICAL_OPTIONS["Marital Status"])

    st.markdown("### Financial and plan details")
    col4, col5, col6 = st.columns(3)
    with col4:
        income_lakhs = st.number_input("Income in lakhs", min_value=0, max_value=200, value=10, step=1)
    with col5:
        number_of_dependants = st.number_input("Number of dependants", min_value=0, max_value=20, value=0, step=1)
    with col6:
        insurance_plan = st.selectbox("Insurance Plan", CATEGORICAL_OPTIONS["Insurance Plan"], index=1)

    st.markdown("### Health and lifestyle")
    col7, col8, col9 = st.columns(3)
    with col7:
        bmi_category = st.selectbox("BMI Category", CATEGORICAL_OPTIONS["BMI Category"])
    with col8:
        smoking_status = st.selectbox("Smoking Status", CATEGORICAL_OPTIONS["Smoking Status"])
    with col9:
        genetical_risk = st.slider("Genetical Risk", min_value=0, max_value=5, value=1)

    st.markdown("### Background")
    col10, col11, col12 = st.columns(3)
    with col10:
        employment_status = st.selectbox("Employment Status", CATEGORICAL_OPTIONS["Employment Status"], index=0)
    with col11:
        region = st.selectbox("Region", CATEGORICAL_OPTIONS["Region"])
    with col12:
        medical_history = st.selectbox("Medical History", CATEGORICAL_OPTIONS["Medical History"])

    submitted = st.form_submit_button("Predict Premium")


input_dict = {
    "Age": age,
    "Number of Dependants": number_of_dependants,
    "Income in Lakhs": income_lakhs,
    "Genetical Risk": genetical_risk,
    "Insurance Plan": insurance_plan,
    "Employment Status": employment_status,
    "Gender": gender,
    "Marital Status": marital_status,
    "BMI Category": bmi_category,
    "Smoking Status": smoking_status,
    "Region": region,
    "Medical History": medical_history,
}


if submitted:
    prediction = predict(input_dict)

    result_col, summary_col = st.columns([1.2, 0.8])
    with result_col:
        st.markdown(
            f"""
            <div class="result-card">
                <div class="card-label">Predicted Premium</div>
                <div class="card-value">{format_inr(prediction)}</div>
                <p class="card-copy">
                    This estimate is based on the applicant information currently entered in the form.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with summary_col:
        st.metric("Selected plan", insurance_plan)
        st.metric("Income profile", f"{income_lakhs} lakhs")
        st.metric("Dependants", int(number_of_dependants))

    st.caption("Use the form inputs to compare how lifestyle, medical history, and plan type affect the estimate.")
