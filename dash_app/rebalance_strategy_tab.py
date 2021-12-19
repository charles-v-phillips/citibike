from dash import dcc, html
import pydeck as pdk
import dash_deck
import requests
from secrets import mapbox_key
import pandas as pd
from rebalancing_strategy_blurbs import logistics_blurb, ml_blurb, algorithm_blurb
from PIL import Image
legend = Image.open('./data/image/legend.png')

max_bikes_input = dcc.Input(id = 'max_bikes_input', placeholder = 'Input Max Bikes you can move',type = 'number',value = 500)
min_cargo_size = dcc.Input(id = 'min_cargo_size', placeholder = 'Min Cargo Size', type = 'number',value = 3)
max_distance = dcc.Input(id='max_distance', placeholder = 'Max Distance',type = 'number',value = 2)
low_availability_threshold = dcc.Input(id = 'low_availability_threshold', placeholder = 'Low Availability Threshold',type = 'number', value = .666)
high_availability_threshold = dcc.Input(id = 'high_availability_threshold', placeholder = 'High Availability Threshold',type = 'number',value = .333)


predictions = pd.read_csv('./../communal/dataframe_for_live_predictions.csv')

times = [{'label' : date, 'value' : date} for date in predictions['datetime'].unique()]

date_picker = dcc.Dropdown(id = 'date_input', options = times,value = times[0]['value'])
calculate_button = html.Button('Calculate', id='calculate_button', n_clicks=0)


# BLUE_RGB = [0, 59, 112, 90]
# RED_RGB = [217, 38, 28, 90]
# arc_layer = pdk.Layer(
#     "ArcLayer",
#     # data = weekday_grouped[:300],
#     # get_source_position=['end_lon','end_lat'],
#     # get_target_position = ['next_lon','next_lat'],
#     get_tilt=15,
#     get_source_color=RED_RGB,
#     get_target_color=BLUE_RGB,
#     pickable=True,
#     auto_highlight=True,
#     # get_width = 'count/700'
#     )
#
# view_state = pdk.ViewState(latitude = 40.778786,longitude = -73.974785, bearing=45, pitch=50, zoom=11,)
# # latitude = 40.778786,longitude = -73.974785
#
# TOOLTIP_TEXT = {"html": "{count} bikes moved from {end_station}<br />\
#                 to {next_station}Home of commuter in red; work location in green"}
# r = pdk.Deck(arc_layer, initial_view_state=view_state, tooltip=TOOLTIP_TEXT,map_style = 'light')

rebalance_strategy_tab =\
dcc.Tab(
    label = 'Rebalancing Forecasting Tool',
    value='rebalance_strategy',
    children = [
                    html.Div(children = [
                        html.Div(children = [html.H1('Logistic Strategy',style = {'text-align':'center'}),'dummy_text'],style = {'height': '30vh','width': '40vw','margin-right' : '4vw','display' : 'inline-block'}),
                        html.Div(children = [html.H1('Machine Learning Model',style = {'text-align':'center'}),'dummy_text'],style = {'height': '30vh','width': '40vw','display' : 'inline-block'})]
                    ),


                    html.Div(children = [html.H6('Date & Time'),date_picker],style = {'display' : 'inline-block','width' : '20vw'}),
                    html.Div(children = [
                                         html.Div(children = [html.H6('Max Bikes To Move'),max_bikes_input],style = {'display' : 'inline-block'}),
                                         html.Div(children = [html.H6('Min Cargo Size'),min_cargo_size],style = {'display' : 'inline-block'}),
                                         html.Div(children = [html.H6('Max Distance'),max_distance],style = {'display' : 'inline-block'}),
                                         html.Div(children = [html.H6('Low Avail. Threshold'),low_availability_threshold],style = {'display' : 'inline-block'}),
                                         html.Div(children = [html.H6('High Avail. Threshold'),high_availability_threshold],style = {'display' : 'inline-block'}),
                                         html.Div(children = [html.H6('Calculate'),calculate_button],style = {'display' : 'inline-block'})],
                              style = {'width': '100vw'}),

                    html.Div(children=[
                                        html.Div(children = [dash_deck.DeckGL(style = {'height' : '100%',"position": 'relative'},
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
                                style = {'height' : '45vh','margin-top':'2%'}),
                    html.Img(id = 'leg',
                            src = legend,
                            style = {'width':'auto', 'height': 100})
                ]
)
