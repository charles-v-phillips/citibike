from dash import dcc, html
import requests

weather_dict =  request = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=40.7812&lon=-73.9665&exclude=minutely,current,daily,alerts&units=metric&appid=404310456b8e1c31228341dd6c95dd04')

rebalance_strategy_tab =\
dcc.Tab(
    label = 'Rebalancing Stategy',
    value='rebalance_strategy',
    children = [
                    html.Div('eyo'),
                    dcc.Input()
                ]
)
