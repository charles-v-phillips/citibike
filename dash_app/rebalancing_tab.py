from dash import dcc, html
import pydeck as pdk
import pandas as pd
import numpy as np
import dash_deck
import json
from secrets import mapbox_key
with open('./data/weekday_rebalancing.json', 'r') as js: # shape file for neighborhood boundaries, needed for population density plot
    weekday_rebalanced_plot = json.loads(js.read())

with open('./data/weekend_rebalancing.json', 'r') as js: # shape file for neighborhood boundaries, needed for population density plot
    weekend_rebalanced_plot = json.loads(js.read())



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
                                         style={'width': '30%', 'display': 'inline-block','vertical-align': 'top','margin-left': '9%'})],style = {'height' : '45vh','margin-top':'10px'})
                                   ]
                          )

                          # html.H3('Weekday Rebalancing'),
                          # dash_deck.DeckGL(weekday_rebalanced_plot,
                          #           style={"width": "50vw", "height": "50vh","position": 'relative'},
                          #           id='deck-gl',
                          #           tooltip=TOOLTIP_TEXT,
                          #           mapboxKey=mapbox_key)])
