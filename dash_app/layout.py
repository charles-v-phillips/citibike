from dash import html,dcc
import eda_tab as eda_tab
import about_us_tab as about_us_tab
import rebalancing_tab as rebalancing_tab

tabs = dcc.Tabs(id="tabs-example-graph", children=[eda_tab.eda_tab,rebalancing_tab.rebalancing_tab,about_us_tab.about_us_tab],value='eda')

layout = html.Div([
    html.H1('CitiBike'),
    tabs,
    html.Div(id='tabs-content-example-graph'),

])
