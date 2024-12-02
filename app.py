import streamlit as st
from  functions.initiate_session_state_dict import initialize_session_state_1

st.set_page_config(
    # layout="wide",
    page_title="National Accounting: Effects of the US to produce goods and services imported locally",
    page_icon="assets/images/logo_1.png",
    )

initialize_session_state_1()
countries_page = st.Page("pages/countries_page.py", title="Country Analysis", icon="🇺🇸")
products_page = st.Page("pages/products_page.py", title="Products Analysis", icon="🇺🇸")
methodology_page = st.Page("pages/methodology_page.py", title="Methodology", icon="🇺🇸")


pg = st.navigation([methodology_page,countries_page, products_page])
pg.run()
