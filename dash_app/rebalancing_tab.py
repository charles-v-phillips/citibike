from dash import dcc, html
import pydeck as pdk
import pandas as pd
import numpy as np
import dash_deck
import json
from PIL import Image
import plotly.express as px
from secrets import mapbox_key
from rebalance_blurbs import cluster_weekday_blurb, cluster_weekend_blurb, rebalance_time_blurb, rebalance_dist_blurb, rebalance_3d_weekday_blurb, rebalance_3d_weekend_blurb

with open('./data/weekday_rebalancing.json', 'r') as js: # shape file for neighborhood boundaries, needed for population density plot
    weekday_rebalanced_plot = json.loads(js.read())

with open('./data/weekend_rebalancing.json', 'r') as js: # shape file for neighborhood boundaries, needed for population density plot
    weekend_rebalanced_plot = json.loads(js.read())

cluster0 = Image.open('./data/weekday_cluster_images/weekday_cluster_0.png')
cluster1 = Image.open('./data/weekday_cluster_images/weekday_cluster_1.png')
cluster2 = Image.open('./data/weekday_cluster_images/weekday_cluster_2.png')
cluster3 = Image.open('./data/weekday_cluster_images/weekday_cluster_3.png')
cluster4 = Image.open('./data/weekday_cluster_images/weekday_cluster_4.png')
cluster5 = Image.open('./data/weekday_cluster_images/weekday_cluster_5.png')
cluster6 = Image.open('./data/weekday_cluster_images/weekday_cluster_6.png')
frame_for_weekday_cluster_map = pd.read_csv('./data/frame_for_weekday_cluster_map.csv')
frame_for_weekday_cluster_map['cluster'] = frame_for_weekday_cluster_map['cluster'].astype(str)

weekday_cluster_map = px.scatter_mapbox(  frame_for_weekday_cluster_map,
                    lat = 'lat',
                    lon = 'lon',
                    color = 'cluster',
                    mapbox_style = 'carto-positron',
                    color_discrete_sequence=['rgba(204, 27, 14,1)','rgba(245,130,48,1)',
                                                'rgba(0,0,128,1)','rgba(128,0,0,1)',
                                            'rgba(60,180,75,1)','rgba(220,190,255,1)','rgba(128,128,128,1)' ],
                    category_orders = {'cluster':['1','2','3','4','5','6','7']},
                    zoom = 10,
                    center = dict(lat = 40.76421, lon = -73.95623),


                 )

weekday_cluster_map.update_layout(

                                  margin={"r":0,"t":0,"l":0,"b":0},
                                  legend=dict(
                                      yanchor="top",
                                      xanchor = 'left',
                                      y = 1.1,
                                      x = 0,
                                      orientation = 'h'
                              ))


weekend_cluster0 = Image.open('./data/weekend_cluster_images/weekend_cluster_0.png')
weekend_cluster1 = Image.open('./data/weekend_cluster_images/weekend_cluster_1.png')
weekend_cluster2 = Image.open('./data/weekend_cluster_images/weekend_cluster_2.png')
weekend_cluster3 = Image.open('./data/weekend_cluster_images/weekend_cluster_3.png')
weekend_cluster4 = Image.open('./data/weekend_cluster_images/weekend_cluster_4.png')
weekend_cluster5 = Image.open('./data/weekend_cluster_images/weekend_cluster_5.png')

rebalancing_times = Image.open('./data/robert/phantom_rides_time_of_day.png')
rebalancing_distances = Image.open('./data/robert/phantom_rides_distances.png')

TOOLTIP_TEXT = {"html": "{count} bikes moved from {end_station}<br />\
                # to {next_station}Home of commuter in red; work location in green"}


