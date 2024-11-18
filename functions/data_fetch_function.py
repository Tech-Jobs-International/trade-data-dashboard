import streamlit as st
import pandas as pd

# call data
df_data = pd.read_excel('data/marged_product_breakdown.xlsx', sheet_name='gdp_per_hour')

# Get unique values of product_name and code
product_name = df_data['cmdDesc'].unique()
product_code = df_data['cmdCode'].unique()

# Get unique values of country name and code
country_name = df_data['partnerDesc'].unique()
country_code = df_data['country_iso3'].unique()