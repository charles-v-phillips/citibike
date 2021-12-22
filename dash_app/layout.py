from dash import html,dcc
from tabs.eda_tab import eda_tab
from tabs.about_us_tab import about_us_tab
from tabs.rebalancing_tab import rebalancing_tab
from tabs.intro_tab import intro_tab
from tabs.rebalance_strategy_tab import rebalance_strategy_tab
from tabs.conclusion_tab import conclusion_tab
from tabs.cluster_tab import cluster_tab
from PIL import Image

citi_bike_logo = Image.open('./data/image/citi_bike_logo.png')

tabs = dcc.Tabs(id="tabs-example-graph", children=[intro_tab,
                                                    eda_tab,
                                                    cluster_tab,
                                                    rebalancing_tab,
                                                    rebalance_strategy_tab,
                                                    conclusion_tab,
                                                    about_us_tab
                                                    ],
                                                    value='intro')

layout = html.Div([
    html.Img(id='citi_bike_logo',src = citi_bike_logo,
                style = {"width": "40%",
                        "height": "auto"}),
    tabs,
    html.Div(id='tabs-content-example-graph'),

])
