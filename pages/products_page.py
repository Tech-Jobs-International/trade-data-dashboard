import streamlit as st
import pandas as pd
import io

# Import custom functions
from functions.data_fetch_function import df_data
from functions.summerize_data import product_summerized_data
from functions.summerize_visuals import product_viz_treemap
from functions.methodology import new_labor_force_product_filt
from functions.filter_product_dropdown import (
    product_code,
    product_name,
    update_product_code,
    update_product_name
)

# Cache the results of product summary data to avoid recalculation
@st.cache_data
def get_summarized_data():
    return product_summerized_data(df_data)

# Cache the Excel export functionality
@st.cache_data
def export_to_excel(dataframe):
    excel_buffer = io.BytesIO()
    with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
        dataframe.to_excel(writer, index=False, sheet_name='Sheet1')
    return excel_buffer.getvalue()

# Prepare data
summarized_data = get_summarized_data()
excel_data = export_to_excel(summarized_data)

# User Interface
visual_tab, data_tab = st.tabs(['Data Visualization', 'Data Set'])

with data_tab:
    st.markdown("#### Table to show product export values and production hours within the USA as at 2022")
    st.download_button(
        label="Download as Excel",
        data=excel_data,
        file_name='product_summerized.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    st.dataframe(summarized_data, height=300)
    st.markdown("---")
    st.markdown("##### Summary performance report of products exported to the USA as at 2022")

    col1, col2 = st.columns(2)
    selected_product = col1.selectbox(
        "Select a product name:",
        product_name,
        key='selected_product',
        on_change=update_product_code
    )

    selected_item = col2.selectbox(
        "Select a product code:",
        product_code,
        key='selected_code',
        on_change=update_product_name
    )

    # Display filtered data
    st.dataframe(new_labor_force_product_filt(df_data, selected_item))

with visual_tab:
    st.subheader('Exploratory Visuals')
    st.markdown("#### Top product export of each country to the USA as at 2022")
    value_type = st.selectbox('Select value type:', ['USD-value', 'Hours'])
    st.plotly_chart(product_viz_treemap(df_data, value_type))