import streamlit as st
import pandas as pd

from functions.helper_functions import summarize_data, filter_and_summarize

# Define columns to group by and sum for each data type
country_group_by_cols = ['partnerDesc', 'country_iso3', 'GDP_per_hour']
country_sum_cols = ['constant_usd', 'total_hours_needed_to_produce_in_USA']

product_group_by_cols = ['cmdCode', 'cmdDesc']
product_sum_cols = ['constant_usd', 'total_hours_needed_to_produce_in_USA']

@st.cache_data
def country_summerized_data(df_data_country):
    new_df_data = summarize_data(df_data_country, country_group_by_cols, country_sum_cols)

    return new_df_data

@st.cache_data
def country_summerized_filter_data(df_data_country, selected_item):
    new_df_data = filter_and_summarize(df_data_country, 'cmdCode', selected_item, country_group_by_cols, country_sum_cols)

    return new_df_data


@st.cache_data
def product_summerized_data(df_data_product):
    new_df_data = summarize_data(df_data_product, product_group_by_cols, product_sum_cols)

    return new_df_data

@st.cache_data
def product_summerized_filter_data(df_data_product, selected_item):
    new_df_data = filter_and_summarize(df_data_product, 'country_iso3', selected_item, product_group_by_cols, product_sum_cols)

    return new_df_data
