import streamlit as st
import pandas as pd
import io

from functions.data_fetch_function import df_data
from functions.summerize_data import (
    country_summerized_data,
    country_summerized_filter_data
)
from functions.summerize_visuals import (
    country_map_vis,
    country_vis_by_value,
    country_vis_by_hour
)
from functions.filter_product_dropdown import (
    product_code,
    product_name,
    update_product_code,
    update_product_name
)
from functions.methodology import (
    new_labor_force_country_filt,
    new_labor_force_country_filt_USA
)
from functions.filter_country_dropdown import (
    update_country_code,
    update_country_name,
    country_name,
    country_code
)

# Cache results
@st.cache_data
def get_country_summarized_data():
    return country_summerized_data(df_data)

@st.cache_data
def export_to_excel(dataframe):
    excel_buffer = io.BytesIO()
    with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
        dataframe.to_excel(writer, index=False, sheet_name='Sheet1')
    return excel_buffer.getvalue()

# Prepare data
country_data = get_country_summarized_data()
excel_data = export_to_excel(country_data)

# Define dropdown options
dropdown_options = list(range(5, 85, 5))

# create tab for data set and visuals
visual_tab, data_tab = st.tabs(['Data Visualization','Data Set' ])

with data_tab:
    st.markdown("##### Table Displaying U.S. Import Values and Hours Required for Domestic Production by Country in 2022")
    st.download_button(
        label="Download as Excel",
        data=excel_data,
        file_name='country_summerized.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    st.dataframe(country_data, height=300)
    st.markdown("----")
    st.markdown("##### Impact of Domestic Production of a Country's Exports in the USA in 2022")

    col1, col2 = st.columns(2)
    selected_country = col1.selectbox(
        "Select a country name:",
        country_name,
        key='selected_country',
        on_change=update_country_code
    )
    selected_item = col2.selectbox(
        "Select a country code:",
        country_code,
        key='selected_country_code',
        on_change=update_country_name
    )

    col3, col4 = st.columns(2)
    col3.markdown(f"##### {selected_country} perspective")
    col3.dataframe(new_labor_force_country_filt(df_data, selected_item))

    col4.markdown("##### USA perspective")
    col4.dataframe(new_labor_force_country_filt_USA(df_data, selected_item))


with visual_tab:
    st.markdown('### Exploratory Visuals')
    st.markdown("##### Map showing the distribution of countries exporting to the USA in 2022")
    value_type = st.selectbox('Select value type:', ['USD-value', 'Hours'])
    st.plotly_chart(country_map_vis(country_data,value_type))
    st.markdown("----")

    selected_value = st.selectbox("Select the number of bar to display:", dropdown_options)
    st.markdown("#### Top N Exporting Countries to the USA in 2022")

    col1, col2 = st.columns(2)
    col1.markdown(f"##### Top {selected_value} Export to the USA by value in 2022")
    col1.plotly_chart(country_vis_by_value(country_data, selected_value))

    col2.markdown(f"##### Top {selected_value} Export to the USA by hours in 2022")
    col2.plotly_chart(country_vis_by_hour(country_data, selected_value))

    st.markdown("----")

    col3, col4 = st.columns(2)
    selected_product = col3.selectbox(
        "Select a product name:",
        product_name,
        key='selected_product',
        on_change=update_product_code
    )
    selected_product_code = col4.selectbox(
        "Select a product code:",
        product_code,
        key='selected_code',
        on_change=update_product_name
    )

    filtered_data = country_summerized_filter_data(df_data, selected_product_code)

    col5, col6 = st.columns(2)
    col5.markdown(f"###### Top {selected_value} Export of {selected_product} to the USA by value in 2022")
    col5.plotly_chart(country_vis_by_value(filtered_data, selected_value))

    col6.markdown(f"###### Top {selected_value} Export of {selected_product} to the USA by hours in 2022")
    col6.plotly_chart(country_vis_by_hour(filtered_data, selected_value))
        
