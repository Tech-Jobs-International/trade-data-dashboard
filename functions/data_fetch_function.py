from functions.helper_functions import load_data, get_unique_values

# load Data
df_data = load_data('data/marged_product_breakdown.xlsx', sheet_name='gdp_per_hour')

# Get unique values
product_name = get_unique_values(df_data, 'cmdDesc')
product_code = get_unique_values(df_data, 'cmdCode')
country_name = get_unique_values(df_data, 'partnerDesc')
country_code = get_unique_values(df_data, 'country_iso3')