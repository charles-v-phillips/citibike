from dash import dcc, html
import pydeck as pdk
import dash_deck
from secret import mapbox_key
import pandas as pd
from blurbs.rebalancing_strategy_blurbs import logistics_blurb, ml_blurb, algorithm_blurb
from PIL import Image
legend = Image.open('./data/image/legend.png')
from dash import dash_table

max_bikes_input = dcc.Input(id = 'max_bikes_input', placeholder = 'Input Max Bikes you can move',type = 'number',value = 200)
min_cargo_size = dcc.Input(id = 'min_cargo_size', placeholder = 'Min Cargo Size', type = 'number',value = 3)
max_distance = dcc.Input(id='max_distance', placeholder = 'Max Distance',type = 'number',value = 2)
low_availability_threshold = dcc.Input(id = 'low_availability_threshold', placeholder = 'Low Availability Threshold',type = 'number', value = .333)
high_availability_threshold = dcc.Input(id = 'high_availability_threshold', placeholder = 'High Availability Threshold',type = 'number',value = .666)


predictions = pd.read_csv('./data/robert/dataframe_for_live_predictions.csv')

times = [{'label' : date, 'value' : date} for date in predictions['datetime'].unique()]

date_picker = dcc.Dropdown(id = 'date_input', options = times,value = times[0]['value'])
calculate_button = html.Button('Calculate', id='calculate_button', n_clicks=0)


rebalance_strategy_tab =\
dcc.Tab(
    label = 'Rebalancing Forecasting Tool',
    value='rebalance_strategy',
    children = [
                    html.Div(children = [
                        html.Div(children = [html.H1('Logistics Strategy',style = {'text-align':'center'}),html.Div(logistics_blurb,style = {'font-size':'1vw'})],style = {'height': '20vh','width': '46vw','margin-right' : '4vw','display' : 'inline-block','vertical-align': 'top'}),
                        html.Div(children = [html.H1('Machine Learning Model',style = {'text-align':'center'}),html.Div(ml_blurb,style = {'font-size':'1vw'})],style = {'height': '20vh','width': '46vw','display' : 'inline-block'})]
                    ),

                    html.H3(),
                    html.Div(children = [html.H6('Date & Time'),date_picker],style = {'display' : 'inline-block','width' : '20vw'}),
                    html.Div(children = [
                                         html.Div(children = [html.H6('Max Bikes To Move'),max_bikes_input],style = {'display' : 'inline-block'}),
                                         html.Div(children = [html.H6('Min Cargo Size'),min_cargo_size],style = {'display' : 'inline-block'}),
                                         html.Div(children = [html.H6('Max Distance (miles)'),max_distance],style = {'display' : 'inline-block'}),
                                         html.Div(children = [html.H6('Low Avail. Threshold'),low_availability_threshold],style = {'display' : 'inline-block'}),
                                         html.Div(children = [html.H6('High Avail. Threshold'),high_availability_threshold],style = {'display' : 'inline-block'}),
                                         html.Div(children = [html.H6(),calculate_button],style = {'display' : 'inline-block'})],
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
                                                    html.H2('Rebalancing Algorithm'),
                                                    html.Div(algorithm_blurb,style = {'font-size':'1vw'})],
                                                 style={'width': '30%',
                                                        'display': 'inline-block',
                                                        'vertical-align': 'top',
                                                        'margin-left': '4%',
                                                        "overflow": "scroll"})
                                        ],
                                style = {'height' : '45vh','margin-top':'2%'}),
                    html.Img(id = 'leg',
                            src = legend,
                            style = {'width':'auto', 'height': 100}),
                    html.Div(children = dash_table.DataTable(id = 'whatever'), id = 'table')

                ]
)
