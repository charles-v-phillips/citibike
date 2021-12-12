from dash import dcc, html

eda_tab = dcc.Tab(label='EDA',
                  value='eda',
                  children = [
                    dcc.Slider(
                            id='slider',
                            marks={i: '{}'.format(i) for i in range(1, 10)},
                            min=1,
                            max=9,
                            value=1,
                        ),
                        dcc.Graph(id='rollout_map')
])

