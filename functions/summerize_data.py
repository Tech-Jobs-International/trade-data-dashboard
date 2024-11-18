import streamlit as st
import pandas as pd

@st.cache_data
def country_summerized_data(df_data_country):
    countries_data = df_data_country.copy()
    filterd_countries = countries_data.loc[:,['partnerDesc','country_iso3','constant_usd', 'GDP_per_hour','total_hours_needed_to_produce_in_USA']]
    new_df_data = filterd_countries.groupby(['partnerDesc', 'country_iso3', 'GDP_per_hour']).sum().reset_index()

    return new_df_data

@st.cache_data
def country_summerized_filter_data(df_data_country, selected_item):
    item = selected_item
    countries_data = df_data_country[df_data_country['cmdCode'] == item].copy()
    filterd_countries = countries_data.loc[:,['partnerDesc','country_iso3','constant_usd', 'GDP_per_hour','total_hours_needed_to_produce_in_USA']]
    new_df_data = filterd_countries.groupby(['partnerDesc', 'country_iso3', 'GDP_per_hour']).sum().reset_index()

    return new_df_data


@st.cache_data
def product_summerized_data(df_data_product):
    product_data = df_data_product.copy()
    filterd_products = product_data.loc[:,['cmdCode','cmdDesc','constant_usd','total_hours_needed_to_produce_in_USA']]
    new_df_data = filterd_products.groupby(['cmdCode', 'cmdDesc']).sum().reset_index()

    return new_df_data

@st.cache_data
def product_summerized_filter_data(df_data_product, selected_item):
    item = selected_item
    countries_data = df_data_product[df_data_product['country_iso3'] == item].copy()
    filterd_countries = countries_data.loc[:,['cmdDesc','cmdCode','constant_usd','total_hours_needed_to_produce_in_USA']]
    new_df_data = filterd_countries.groupby(['cmdDesc', 'cmdCode']).sum().reset_index()

    return new_df_data