rebalancing_tab = dcc.Tab(label='Rebalancing',
                          value='rebalancing',
                          children = [
                          html.Div(children=[
                                html.Div(dash_deck.DeckGL(weekday_rebalanced_plot,
                                                          style = {'height' : '100%',"position": 'relative'},
                                                          id='deck-gl',
                                                          tooltip=TOOLTIP_TEXT,
                                                          mapboxKey=mapbox_key),
                                         style={'width': '60%','height' : '100%', 'display': 'inline-block'}),

                                html.Div(children = [html.H2('Weekday Rebalancing'), rebalance_3d_weekday_blurb],
                                         style={'width': '30%', 'display': 'inline-block','vertical-align': 'top','margin-left': '9%'})],style = {'height' : '45vh'}),
                          html.Div(children=[
                                html.Div(dash_deck.DeckGL(weekend_rebalanced_plot,
                                                          style = {'height' : '100%',"position": 'relative'},
                                                          id='deck-gl2',
                                                          tooltip=TOOLTIP_TEXT,
                                                          mapboxKey=mapbox_key),
                                         style={'width': '60%','height' : '100%', 'display': 'inline-block'}),

                                html.Div(children = [html.H2('Weekend Rebalancing'), rebalance_3d_weekend_blurb],
                                         style={'width': '30%', 'display': 'inline-block','vertical-align': 'top','margin-left': '9%'})],style = {'height' : '45vh','margin-top':'10px'}),
                          html.H1('Weekday Cluster Stations',style = {'margin-top': '10px'}),
                          html.Div(children = [ html.Div(children = [html.Img(id = 'c1',src = cluster0,style = {"height": "30vh","width": "auto"}),
                                                                     html.Img(id = 'c2',src = cluster1,style = {"height": "30vh","width": "auto"}),
                                                                     html.Img(id = 'c3',src = cluster2,style = {"height": "30vh", "width": "auto"}),
                                                                     html.Img(id = 'c4',src = cluster3,style = {"height": "30vh", "width": "auto"}),
                                                                     html.Img(id = 'c5',src = cluster4,style = {"height": "30vh", "width": "auto"}),
                                                                     html.Img(id = 'c6',src = cluster5,style = {"height": "30vh", "width": "auto"}),
                                                                     html.Img(id = 'c7',src = cluster6,style = {"height": "30vh", "width": "auto"})],
                                                                style={'width': '55%','height' : '100%', 'display': 'inline-block'}),
                                                html.Div(children = [
                                                        html.H1('Weekday Clusters'), cluster_weekday_blurb,dcc.Graph(id = 'weekday-cluster-graph',
                                                                                                                    figure = weekday_cluster_map)],
                                                         style={'width': '43%','margin-left' : '2%','height' : '100%', 'display': 'inline-block','vertical-align': 'top'})



                                                ]),
                          html.H1('Weekend Cluster Stations',style = {'margin-top': '10px'}),
                          html.Div(children = [ html.Div(children = [html.Img(id = 'wkndc1',src = weekend_cluster0,style = {"height": "34vh","width": "auto"}),
                                                                     html.Img(id = 'wkndc2',src = weekend_cluster1,style = {"height": "34vh","width": "auto"}),
                                                                     html.Img(id = 'wkndc3',src = weekend_cluster2,style = {"height": "34vh", "width": "auto"}),
                                                                     html.Img(id = 'wkndc4',src = weekend_cluster3,style = {"height": "34vh", "width": "auto"}),
                                                                     html.Img(id = 'wkndc5',src = weekend_cluster4,style = {"height": "34vh", "width": "auto"}),
                                                                     html.Img(id = 'wkndc6',src = weekend_cluster5,style = {"height": "34vh", "width": "auto"})],
                                                                style={'width': '70%','height' : '100%', 'display': 'inline-block'}),
                                                html.Div(children = [
                                                        html.H1('Weekend Clusters'), cluster_weekend_blurb],
                                                         style={'width': '25%','margin-left' : '2%','height' : '100%', 'display': 'inline-block','vertical-align': 'top'})



                                                ]),
               html.Div(children = [ html.Div(children = [html.Img(id = 'rebalancing_times', src = rebalancing_times, style = {"height": "68vh","width": "auto"})],
                                                                style={'width': '70%','height' : '100%', 'display': 'inline-block'}),
                                                html.Div(children = [
                                                        html.H1('Distribution of Rebalanced Trip Times'), rebalance_time_blurb],
                                                         style={'width': '25%','margin-left' : '2%','height' : '100%', 'display': 'inline-block','vertical-align': 'top'})



                                                ]),
               html.Div(children = [ html.Div(children = [html.Img(id = 'rebalancing_distances', src = rebalancing_distances, style = {"height": "68vh","width": "auto"})],
                                                                style={'width': '70%','height' : '100%', 'display': 'inline-block'}),
                                                html.Div(children = [
                                                        html.H1('Distribution of Rebalance Trip Distance'), rebalance_dist_blurb],
                                                         style={'width': '25%','margin-left' : '2%','height' : '100%', 'display': 'inline-block','vertical-align': 'top'})



                                                ])

             ])
