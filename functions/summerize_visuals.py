import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

@st.cache_data
def country_vis(df_data):
    vis_data = df_data.copy()

    # sort value in ascending order
    vis_data_value_asc = vis_data.sort_values(by='constant_usd', ascending=False).head(10)
    vis_data_hour_asc = vis_data.sort_values(by='total_hours_needed_to_produce_in_USA', ascending=False).head(10)

    # Create a 1x2 subplot grid
    fig = make_subplots(rows=1, 
                        cols=2, 
                        subplot_titles=("Top 10  Export in USD Value", 
                                        "Top 10  Export in Hours to Product in USA"
                                        )
                    )

    # Add data to the first top subplot
    fig.add_trace(
        go.Bar(x=vis_data_value_asc['constant_usd'], 
               y=vis_data_value_asc['country_iso3'], 
               name='Top 10  Export in USD Value',
               orientation='h'
               ),
        row=1, col=1
    )

    # Add data to the second top subplot
    fig.add_trace(
        go.Bar(x=vis_data_hour_asc['total_hours_needed_to_produce_in_USA'], 
               y=vis_data_hour_asc['country_iso3'], 
               name='Top 10  Export in Hours to Product in USA',
                orientation='h'
               ),
        row=1, col=2
    )

    return fig

@st.cache_data
def country_vis_by_hour(df_data,top_n):
    vis_data = df_data.copy()

    # sort value in ascending order
    vis_data_hour_asc = vis_data.sort_values(by='total_hours_needed_to_produce_in_USA', ascending=False).head(top_n)

    # Dynamically set figure height based on the number of bars
    num_bars = len(vis_data_hour_asc)
    base_height = 200  # Minimum height
    bar_height = 20    # Additional height per bar

    fig_height = base_height + (bar_height * num_bars)


    # Add data to the figure
    fig = go.Figure(
        data=[
            go.Bar(
                x=vis_data_hour_asc['total_hours_needed_to_produce_in_USA'], 
                y=vis_data_hour_asc['country_iso3'], 
                orientation='h'
            )
        ]
    )
    # Update layout with dynamic height
    fig.update_layout(
        height=fig_height,
        xaxis_title="Hours",
        yaxis_title="Country"
    )

    return fig

@st.cache_data
def country_vis_by_value(df_data,top_n):
    vis_data = df_data.copy()

    # sort value in ascending order
    vis_data_value_asc = vis_data.sort_values(by='constant_usd', ascending=False).head(top_n)      

    # Dynamically set figure height based on the number of bars
    num_bars = len(vis_data_value_asc)
    base_height = 200  # Minimum height
    bar_height = 20    # Additional height per bar

    fig_height = base_height + (bar_height * num_bars)

    # Add data to the figure
    fig = go.Figure(
        data=[
            go.Bar(
                x=vis_data_value_asc['constant_usd'], 
                y=vis_data_value_asc['country_iso3'], 
                name='Top Export in USD Value',
                orientation='h'
            )
        ]
    )

    # Update layout with dynamic height
    fig.update_layout(
        height=fig_height,
        xaxis_title="USD value",
        yaxis_title="Country"
    )
    
    return fig


@st.cache_data
def country_map_vis(df_data):
    vis_date = df_data.copy()

    # sort value in ascending order
    vis_data_value_asc = vis_date.sort_values(by='constant_usd', ascending=False)
    # vis_data_hour_asc = vis_date.sort_values(by='total_hours_needed_to_produce_in_USA', ascending=False)

    # Create a custom blue-to-white color scale
    blue_to_white_scale = [
        [0, 'rgba(128, 128, 128, 0.1)'],   # grey with 10% opacity
        [0.25, 'rgba(255, 255, 0, 0.4)'], # Yellow with 40% opacity
        [0.5, 'rgba(0, 255, 0, 0.7)'], # Green with 70% opacity
        [1, 'rgba(0, 0, 255, 1)'],      # Blue with full opacity
    ]
    # [(0, "grey"),(0.5, "green"), (1, "blue")]

    # Create a choropleth map using Plotly Express
    fig = px.choropleth(vis_data_value_asc, 
                    locations="country_iso3",  # ISO3 country codes
                    color="constant_usd",  # Data to color the countries by
                    hover_data = ["constant_usd", "total_hours_needed_to_produce_in_USA"],
                    color_continuous_scale=blue_to_white_scale,  # Color scale
                    )
    
    # Update the figure size
    fig.update_layout(
        width=1500,  # Set the width of the figure
        height=550,  # Set the height of the figure
    )

    
    return fig

