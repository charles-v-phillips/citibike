from dash import dcc, html
import pydeck as pdk
import dash_deck
import requests
from secrets import mapbox_key
import pandas as pd

max_bikes_input = dcc.Input(id = 'max_bikes_input', placeholder = 'Input Max Bikes you can move')

weather_response = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=40.7812&lon=-73.9665&exclude=minutely,current,daily,alerts&units=metric&appid=404310456b8e1c31228341dd6c95dd04')
weather = weather_response.json()
times  = [{'label' : str(pd.to_datetime(weather['hourly'][i]['dt'],unit = 's')),
           'value' : str(pd.to_datetime(weather['hourly'][i]['dt'],unit = 's'))} for i in range(len(weather['hourly']))]

date_picker = dcc.Dropdown(id = 'date_input', options = times,value = times[0]['value'])

BLUE_RGB = [0, 59, 112, 90]
RED_RGB = [217, 38, 28, 90]
arc_layer = pdk.Layer(
    "ArcLayer",
    # data = weekday_grouped[:300],
    # get_source_position=['end_lon','end_lat'],
    # get_target_position = ['next_lon','next_lat'],
    get_tilt=15,
    get_source_color=RED_RGB,
    get_target_color=BLUE_RGB,
    pickable=True,
    auto_highlight=True,
    # get_width = 'count/700'
    )

view_state = pdk.ViewState(latitude = 40.778786,longitude = -73.974785, bearing=45, pitch=50, zoom=11,)
# latitude = 40.778786,longitude = -73.974785

TOOLTIP_TEXT = {"html": "{count} bikes moved from {end_station}<br />\
                to {next_station}Home of commuter in red; work location in green"}
r = pdk.Deck(arc_layer, initial_view_state=view_state, tooltip=TOOLTIP_TEXT,map_style = 'light')

rebalance_strategy_tab =\
dcc.Tab(
    label = 'Rebalancing Stategy',
    value='rebalance_strategy',
    children = [
                    html.Div('eyo'),
                    max_bikes_input,
                    html.Div(date_picker,style = {'width' : '20%'}),
                    html.Div(children=[
                                        html.Div(children = [dash_deck.DeckGL(r.to_json(),style = {'height' : '100%',"position": 'relative'},
                                                                  id='rebalancing-strategy-graphic',
                                                                  mapboxKey=mapbox_key)],
                                                  style={'width': '60%',
                                                         'height' : '100%',
                                                         'display': 'inline-block'},
                                                  id = 'rebalancing_strategy_left_div'),

                                        html.Div(children =[
                                                    html.H2('Weekday Rebalancing'),
                                                    'stupid text'],
                                                 style={'width': '30%',
                                                        'display': 'inline-block',
                                                        'vertical-align': 'top',
                                                        'margin-left': '4%',
                                                        "maxHeight": "400px",
                                                        "overflow": "scroll"})
                                        ],
                                style = {'height' : '45vh','margin-top':'2%'})
                ]
)
