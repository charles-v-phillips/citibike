import dash
from dash import dcc, html
import pickle
import json
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

## START POPULATION DENSITY GRAPHIC --------------------------
pop_data = pickle.load(open('./data/pop_data.pkl', 'rb')) # population density data frame

with open('./data/N_Areas.geojson', 'r') as j: # shape file for neighborhood boundaries, needed for population density plot
    boundaries = json.loads(j.read())

pop_density =px.choropleth_mapbox(pop_data,
                          geojson=boundaries,
                          locations = 'Neighborhood Tabulation Area Code (NTA Code)',
                           featureidkey="properties.ntacode",
                          color = 'Population Density (per Sq. Mi.)',
                           center={"lat": 40.77, "lon": -73.79},
                          mapbox_style="carto-positron")
pop_density.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
pop_density.layout.coloraxis.colorbar.title = ''
# pop_density.update_traces(legendgrouptitle = dict(text = 'work?'))

## END POPULATION DENSITY GRAPHIC CHUNK ---------------------------

## START PUBLIC TRANSIT LOCATION GRAPHIC ---------------------------
dock_train_bus_df = pickle.load(open('./data/dock_train_bus_df.pkl', 'rb')) # dataframe with dock locations, bus stop location, and subway station locations
transit_locations = px.scatter_mapbox(dock_train_bus_df,
                lat = 'latitude',
                lon = 'longitude',
                 color = 'type',
                 mapbox_style = 'carto-positron',
                  #color_continuous_scale=['pink','red','orange', 'yellow' 'green', 'blue','purple' ,'grey','black'],
                  zoom = 10,
                  center = dict(lat = 40.76421, lon = -73.95623)
                 )

## END PUBLIC TRANSIT LOCATION GRAPHIC -----------------------------------

## START ROLLOUT CLUSTER GRAPHIC ----------------------------------

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
    title = dict(text='Average Number of Rides by Time and Day of Week')

)

## END ROLLOUT CLUSTER GRAPHIC --------------------------------

## START RIDES BY MONTH AND RIDES BY YEAR GRAPHIC ---------------------------

ride_time_data = pickle.load(open('./data/ridesbytime.pkl', 'rb'))

rides_per_year = px.line(pd.DataFrame(ride_time_data.groupby('year')['ridecount'].agg('sum')).reset_index(),
              x='year',
              y='ridecount',
              title="Annual Total Rides",
              labels = dict(total_rides="Total Number of Rides", year="Year"),
              markers=True)
rides_per_year.layout.plot_bgcolor = 'white'
rides_per_year.update_yaxes(nticks=15, ticks = 'outside', showgrid = True)
rides_per_year.update_xaxes(nticks = 10, tickangle=0, ticks = 'outside', showgrid = True)

rides_per_month = px.line(ride_time_data,
              x='ym',
              y='ridecount',
              title="Monthly Total Rides",
              labels = dict(total_rides="Total Number of Rides", ym="Year-Month"),
              markers=True)
rides_per_month.layout.plot_bgcolor = 'white'
rides_per_month.update_traces(marker={'size': 12,
                          'color': 'blue'})
rides_per_month.update_yaxes(nticks=15, ticks = 'outside', showgrid = False)
rides_per_month.update_xaxes(nticks = 15, tickangle=45, ticks = 'outside', showgrid = False)

## END RIDES BY MONTH AND YEAR GRAPHIC --------------------------------------

## START NUMBER OF RIDES BY MINUTE

rides_by_minute_data = pickle.load(open('./data/countofridesbyminutes.pkl', 'rb'))

rides_by_minute = px.bar(rides_by_minute_data,
             x="durationinmin",
             y="count",
             title="Trip Duration Count",
             labels = dict(count="Total Number of Rides", durationinmin="Minutes"))
rides_by_minute.update_traces(marker_color='blue')
for data in rides_by_minute.data:
   data["width"] = 1.0
rides_by_minute.layout.plot_bgcolor = 'white'
rides_by_minute.update_yaxes(nticks = 16, ticks = 'outside', showgrid = False)
rides_by_minute.update_xaxes(nticks = 14, ticks = 'outside')


## END NUMBER OF RIDES BY MINUTE

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
                        html.Div([
   html.Div(dcc.Graph(id='pop_density' ,figure=pop_density,style = {'height' : '100%'}), style={'width': '60%','height' : '100%', 'display': 'inline-block'}),
   html.Div(children = [html.H2('Population Density in NYC'),'text'], style={'width': '30%', 'display': 'inline-block','vertical-align': 'top','margin-left': '9%'})

],style = {'height' : '80vh'}),






                        # dcc.Graph(id='pop_density' ,figure=pop_density),



                        dcc.Graph(id = 'transit_locations', figure = transit_locations),

                        dcc.Graph(id='usage_pattern',figure=usage_trend_plot),

                        dcc.Graph(id='rides_per_year',figure=rides_per_year),

                        dcc.Graph(id='rides_per_month',figure=rides_per_month),

                        dcc.Graph(id='num_of_rides_by_minute', figure = rides_by_minute)
])
