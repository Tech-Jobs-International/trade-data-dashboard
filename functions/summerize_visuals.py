import streamlit as st

from functions.helper_functions import sort_and_filter, create_bar_chart, create_choropleth_map, create_treemap

@st.cache_data
def country_vis_by_hour(df_data,top_n):

    # sort value in ascending order
    vis_data_hour_asc = sort_and_filter(df_data, 'total_hours_needed_to_produce_in_USA', top_n)

    #plot bar chart
    fig =  create_bar_chart(vis_data_hour_asc, 'total_hours_needed_to_produce_in_USA', 'country_iso3')

    return fig

@st.cache_data
def country_vis_by_value(df_data,top_n):  

    # sort value in ascending order
    vis_data_value_asc = sort_and_filter(df_data, 'constant_usd', top_n)

    #plot bar chart
    fig =  create_bar_chart(vis_data_value_asc, 'constant_usd', 'country_iso3')
    
    return fig

@st.cache_data
def country_map_vis(df_data):

    # sort value in ascending order
    vis_data_value_asc = sort_and_filter(df_data, 'constant_usd')

    # Plot map
    fig = create_choropleth_map(vis_data_value_asc, 'country_iso3', 'constant_usd', ['constant_usd', 'total_hours_needed_to_produce_in_USA'],3000,550)

    
    return fig

@st.cache_data
def product_viz_treemap(df_data, item):
    
    # sort value in ascending order
    vis_data_value_asc = sort_and_filter(df_data, 'constant_usd','',True)

    # Plt tree map
    fig = create_treemap(vis_data_value_asc, ['country_iso3', 'cmdDesc'], 'constant_usd', item, 1200, 600)

    return fig