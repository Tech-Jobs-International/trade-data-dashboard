import streamlit as st
from  functions.initiate_session_state_dict import initialize_session_state_1

st.set_page_config(
    # layout="wide",
    page_title="US Imports",
    page_icon="assets/images/logo_1.png",
    )

initialize_session_state_1()
countries_page = st.Page("pages/countries_page.py", title="Exporters", icon="🇺🇸")
#products_page = st.Page("pages/products_page.py", title="Products Analysis", icon="🇺🇸")
methodology_page = st.Page("pages/methodology_page.py", title="Methodology", icon="🇺🇸")


pg = st.navigation([methodology_page,countries_page])
pg.run()
