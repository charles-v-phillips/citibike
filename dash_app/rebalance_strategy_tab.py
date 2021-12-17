from dash import dcc, html


rebalance_strategy_tab =\
dcc.Tab(
    label = 'Rebalancing Stategy',
    value='rebalance_strategy',
    children = [
                    html.Div('eyo'),
                    dcc.Input()
                ]
)
