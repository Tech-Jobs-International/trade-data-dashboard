import streamlit as st
import pandas as pd
import io

from functions.summerize_data import product_summerized_data,product_summerized_filter_data
from functions.summerize_visuals import product_vis_filters
from functions.filter_country_dropdown import df_data, update_country_code,update_country_name,country_name,country_code

# create tab for data set and visuals
visual_tab, data_tab = st.tabs(['Data Visualization','Data Set' ])

# Export to Excel
excel_buffer = io.BytesIO()
with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
    product_summerized_data(df_data).to_excel(writer, index=False, sheet_name='Sheet1')
excel_data = excel_buffer.getvalue()


with data_tab:
    
    st.subheader("Table to show US values and Hours to produce imports within the US by countries")
    st.download_button(
        label="Download as Excel",
        data=excel_data,
        file_name='country_summerized.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
    st.dataframe(product_summerized_data(df_data), height=300)


with visual_tab:
    with st.container():
        st.subheader('Exploratory Visuals')
        # Create three columns 
        col1, col2 = st.columns(2)  # Adjust the column widths as needed

        with col1:
             st.selectbox(
                "Select a country name:",
                country_name,
                key='selected_country',
                on_change=update_country_code
                )

        with col2:
            selected_item = st.selectbox(
                "Select a country code:",
                country_code,
                key='selected_country_code',
                on_change=update_country_name
                )
        with st.expander('Visuals'):
            st.plotly_chart(product_vis_filters(product_summerized_filter_data(df_data, selected_item))) 
