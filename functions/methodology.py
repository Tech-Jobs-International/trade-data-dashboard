import streamlit as st

from functions.helper_functions import format_number,get_top_item_info

# Constant for total hours worked in the USA
TOTAL_HOURS_WORKED_US = 523670559867
USA_LABOR_FORCE = 263973465


# Cached function to filter and summarize data by country
@st.cache_data
def new_labor_force_country_filt(df, country_iso3=None):
    filtered_df = df[df['country_iso3'] == country_iso3]
    if filtered_df.empty:
        print(f'country_iso3 {country_iso3} does not exist')
        return {}

    product_df = filtered_df['total_hours_needed_to_produce_in_USA'].sum()
    top_exported_product, top_exported_value = get_top_item_info(filtered_df, 'constant_usd', 'cmdDesc')

    return {
        'Total annual hours to produce': format_number(round(product_df, 2)),
        'Top exported product': top_exported_product,
        'Top exported product in $': format_number(top_exported_value)
    }

# Cached function to summarize USA labor force contribution
@st.cache_data
def new_labor_force_country_filt_USA(df, country_iso3=None):
    filtered_df = df[df['country_iso3'] == country_iso3]
    if filtered_df.empty:
        print(f'country_iso3 {country_iso3} does not exist')
        return {}

    product_hours = filtered_df['total_hours_needed_to_produce_in_USA'].sum()
    hours_increase_percentage = product_hours / TOTAL_HOURS_WORKED_US

    return {
        'Annual Hours worked in the USA': format_number(TOTAL_HOURS_WORKED_US),
        'USA Labor Force': format_number(USA_LABOR_FORCE),
        'Percentage share of Working hours': "{:.2%}".format(hours_increase_percentage)
    }

# Cached function to filter and summarize data by product
@st.cache_data
def new_labor_force_product_filt(df, cmdCode=None):
    filtered_df = df[df['cmdCode'] == cmdCode]
    if filtered_df.empty:
        print(f'product code {cmdCode} does not exist')
        return {}

    product_hours = filtered_df['total_hours_needed_to_produce_in_USA'].sum()
    hours_increase_percentage = product_hours / TOTAL_HOURS_WORKED_US
    top_exporting_country, top_exporting_value = get_top_item_info(filtered_df, 'constant_usd', 'partnerDesc')

    return {
        'Total annual hours to produce': format_number(round(product_hours, 2)),
        'Top exporting country': top_exporting_country,
        'Top exporting value in $': format_number(top_exporting_value),
        'USA Labor Force': format_number(USA_LABOR_FORCE),
        'Percentage share of Working hours': "{:.2%}".format(hours_increase_percentage)
    }