@st.cache_data
def country_vis_filters(df_data):
    vis_data = df_data.copy()

    # sort value in ascending order
    vis_data_value_asc = vis_data.sort_values(by='constant_usd', ascending=True).head(10)
    vis_data_hour_asc = vis_data.sort_values(by='total_hours_needed_to_produce_in_USA', ascending=True).head(10)

    # Create a 1x2 subplot grid
    fig = make_subplots(rows=1, 
                        cols=2, 
                        subplot_titles=("Top 10  Export in USD Value", 
                                        "Top 10  Export in Hours to Produce in USA"))

    # Add data to the first top subplot
    fig.add_trace(
            go.Bar(
                x=vis_data_value_asc['constant_usd'],
                y=vis_data_value_asc['country_iso3'], 
                name='Top 10  Export in USD Value',
                orientation='h'
            ),
        row=1, col=1
    )

    # Add data to the second top subplot
    fig.add_trace(
        go.Bar(x=vis_data_hour_asc['total_hours_needed_to_produce_in_USA'], 
               y=vis_data_hour_asc['country_iso3'],
               name='Top 10  Export in Hours to Product in USA',
               orientation='h'
               ),
        row=1, col=2
    )

    return fig

@st.cache_data
def country_vis_by_hour_filter(df_data,top_n):
    vis_data = df_data.copy()

    # sort value in ascending order
    vis_data_hour_asc = vis_data.sort_values(by='total_hours_needed_to_produce_in_USA', ascending=False).head(top_n)

    # Dynamically set figure height based on the number of bars
    num_bars = len(vis_data_hour_asc)
    base_height = 200  # Minimum height
    bar_height = 20    # Additional height per bar

    fig_height = base_height + (bar_height * num_bars)


    # Add data to the figure
    fig = go.Figure(
        data=[
            go.Bar(
                x=vis_data_hour_asc['total_hours_needed_to_produce_in_USA'], 
                y=vis_data_hour_asc['country_iso3'], 
                orientation='h'
            )
        ]
    )
    # Update layout with dynamic height
    fig.update_layout(
        height=fig_height,
        xaxis_title="Hours",
        yaxis_title="Country"
    )

    return fig

@st.cache_data
def country_vis_by_value_filter(df_data,top_n):
    vis_data = df_data.copy()

    # sort value in ascending order
    vis_data_value_asc = vis_data.sort_values(by='constant_usd', ascending=False).head(top_n)      

    # Dynamically set figure height based on the number of bars
    num_bars = len(vis_data_value_asc)
    base_height = 200  # Minimum height
    bar_height = 20    # Additional height per bar

    fig_height = base_height + (bar_height * num_bars)

    # Add data to the figure
    fig = go.Figure(
        data=[
            go.Bar(
                x=vis_data_value_asc['constant_usd'], 
                y=vis_data_value_asc['country_iso3'], 
                name='Top Export in USD Value',
                orientation='h'
            )
        ]
    )

    # Update layout with dynamic height
    fig.update_layout(
        height=fig_height,
        xaxis_title="USD value",
        yaxis_title="Country"
    )
    
    return fig

