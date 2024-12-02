import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Cache the data loading function
@st.cache_data
def load_data(file_path, sheet_name):
    # Load the Excel file
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df

# Define a function to get unique values
@st.cache_data
def get_unique_values(df, column_name):
    return df[column_name].unique()


## Data Fetching and modification
@st.cache_data
def summarize_data(df, group_by_cols, sum_cols):
    """
    Generic function to summarize data by grouping and summing specified columns.
    Args:
    - df: DataFrame to summarize.
    - group_by_cols: List of columns to group by.
    - sum_cols: List of columns to sum.
    Returns:
    - A DataFrame with the summarized data.
    """
    filtered_df = df[group_by_cols + sum_cols]
    summarized_df = filtered_df.groupby(group_by_cols).sum().reset_index()
    return summarized_df

@st.cache_data
def filter_and_summarize(df, filter_col, filter_value, group_by_cols, sum_cols):
    """
    Filter data by a specific value and summarize.
    Args:
    - df: DataFrame to filter and summarize.
    - filter_col: Column to apply the filter on.
    - filter_value: Value to filter the column by.
    - group_by_cols: Columns to group by after filtering.
    - sum_cols: Columns to sum.
    Returns:
    - A DataFrame with the filtered and summarized data.
    """
    filtered_df = df[df[filter_col] == filter_value]
    return summarize_data(filtered_df, group_by_cols, sum_cols)


## Data Visual Helper
@st.cache_data
def sort_and_filter(df, sort_col, top_n=None, ascending=False):
    """Sort a dataframe by a specified column and optionally limit the results."""
    sorted_df = df.sort_values(by=sort_col, ascending=ascending)
    if top_n:
        return sorted_df.tail(top_n)
    return sorted_df

@st.cache_data
def create_bar_chart(data, x_col, y_col,x_axis_name,y_axis_name, orientation='h',height=None):
    """Create a bar chart with dynamic height."""
    num_bars = len(data)
    base_height = 200
    bar_height = 20
    fig_height = height or (base_height + (bar_height * num_bars))

    fig = go.Figure(go.Bar(x=data[x_col], y=data[y_col], orientation=orientation,name='',text=data['partnerDesc'],hovertemplate=(
        "Country: %{text}<br>" +  # Display country name
        "Rank: %{customdata[0]}<br>" +  # Display rank
        "Value: %{x:,.2f}"  # Display USD value
    ),
    customdata=data[['rank']]
    ))
    fig.update_layout(height=fig_height, xaxis_title=x_axis_name, yaxis_title=y_axis_name,hovermode="closest")
    return fig

@st.cache_data
def create_choropleth_map(df, location_col, color_col,item,width=1500,height=550):
    """Create a choropleth map with a custom color scale."""
    value_col = df['total_hours_needed_to_produce_in_USA'] if item != 'USD-value' else color_col
    color_scale = [
        [0, 'rgba(128, 128, 128, 0.1)'], 
        [0.25, 'rgba(255, 255, 0, 0.4)'],
        [0.5, 'rgba(0, 255, 0, 0.7)'],  
        [1, 'rgba(0, 0, 255, 1)']
    ]

    fig = px.choropleth(
                            df, 
                            locations=location_col, 
                            color=value_col,
                            hover_name='partnerDesc', 
                            hover_data={
                                'country_iso3': False,# Hide the country code from hover
                                'partnerDesc': False},
                            color_continuous_scale=color_scale,
                            labels={'total_hours_needed_to_produce_in_USA': 'Hours',
                                    'constant_usd': 'Exported Value (USD)'} # Rename the color scale
                        )
    
    fig.update_layout(width=width, height=height)

    # Customize the hover template
    fig.update_traces(
         hovertemplate="<b>%{hovertext}</b><br>Value: %{z:,.2f}<extra></extra>"
        )
    return fig

@st.cache_data
def create_treemap(df, path, value_column, item,width=1200,height=600):
    """Create a treemap visualization."""
    value_col = df['total_hours_needed_to_produce_in_USA'] if item != 'USD-value' else value_column
    color_scale = [
        [0, 'rgba(0, 0, 255, 0.1)'],
        [0.25, 'rgba(0, 255, 0, 0.4)'],
        [0.5, 'rgba(255, 255, 0, 0.7)'],
        [0.75, 'rgba(255, 165, 0, 1)'],
        [1, 'rgba(255, 0, 0, 1)']
    ]

    fig = px.treemap(df, path=path, values=value_col, color=value_col, color_continuous_scale=color_scale)
    fig.update_layout(width=width, height=height)
    return fig

# Helper function to format numbers
@st.cache_data
def format_number(value):
    return "{:,}".format(value)

# Helper function to get top exported product or country info
@st.cache_data
def get_top_item_info(df, sort_by, item_key):
    sorted_df = df.sort_values(by=sort_by, ascending=False).head(1)
    return sorted_df[item_key].iloc[0], round(sorted_df[sort_by].iloc[0], 2)
