from dash import dcc, html
import pydeck as pdk
import pandas as pd
import numpy as np
import dash_deck
import json
from secrets import mapbox_key
with open('./data/weekday_rebalancing.json', 'r') as js: # shape file for neighborhood boundaries, needed for population density plot
    weekday_rebalanced_plot = json.loads(js.read())



TOOLTIP_TEXT = {"html": "{count} bikes moved from {end_station}<br />\
                # to {next_station}Home of commuter in red; work location in green"}


rebalancing_tab = dcc.Tab(label='Rebalancing',
                          value='rebalancing',
                          children = [
                          html.H1('Rebalancing'),
                          html.H4('Rebalancing is the process of moving bikes from location to location, making sure to meet demand of all your customers\nnewline'),
                          html.H3('Weekday Rebalancing'),
                          dash_deck.DeckGL(weekday_rebalanced_plot,
                                    style={"width": "50vw", "height": "50vh","position": 'relative'},
                                    id='deck-gl',
                                    tooltip=TOOLTIP_TEXT,
                                    mapboxKey=mapbox_key)])