# @st.cache_data
# def product_vis(df_data):

    # vis_data = df_data.copy()

    # # sort value in ascending order
    # vis_data_value_asc = vis_data.sort_values(by='constant_usd', ascending=False).head(10)
    # vis_data_hour_asc = vis_data.sort_values(by='total_hours_needed_to_produce_in_USA', ascending=False).head(10)

    # # sort in descending order
    # vis_data_value_dsc = vis_data.sort_values(by='constant_usd', ascending=False).tail(10)
    # vis_data_hour_dsc = vis_data.sort_values(by='total_hours_needed_to_produce_in_USA', ascending=False).tail(10)
    # # Create a 1x2 subplot grid
    # fig = make_subplots(rows=2, 
    #                     cols=2, 
    #                     subplot_titles=("Top 10  Export in USD Value", 
    #                                     "Top 10  Export in Hours to Product in USA",
    #                                     "Bottom 10  Export in USD Value", 
    #                                     "Bottom 10  Export in Hours to Product in USA",))

    # # Add data to the first top subplot
    # fig.add_trace(
    #     go.Bar(x=vis_data_value_asc['cmdDesc'], 
    #            y=vis_data_value_asc['constant_usd'], 
    #            name='Top 10  Export in USD Value'
    #            ),
    #     row=1, col=1
    # )

    # # Add data to the second top subplot
    # fig.add_trace(
    #     go.Bar(x=vis_data_hour_asc['cmdDesc'], 
    #            y=vis_data_hour_asc['total_hours_needed_to_produce_in_USA'], 
    #            name='Top 10  Export in Hours to Product in USA'
    #            ),
    #     row=1, col=2
    # )

    # # Add data to the first bottom subplot
    # fig.add_trace(
    #     go.Bar(x=vis_data_value_dsc['cmdDesc'], 
    #            y=vis_data_value_dsc['constant_usd'], 
    #            name='Bottom 10  Export in USD Value'
    #            ),
    #     row=2, col=1
    # )

    # # Add data to the second bottom subplot
    # fig.add_trace(
    #     go.Bar(x=vis_data_hour_dsc['cmdDesc'], 
    #            y=vis_data_hour_dsc['total_hours_needed_to_produce_in_USA'], 
    #            name='Bottom 10 Export in Hours to Product in USA'
    #            ),
    #     row=2, col=2
    # )

    # return fig

@st.cache_data
def product_vis_filters(df_data):

    vis_data = df_data.copy()
    # sort value in ascending order
    vis_data_value_asc = vis_data.sort_values(by='constant_usd', ascending=True)
    vis_data_hour_asc = vis_data.sort_values(by='total_hours_needed_to_produce_in_USA', ascending=True)

    # Create a 1x2 subplot grid
    fig = make_subplots(rows=2, 
                        cols=1, 
                        subplot_titles=("Export in USD Value", 
                                        "Export in Hours to Produce in USA"))

    # Add data to the first top subplot
    fig.add_trace(
            go.Bar(
                x=vis_data_value_asc['cmdCode'],
                y=vis_data_value_asc['constant_usd'],
                text = vis_data_value_asc['cmdDesc'],
                hoverinfo='text'
            ),
        row=1, col=1
    )

    # Add data to the second top subplot
    fig.add_trace(
        go.Bar(
                x=vis_data_hour_asc['cmdCode'],
                y=vis_data_hour_asc['total_hours_needed_to_produce_in_USA'],
                text = vis_data_value_asc['cmdDesc'],
                hoverinfo='text'
            ),
        row=2, col=1
    )

    fig.update_layout(height=800, width=600, title_text="Product Export Visualizations")
    return fig

@st.cache_data
def product_viz_treemap(df_data, item):
    vis_data = df_data.copy()
    # sort value in ascending order
    vis_data_value_asc = vis_data.sort_values(by='constant_usd', ascending=True)

    # Choose the column to display based on selection
    value_column = vis_data_value_asc['constant_usd'] if item == 'USD-value' else vis_data_value_asc['total_hours_needed_to_produce_in_USA']        

    # Define a custom color scale with RGBA values (RGB with Opacity)
    colorscale = [
        [0, 'rgba(0, 0, 255, 0.1)'],   # Blue with 10% opacity
        [0.25, 'rgba(0, 255, 0, 0.4)'], # Green with 40% opacity
        [0.5, 'rgba(255, 255, 0, 0.7)'], # Yellow with 70% opacity
        [0.75, 'rgba(255, 165, 0, 1)'], # Orange with full opacity
        [1, 'rgba(255, 0, 0, 1)'],      # Red with full opacity
    ]

    # Prepare the data for the Treemap
    fig = px.treemap(
                vis_data_value_asc,
                path=['country_iso3','cmdDesc'],
                values=value_column,
                color=value_column, 
                color_continuous_scale= colorscale
            )

    # Set titles and labels
    fig.update_layout(
        xaxis=dict(title='value'),
        yaxis=dict(title='country'),
        coloraxis_showscale=True,
        width=1200,  # Adjust width as needed
        height=600  # Adjust height as needed
    )

    return fig