import streamlit as st

from functions.data_fetch_function import df_data
from functions.methodology import steps,new_labor_force_country_filt,new_labor_force_product_filt,limitation,assumption,introduction
from functions.filter_country_dropdown import df_data, update_country_code,update_country_name,country_name,country_code
from functions.filter_product_dropdown import df_data, product_code,product_name, update_product_code, update_product_name


# create tab for data set and visuals
methodology_tab, results ,limitation_tab = st.tabs(['Methodology','Results','Limitations'])

with methodology_tab:
    st.markdown("###  Labor force effect on import production within the USA as at 2022")
    st.info(introduction)
    st.markdown("""----""")
    st.info(steps)

with results: 
        st.subheader("Results")
        st.markdown("This data set serves as the source dataframe after pulling and merging the different data source ")
        st.dataframe(df_data)
        st.markdown("""----""")
        st.markdown("### **Effect of producing a country's exports within the USA**")
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
        
        st.dataframe(new_labor_force_country_filt(df_data,selected_item))

        col5, col6 = st.columns(2) # dropdown for products
        with col5:
             st.selectbox(
                "Select a product name:",
                product_name,
                key='selected_product',
                on_change=update_product_code
                )

        with col6:
            selected_item = st.selectbox(
                "Select a product code:",
                product_code,
                key='selected_code',
                on_change=update_product_name
                )
        st.dataframe(new_labor_force_product_filt(df_data,selected_item))

with limitation_tab:
        st.subheader("Limitations")
        st.markdown("The limitations identified are as follows:")
        st.markdown(limitation)
        st.subheader("Assumptions")
        st.markdown("The assumptions are as follows:")
        st.markdown(assumption)

