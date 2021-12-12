import dash
from dash import dcc, html
import pickle
import json
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


pop_data = pickle.load(open('./data/pop_data.pkl', 'rb')) # population density data frame

with open('./data/N_Areas.geojson', 'r') as j: # shape file for neighborhood boundaries, needed for population density plot
    boundaries = json.loads(j.read())

dock_train_bus_df = pickle.load(open('./data/dock_train_bus_df.pkl', 'rb')) # dataframe with dock locations, bus stop location, and subway station locations

pop_density =px.choropleth_mapbox(pop_data,
                          geojson=boundaries,
                          locations = 'Neighborhood Tabulation Area Code (NTA Code)',
                           featureidkey="properties.ntacode",
                          color = 'Population Density (per Sq. Mi.)',
                           center={"lat": 40.77, "lon": -73.79},
                          mapbox_style="carto-positron")
transit_locations = px.scatter_mapbox(dock_train_bus_df,
                lat = 'latitude',
                lon = 'longitude',
                 color = 'type',
                 mapbox_style = 'carto-positron',
                  #color_continuous_scale=['pink','red','orange', 'yellow' 'green', 'blue','purple' ,'grey','black'],
                  zoom = 10,
                  center = dict(lat = 40.76421, lon = -73.95623)
                 )

usage_patterns = pd.read_csv('data/usage_patterns.csv')
usage_trend_plot = go.Figure(go.Heatmap(
                z = usage_patterns['num_rides'],
                x = usage_patterns['hour_of_day'],
                y = usage_patterns['day_of_week'],
                colorscale=[[0, 'white'], [1, 'blue']]))
usage_trend_plot.update_layout(
    yaxis = dict(
        tickmode = 'array',
        tickvals = [1, 2, 3, 4, 5, 6,7],
        ticktext = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday']
    ),
    xaxis = dict(
        tickmode = 'array',
        tickvals = list(range(24)),
        ticktext = ['12 AM','','','','4 AM','','','','8 AM','','','','12 PM','','','','4 PM','','','','8 PM','','','11 PM']
        ),
    font = dict(size = 16),
    title = dict(text='WILL THINK OF SOMETHING')

)

eda_tab = dcc.Tab(label='EDA',
                  value='eda',
                  children = [
                    dcc.Slider(
                            id='slider',
                            marks={i: '{}'.format(i) for i in range(1, 10)},
                            min=1,
                            max=9,
                            value=1,
                        ),
                        dcc.Graph(id='rollout_map'),

                        dcc.Graph(id='pop_density' ,figure=pop_density),

                        dcc.Graph(id = 'transit_locations', figure = transit_locations),

                        dcc.Graph(id='usage_pattern',figure=usage_trend_plot)
])
