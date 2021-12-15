from dash import dcc, html
import pydeck as pdk
import pandas as pd
import numpy as np
import dash_deck
import json
from PIL import Image
from secrets import mapbox_key
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

weekend_cluster0 = Image.open('./data/weekend_cluster_images/weekend_cluster_0.png')
weekend_cluster1 = Image.open('./data/weekend_cluster_images/weekend_cluster_1.png')
weekend_cluster2 = Image.open('./data/weekend_cluster_images/weekend_cluster_2.png')
weekend_cluster3 = Image.open('./data/weekend_cluster_images/weekend_cluster_3.png')
weekend_cluster4 = Image.open('./data/weekend_cluster_images/weekend_cluster_4.png')
weekend_cluster5 = Image.open('./data/weekend_cluster_images/weekend_cluster_5.png')



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

                                html.Div(children = [html.H2('Weekday Rebalancing'),'text'],
                                         style={'width': '30%', 'display': 'inline-block','vertical-align': 'top','margin-left': '9%'})],style = {'height' : '45vh'}),
                          html.Div(children=[
                                html.Div(dash_deck.DeckGL(weekend_rebalanced_plot,
                                                          style = {'height' : '100%',"position": 'relative'},
                                                          id='deck-gl2',
                                                          tooltip=TOOLTIP_TEXT,
                                                          mapboxKey=mapbox_key),
                                         style={'width': '60%','height' : '100%', 'display': 'inline-block'}),

                                html.Div(children = [html.H2('Weekend Rebalancing'),'text'],
                                         style={'width': '30%', 'display': 'inline-block','vertical-align': 'top','margin-left': '9%'})],style = {'height' : '45vh','margin-top':'10px'}),
                          html.H1('Weekday Cluster Stations',style = {'margin-top': '10px'}),
                          html.Div(children = [ html.Div(children = [html.Img(id = 'c1',src = cluster0,style = {"height": "34vh","width": "auto"}),
                                                                     html.Img(id = 'c2',src = cluster1,style = {"height": "34vh","width": "auto"}),
                                                                     html.Img(id = 'c3',src = cluster2,style = {"height": "34vh", "width": "auto"}),
                                                                     html.Img(id = 'c4',src = cluster3,style = {"height": "34vh", "width": "auto"}),
                                                                     html.Img(id = 'c5',src = cluster4,style = {"height": "34vh", "width": "auto"}),
                                                                     html.Img(id = 'c6',src = cluster5,style = {"height": "34vh", "width": "auto"}),
                                                                     html.Img(id = 'c7',src = cluster6,style = {"height": "34vh", "width": "auto"})],
                                                                style={'width': '70%','height' : '100%', 'display': 'inline-block'}),
                                                html.Div(children = [
                                                        html.H1('Weekday Clusters'), 'somemore dummy text'],
                                                         style={'width': '25%','margin-left' : '2%','height' : '100%', 'display': 'inline-block','vertical-align': 'top'})



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
                                                        html.H1('DUMMY HEader'), 'dumdfjgvhdniughmy_text'],
                                                         style={'width': '25%','margin-left' : '2%','height' : '100%', 'display': 'inline-block','vertical-align': 'top'})



                                                ])

                            ])
