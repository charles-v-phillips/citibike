import pandas as pd
import numpy as np
from dash import dcc, html
import pydeck as pdk
import dash_deck
import plotly.express as px
import json
from PIL import Image
from secret import mapbox_key
from blurbs.rebalance_blurbs import cluster_weekday_blurb,cluster_weekend_blurb,rebalance_time_blurb,rebalance_dist_blurb,rebalance_3d_weekday_blurb,rebalance_3d_weekend_blurb

# JSON File for 3D Interactive Rebalancing Plot (Weekday)
with open('./data/weekday_rebalancing.json', 'r') as js:
    weekday_rebalanced_plot = json.loads(js.read())

# JSON File for 3D Interactive Rebalancing Plot (Weekend)
with open('./data/weekend_rebalancing.json', 'r') as js:
    weekend_rebalanced_plot = json.loads(js.read())

legend = Image.open('./data/image/legend.png')

frame_for_weekday_cluster_map = pd.read_parquet('./data/frame_for_weekday_cluster_map.parquet')

weekday_cluster_map = px.scatter_mapbox(frame_for_weekday_cluster_map,
                                        lat = 'lat',
                                        lon = 'lon',
                                        color = 'cluster',
                                        mapbox_style = 'carto-positron',
                                        color_discrete_sequence=['rgba(204, 27, 14,1)','rgba(245,130,48,1)',
                                                                 'rgba(0,0,128,1)','rgba(128,0,0,1)',
                                                                 'rgba(60,180,75,1)','rgba(220,190,255,1)','rgba(128,128,128,1)' ],
                                        category_orders = {'cluster':['1','2','3','4','5','6','7']},
                                        zoom = 10,
                                        center = dict(lat = 40.76421, lon = -73.95623)
                 )
weekday_cluster_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0},
                                  legend=dict(
                                      yanchor="top",
                                      xanchor = 'left',
                                      y = 1.1,
                                      x = 0,
                                      orientation = 'h'
                              )
                              )

frame_for_weekend_cluster_map = pd.read_parquet('./data/frame_for_weekend_cluster_map.parquet')


weekend_cluster_map = px.scatter_mapbox(frame_for_weekend_cluster_map,
                                        lat = 'lat',
                                        lon = 'lon',
                                        color = 'cluster',
                                        mapbox_style = 'carto-positron',
                                        color_discrete_sequence=['rgba(204, 27, 14,1)',
                                                                 'rgba(245,130,48,1)',
                                                                 'rgba(0,0,128,1)',
                                                                 'rgba(32,64,64,1)',
                                                                 'rgba(30,128,150,1)',
                                                                 'rgba(145,50,180,1)'],
                                        category_orders = {'cluster':['1','2','3','4','5','6']},
                                        zoom = 10,
                                        center = dict(lat = 40.76421, lon = -73.95623),
                                        )

weekend_cluster_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0},
                                  legend=dict(yanchor="top",
                                              xanchor = 'left',
                                              y = 1.1,
                                              x = .45,
                                              orientation = 'h')
                                  )


rebalancing_times = Image.open('./data/robert/phantom_rides_time_of_day.png')
rebalancing_distances = Image.open('./data/robert/phantom_rides_distances.png')

TOOLTIP_TEXT = {"html": "{count} bikes moved from {end_station}<br />\
                 to {next_station}"}


rebalancing_tab =\
dcc.Tab(label='Current Rebalancing',
        value='rebalancing',
        children = [
            #Weekday Rebalancing Div
            html.Div(children=[
                                html.Div(dash_deck.DeckGL(weekday_rebalanced_plot,
                                                          style = {'height' : '100%',"position": 'relative'},
                                                          id='deck-gl',
                                                          tooltip=TOOLTIP_TEXT,
                                                          mapboxKey=mapbox_key),
                                          style={'width': '60%',
                                                 'height' : '100%',
                                                 'display': 'inline-block'}),

                                html.Div(children =[
                                            html.H2('Weekday Rebalancing'),
                                            html.Div(rebalance_3d_weekday_blurb,style = {'font-size':'1vw'})],
                                         style={'width': '30%',
                                                'display': 'inline-block',
                                                'vertical-align': 'top',
                                                'margin-left': '4%',
                                                # "maxHeight": "400px",
                                                "overflow": "scroll"})
                                ],
                        style = {'height' : '45vh','margin-top':'2%'}),


            html.Div('*For each arc, the bike starts at the green side and move to the red side'),
            html.Div('**Arc thickness is proportional to quantities of bikes moved'),
            #Weekend Rebalancing Div
            html.Div(children=[
                                html.Div(dash_deck.DeckGL(weekend_rebalanced_plot,
                                                          style = {'height' : '100%',"position": 'relative'},
                                                          id='deck-gl2',
                                                          tooltip=TOOLTIP_TEXT,
                                                          mapboxKey=mapbox_key),
                                         style={'width': '60%',
                                                'height' : '100%',
                                                'display': 'inline-block'}),

                                html.Div(children = [
                                                html.H2('Weekend Rebalancing'),
                                                html.Div(rebalance_3d_weekend_blurb,style = {'font-size':'1vw'})],
                                         style={'width': '30%',
                                                'display': 'inline-block',
                                                'vertical-align': 'top',
                                                'margin-left': '4%'})],
                     style = {'height' : '45vh','margin-top':'2%'}),


            html.Div('*For each arc, the bike starts at the green side and move to the red side'),
            html.Div('**Arc thickness is proportional to quantities of bikes moved'),
            
            #    #Rebalancing Times Div
               html.Div(children=[
                                  html.Div(children =[
                                                      html.Img(id = 'rebalancing_times',
                                                               src = rebalancing_times,
                                                               style = {"height": "68vh",
                                                                        "width": "auto"})],
                                            style={'width': '55%',
                                                   'height' : '100%',
                                                   'display': 'inline-block'}),
                                 html.Div(children = [
                                                      html.H1('Distribution of Rebalanced Trip Times'),
                                                      html.Div(rebalance_time_blurb,style = {'font-size':'1vw'})],
                                          style={'width': '43%',
                                                 'margin-left' : '2%',
                                                 'height' : '100%',
                                                 'display': 'inline-block',
                                                 'vertical-align': 'top'})
                ]),
            #
            #
            #
            #    # Rebalancing Distances Tab
               html.Div(children=[
                                  html.Div(children=[
                                                     html.Img(id = 'rebalancing_distances',
                                                     src = rebalancing_distances,
                                                    style = {"height": "68vh",
                                                             "width": "auto"})],
                                            style={'width': '55%',
                                                   'height' : '100%',
                                                   'display': 'inline-block'}),
                                  html.Div(children=[
                                                    html.H1('Distribution of Rebalance Trip Distance'),
                                                    html.Div(rebalance_dist_blurb,style = {'font-size':'1vw'})],
                                            style={'width': '43%',
                                                   'margin-left' : '2%',
                                                   'height' : '100%',
                                                   'display': 'inline-block',
                                                   'vertical-align': 'top'})
                ])

])
