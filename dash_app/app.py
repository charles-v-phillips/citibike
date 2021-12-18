
#-------------------- PACKAGES -------------------------
import dash
from dash.dependencies import Input, Output, State

import pandas as pd
import plotly.express as px

import layout

#-------------------- DATA ------------------------------


rollout_data = pd.read_csv('./data/rollout_clusters2.csv')
rollout_data['rollout_cluster'] = rollout_data['rollout_cluster'].astype(str)


#-------------------- LAYOUT ------------------------------
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

app.layout = layout.layout


# ------------------- CALLBACKS ------------------------------

@app.callback(
    [
        Output(component_id='rollout_map',component_property='figure'),
        Input(component_id='slider',component_property='value')
    ]
)
def update_plot(rollout):
    copy = rollout_data.copy()
    copy = copy[copy['rollout_cluster'].isin([str(i) for i in range(2013,rollout+1)])]

    map = px.scatter_mapbox(copy,
                            lat='latitude',
                            lon='longitude',
                            color='rollout_cluster',
                            mapbox_style='carto-positron',
                            # color_continuous_scale=['pink', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'grey',
                                                    # 'black','white'],

                            zoom=11,
                            center=dict(lat=40.76421, lon=-73.95623)
                            )

    # map.update_layout(height=800)

    return [map]


@app.callback(
    Output(component_id='rebalancing_strategy_left_div',component_property = 'children'),
    State(component_id='date_input', component_property='value'),
    State(component_id = 'max_bikes_input',component_property='value'),
    State(component_id = 'min_cargo_size',component_property='value'),
    State(component_id = 'max_distance',component_property='value'),
    State(component_id = 'low_availability_threshold',component_property='value'),
    State(component_id = 'high_availability_threshold',component_property='value'),
    Input('calculate_button', 'n_clicks')




)
def render_map(date_input,
            max_bikes_input,
            min_cargo_size,
            max_distance,
            low_availability_threshold,
            high_availability_threshold,
            calculate_button):
    print(date_input,max_bikes_input,min_cargo_size,max_distance,low_availability_threshold,high_availability_threshold)
    return [None]
    #TODO: need to return a whole ass child here




#------------------------- RUN APP
if __name__ == '__main__':
    app.run_server(debug=True)
