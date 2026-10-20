from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Databytes Learning Labs",
    page_icon="D",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT = Path(__file__).parent
LABS = {
    "Overfitting Lab": {
        "file": ROOT / "labs" / "overfitting.html",
        "description": "Explore model complexity, training error, and generalization.",
        "height": 1500,
    },
    "Ridge, Lasso & Elastic Net": {
        "file": ROOT / "labs" / "regularization.html",
        "description": "Experiment with regularization and compare coefficient behaviour.",
        "height": 1500,
    },
    "Prompt Injection in LLMs": {
        "file": ROOT / "labs" / "prompt_injection.html",
        "description": "Explore prompt-injection scenarios and defensive strategies.",
        "height": 1400,
    },
}

st.markdown(
    """
    <style>
    .block-container {max-width: 1500px; padding-top: 1.4rem; padding-bottom: 2rem;}
    [data-testid="stSidebar"] {border-right: 1px solid rgba(128,128,128,.18);}
    .db-subtitle {opacity: .75; margin-top: -.5rem; margin-bottom: 1.2rem;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Databytes Learning Labs")
st.markdown(
    '<p class="db-subtitle">Interactive simulations for machine learning and AI security.</p>',
    unsafe_allow_html=True,
)

with st.sidebar:
    st.subheader("Learning Labs")
    selected = st.radio("Choose a lab", list(LABS.keys()), label_visibility="collapsed")
    st.divider()
    st.caption("Select a lab to load its interactive simulation.")

lab = LABS[selected]
st.subheader(selected)
st.write(lab["description"])

if not lab["file"].exists():
    st.error(f"Lab file is missing: {lab['file'].name}")
else:
    html = lab["file"].read_text(encoding="utf-8")
    components.html(html, height=lab["height"], scrolling=True)

st.divider()
st.caption("Databytes • Interactive learning experiences")
