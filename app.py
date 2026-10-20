
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Databytes Learning Labs",
    page_icon="D",
    layout="wide",
)

ROOT = Path(__file__).parent
LABS_DIR = ROOT / "labs"

st.title("Databytes Learning Labs")
st.caption("Interactive simulations for machine learning and AI.")

# Automatically discover all HTML files in the labs folder
html_files = sorted(
    LABS_DIR.glob("*.html"),
    key=lambda p: p.stem.lower()
)

if not html_files:
    st.warning("No HTML labs found. Upload HTML files to the labs folder.")
    st.stop()

# Convert filenames into readable sidebar labels
def format_title(path):
    return path.stem.replace("_", " ").replace("-", " ").title()

lab_map = {format_title(path): path for path in html_files}

with st.sidebar:
    st.subheader("Learning Labs")
    selected = st.radio(
        "Choose a lab",
        list(lab_map.keys()),
        label_visibility="collapsed",
    )

lab_file = lab_map[selected]

st.subheader(selected)

html = lab_file.read_text(encoding="utf-8")
components.html(html, height=1500, scrolling=True)

st.divider()
st.caption("Databytes • Interactive learning experiences")
