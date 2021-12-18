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

date_picker = dcc.Dropdown(id = 'date_input', options = times)


rebalance_strategy_tab =\
dcc.Tab(
    label = 'Rebalancing Stategy',
    value='rebalance_strategy',
    children = [
                    html.Div('eyo'),
                    max_bikes_input,
                    date_picker,
                    html.Div(children=[
                                        html.Div(dash_deck.DeckGL(style = {'height' : '100%',"position": 'relative'},
                                                                  id='rebalancing-strategy-graphic',
                                                                  mapboxKey=mapbox_key),
                                                  style={'width': '60%',
                                                         'height' : '100%',
                                                         'display': 'inline-block'}),

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
