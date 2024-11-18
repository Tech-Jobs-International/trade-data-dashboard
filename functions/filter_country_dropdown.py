import streamlit as st

from functions.data_fetch_function import country_code,country_name,df_data

# Use session state to maintain dropdown selections
if 'selected_country' not in st.session_state:
    st.session_state.selected_country = country_name[0]

if 'selected_country_code' not in st.session_state:
    st.session_state.selected_country_code = country_code[0]

# Function to update country code options based on the selected country name
def update_country_code():
    filtered_items = df_data[df_data['partnerDesc'] == st.session_state.selected_country]['country_iso3'].unique()
    if st.session_state.selected_country_code not in filtered_items:
        st.session_state.selected_country_code = filtered_items[0]

# Function to update country name options based on the selected country code
def update_country_name():
    filtered_categories = df_data[df_data['country_iso3'] == st.session_state.selected_country_code]['partnerDesc'].unique()
    if st.session_state.selected_country not in filtered_categories:
        st.session_state.selected_country = filtered_categories[0]