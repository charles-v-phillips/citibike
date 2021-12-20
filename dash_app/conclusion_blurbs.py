from dash import dcc
conclusion_blurb = dcc.Markdown('''
1. Based on CitiBikes growth other bike share companies can incorporate their rollout strategy
2. There are clear weekday usage patterns driven by commuter usage, weekend patterns are less defined
3. The majority of rebalancing occurs during the morning and evening commuting hours with a majority of the bikes being moved less than 2 miles
4. Weekday rebalancing is most prevalent in Alphabet City and Midtown
5. Weekend rebalancing is most prevalent around Central Park
6. We created a ML model that predicts bike availability at specified time in the next 48 hours
7. We create a rebalancing algorithm that uses bike availability predictions and can be added on top of CitiBike’s current rebalancing strategy
''')

next_steps_blurb = dcc.Markdown('''
1. Do not have real time data
2. Dock availability data stopped being publicly available in 2019 and was only on hourly basis
3. Do not have CitiBike operational information on current rebalancing strategy and staffing capacity/budget for bike rebalancing
4. Difficult to train ML models on full dataset without Cloud Computing
''')
