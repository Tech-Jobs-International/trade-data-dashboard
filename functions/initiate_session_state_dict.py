import streamlit as st


def initialize_session_state_1():
    
    if "countries" not in st.session_state:
        st.session_state["countries"] = {}
    if "filter" not in st.session_state["countries"]:
        st.session_state["countries"]["filter"] = {}