import streamlit as st
import pandas as pd
import io

from functions.summerize_data import product_summerized_data
from functions.summerize_visuals import product_viz_treemap
from functions.filter_product_dropdown import df_data, product_code,product_name, update_product_code, update_product_name
from functions.methodology import new_labor_force_product_filt

# create tab for data set and visuals
visual_tab, data_tab = st.tabs(['Data Visualization','Data Set' ])

# Export to Excel
excel_buffer = io.BytesIO()
with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
    product_summerized_data(df_data).to_excel(writer, index=False, sheet_name='Sheet1')
excel_data = excel_buffer.getvalue()


with data_tab:
    
    st.markdown("#### Table to show US values and Hours to produce imports within the US by countries as at 2022")
    st.download_button(
        label="Download as Excel",
        data=excel_data,
        file_name='country_summerized.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
    st.dataframe(product_summerized_data(df_data), height=300)
    st.markdown("---")
    st.markdown("##### Summery performance report of products exported to the USA as at 2022")
    col1, col2 = st.columns(2)  # Adjust the column widths as needed

    with col1:
            selected_product =  st.selectbox(
                "Select a product name:",
                product_name,
                key='selected_product',
                on_change=update_product_code
                )

    with col2:
            selected_item = st.selectbox(
                "Select a product code:",
                product_code,
                key='selected_code',
                on_change=update_product_name
                )
    with st.container():         
        st.dataframe(new_labor_force_product_filt(df_data,selected_item))


with visual_tab:
    with st.container():
        st.subheader('Exploratory Visuals')
        # Create three columns 
        with st.container():
            st.markdown("#### Top product export of each country to the USA as at 2022 ")
            value_type = st.selectbox('Select value type:', ['USD-value', 'Hours'])
            st.plotly_chart(product_viz_treemap(df_data, value_type)) 
