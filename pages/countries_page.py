import streamlit as st
import pandas as pd
import numpy as np
import io

from functions.summerize_data import country_summerized_data,country_summerized_filter_data
from functions.summerize_visuals import country_map_vis,country_vis_filters,country_vis_by_value,country_vis_by_hour,country_vis_by_value_filter,country_vis_by_hour_filter
from functions.filter_product_dropdown import df_data, product_code,product_name, update_product_code, update_product_name

# create tab for data set and visuals
visual_tab, data_tab = st.tabs(['Data Visualization','Data Set' ])

# Export to Excel
excel_buffer = io.BytesIO()
with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
    country_summerized_data(df_data).to_excel(writer, index=False, sheet_name='Sheet1')
excel_data = excel_buffer.getvalue()

# Define dropdown options for Multiselect
options = [5,6,7,8,9,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80]  # Steps of 5
dropdown_options = options  # Add "Select All" to the dropdown


with data_tab:
    
    st.subheader("Table to show US values and Hours to produce imports within the US by countries")
    st.download_button(
        label="Download as Excel",
        data=excel_data,
        file_name='country_summerized.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
    st.dataframe(country_summerized_data(df_data), height=300)


with visual_tab:
    with st.container():
        st.markdown('### Exploratory Visuals')
        st.markdown("----")
        st.markdown("#### Map distribution of countries exporting to the USA as at 2022")
        st.plotly_chart(country_map_vis(country_summerized_data(df_data)))
        st.markdown("----")
        selected_value = st.selectbox("Select the number of bar to display:", dropdown_options)
        st.markdown("----")
        st.markdown("#### Top n exporting countries to the USA as at 2022")

        # Create two columns for the plot
        col1, col2 = st.columns(2)  # Adjust the column widths as needed
        with col1:
           st.markdown(f"##### Top {selected_value} export to the USA in value as at 2022")
           st.plotly_chart(country_vis_by_value(country_summerized_data(df_data),selected_value))

        with col2:
           st.markdown(f"##### Top {selected_value} export to the USA in hours as at 2022")
           st.plotly_chart(country_vis_by_hour(country_summerized_data(df_data),selected_value)) 

        st.markdown("----")

        # Create two columns for the filter
        col3, col4 = st.columns(2)  # Adjust the column widths as needed

        with col3:
            selected_product =  st.selectbox(
                "Select a product name:",
                product_name,
                key='selected_product',
                on_change=update_product_code
                )

        with col4:
            selected_item = st.selectbox(
                "Select a product code:",
                product_code,
                key='selected_code',
                on_change=update_product_name
                )

        with st.container():
            # Create two columns for the filter
            col5, col6 = st.columns(2)  # Adjust the column widths as needed
            with col5:
                st.markdown(f"###### Top {selected_value} export of {selected_product} to the USA in value as at 2022")
                st.plotly_chart(country_vis_by_value_filter(country_summerized_filter_data(df_data, selected_item),selected_value))
            with col6:
                st.markdown(f"###### Top {selected_value} export of {selected_product} to the USA in hours as at 2022")
                st.plotly_chart(country_vis_by_hour_filter(country_summerized_filter_data(df_data, selected_item),selected_value)) 
        
