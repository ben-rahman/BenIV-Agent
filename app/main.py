# main.py

import streamlit as st
from memory_manager import LongTermMemory

# Dummy causal reasoning placeholder
def causal_reasoning_placeholder():
    return "Causal output: Salt intake increases systolic pressure based on IV analysis."

# Setup
st.set_page_config(page_title="BenIV-Agent", layout="wide")
st.title("🧠 BenIV-Agent Dashboard")

# Tabs
tab1, tab2 = st.tabs(["🧠 Memory Context", "📈 Causal Reasoning"])

with tab1:
    st.header("Long-Term Memory")
    mem = LongTermMemory()
    mem.add_entry("User asked about blood pressure thresholds.")
    mem.add_entry("System explained systolic and diastolic concepts.")
    mem.add_entry("User asked how salt affects blood pressure.")
    st.write("Recent Context Entries:")
    for entry in mem.retrieve_recent():
        st.success(f"- {entry}")

with tab2:
    st.header("Instrumental Variable Reasoning")
    st.write(causal_reasoning_placeholder())
    st.info("This is a placeholder for IV-based causal inference using DoWhy.")
