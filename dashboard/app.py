
import dash # dash library give us structure to present data
from dash import dcc, html, Input, Output #dash component
import plotly.express as px #graphing library put ont the structure on dash
import duckdb
import pandas as pd




with duckdb.connect("../air_quality.db", read_only=True) as db_connection:
    df = db_connection.execute(
        "SELECT * FROM presentation.air_quality"
    ).fetch_df()
    latest_values_df = db_connection.execute(
        "SELECT * FROM presentation.latest_param_values_per_location"
    ).fetch_df()
    daily_stats_df = db_connection.execute(
        "SELECT * FROM presentation.daily_air_quality_stats"
    ).fetch_df()

def map_figure():
    map_fig = px.scatter_map(
        latest_values_df,
        lat = "lat",
        lon = "lon",
        hover_name="location",
        hover_data={
            "lat":False,
            "lon":True,
            "datetime":True,
            "pm10":True,
            "pm25":True,
            "so2":True,
        },
        zoom = 6.0
    )

    map_fig.update_layout(
        mapbox_style = "open-street-map",
        height=800,
        title="Air Quality monitoring Locations"
    )

    return map_fig

def line_figure():
    df_so2 = daily_stats_df[daily_stats_df["parameter"] == "so2"] \
                .sort_values(by="measurement_date")

    line_fig = px.line(
        df_so2,
        x="measurement_date",
        y="average_value",
        title="Plot Over Time of SO2 Levels"
    )
    return line_fig

def box_figure():
    df_so2 = daily_stats_df[daily_stats_df["parameter"] == "so2"] \
                .sort_values(by="weekday_number")

    box_fig = px.box(
        df_so2,
        x="weekday",
        y="average_value",
        title="Distribution of SO2 Levels by Weekday"
    )
    return box_fig



app = dash.Dash(__name__)


app.layout = html.Div([
      dcc.Tabs([
            dcc.Tab(
                  label="Sensor Locations",
                  children=[dcc.Graph(id="map-view", figure=map_figure())]
            ),
            dcc.Tab(
                  label="Parameter Plots",
                  children=[
                        # dcc.Dropdown(
                        #       id="location-dropdown",
                        #       clearable=False,
                        #       multi=False,

                        #       searchable=True
                        # ),
                        # dcc.Dropdown(
                        #       id="parameter-dropdown",
                        #       clearable=False,
                        #       multi=False,
                        #       searchable=True
                        # ),
                        # dcc.DatePickerRange(
                        #       id="date-picker-range",
                        #       display_format="YYYY-MM-DD"
                        # ),
                        dcc.Graph(id="line-plot",figure=line_figure()),
                        dcc.Graph(id="box-plot", figure=box_figure())
                  ]  
            )
      ])
])

if __name__ == "__main__":
    app.run(debug=True)


