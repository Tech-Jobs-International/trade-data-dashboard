import streamlit as st
from functions.data_fetch_function import country_code, country_name, df_data

# Initialize session state for dropdown selections
if 'selected_country' not in st.session_state:
    st.session_state.selected_country = country_name[0]

if 'selected_country_code' not in st.session_state:
    st.session_state.selected_country_code = country_code[0]

# Streamlit event-driven programming to update options based on selections
def update_country_code():
    filtered_items = df_data[df_data['partnerDesc'] == st.session_state.selected_country]['country_iso3'].unique()
    st.session_state.selected_country_code = (
        st.session_state.selected_country_code if st.session_state.selected_country_code in filtered_items else filtered_items[0]
    )

def update_country_name():
    filtered_categories = df_data[df_data['country_iso3'] == st.session_state.selected_country_code]['partnerDesc'].unique()
    st.session_state.selected_country = (
        st.session_state.selected_country if st.session_state.selected_country in filtered_categories else filtered_categories[0]
    )