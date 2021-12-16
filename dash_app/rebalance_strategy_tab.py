from dash import dcc, html

rebalance_intro = "FUCKKKK"

rebalance_strategy_tab = dcc.Tab(label = 'Rebalancing Stategy',
                    value='rebalance_strategy',
                    children = [
                    html.Div(rebalance_intro)])
