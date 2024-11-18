import streamlit as st

from functions.data_fetch_function import df_data
from functions.methodology import objective, data_description, data_sources,steps,new_labor_force_country_filt,new_labor_force_product_filt,limitation,assumption
from functions.filter_country_dropdown import df_data, update_country_code,update_country_name,country_name,country_code
from functions.filter_product_dropdown import df_data, product_code,product_name, update_product_code, update_product_name


# create tab for data set and visuals
methodology_tab, limitation_tab = st.tabs(['Methodology','Limitations'])

with methodology_tab:
    st.header("Labor force effect on import production")
    st.markdown("**Introduction**")
    st.markdown("The essence of this exercise aims to provide insight on the practically of the United State of America (USA) being able to produce it's imports products and services internal thereby improving the gross domestic product (GDP) of the USA")
    st.markdown("**Objectives**")
    st.markdown(objective)
    st.markdown("**Prerequisite**")
    st.markdown("To follow along, you should have a basic understanding of Python, data analysis libraries like Pandas, numpy etc and knowledge of Scikit learn for Marching Learning.")
    st.markdown("**Data Sources**")
    st.markdown(data_sources)
    st.markdown("**Data Description**")
    st.markdown(data_description)
    st.markdown("**Procedure:**")
    st.markdown(steps)
    st.subheader("Result")
    st.dataframe(df_data)

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
    with st.expander('results'):
            st.dataframe(new_labor_force_country_filt(df_data,selected_item))

    col3, col4 = st.columns(2) # dropdown for products
    with col3:
             st.selectbox(
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
    with st.expander('results'):
            st.dataframe(new_labor_force_product_filt(df_data,selected_item))

with limitation_tab:
        st.subheader("Limitations")
        st.markdown("The limitations identified are as follows:")
        st.markdown(limitation)
        st.subheader("Assumptions")
        st.markdown("The assumptions are as follows:")
        st.markdown(assumption)

