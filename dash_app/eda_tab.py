import dash
from dash import dcc, html
import pickle
import json
import plotly.express as px


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

                        dcc.Graph(id = 'transit_locations', figure = transit_locations)
])
