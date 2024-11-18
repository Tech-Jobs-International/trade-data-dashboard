import streamlit as st

from functions.data_fetch_function import product_code,product_name,df_data

# Use session state to maintain dropdown selections
if 'selected_product' not in st.session_state:
    st.session_state.selected_product = product_name[0]

if 'selected_code' not in st.session_state:
    st.session_state.selected_code = product_code[0]

# Function to update product code options based on the selected product name
def update_product_code():
    filtered_items = df_data[df_data['cmdDesc'] == st.session_state.selected_product]['cmdCode'].unique()
    if st.session_state.selected_code not in filtered_items:
        st.session_state.selected_code = filtered_items[0]

# Function to update product name options based on the selected product code
def update_product_name():
    filtered_categories = df_data[df_data['cmdCode'] == st.session_state.selected_code]['cmdDesc'].unique()
    if st.session_state.selected_product not in filtered_categories:
        st.session_state.selected_product = filtered_categories[0]