
#-------------------- PACKAGES -------------------------
import dash
from dash.dependencies import Input, Output, State

import pandas as pd
import plotly.express as px

import layout
from dash import dash_table
#-------------------- ALGO AREA -----------------------
from geopy.distance import distance
import pydeck as pdk
import dash_deck
from secrets import mapbox_key
predictions = pd.read_csv('./../communal/dataframe_for_live_predictions.csv')
new = pd.read_csv('./data/robert/new.csv')
day_of_week_conversion = {0:2, 1:3, 2:4, 3:5, 4:6, 5:7, 6:1}
def manhattan_distance(start_lat, start_lon, end_lat, end_lon):
    dist = distance((start_lat, start_lon), (start_lat, end_lon)).miles + \
           distance((end_lat, end_lon), (start_lat, end_lon)).miles
    return dist

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
                            zoom=11,
                            center=dict(lat=40.76421, lon=-73.95623)
                            )
    return [map]


@app.callback(
    Output(component_id='rebalancing_strategy_left_div',component_property = 'children'),
    Output(component_id = 'table', component_property = 'children'),
    State(component_id='date_input', component_property='value'),
    State(component_id = 'max_bikes_input',component_property='value'),
    State(component_id = 'min_cargo_size',component_property='value'),
    State(component_id = 'max_distance',component_property='value'),
    State(component_id = 'low_availability_threshold',component_property='value'),
    State(component_id = 'high_availability_threshold',component_property='value'),
    Input('calculate_button', 'n_clicks')




)
def render_map(date_input, max_bikes_input, min_cargo_size, max_distance, low_availability_threshold, high_availability_threshold, calculate_button):
    max_bikes_input = int(max_bikes_input)
    print(max_bikes_input)
    print(type(date_input),type(max_bikes_input),type(min_cargo_size),type(max_distance),type(low_availability_threshold),type(high_availability_threshold))
    date = pd.to_datetime(date_input)
    month = date.month
    num_day = day_of_week_conversion[date.dayofweek]
    hour = date.hour
    print(month,num_day,hour)

    query = predictions[(predictions['month'] == month) & (predictions['num_day'] == num_day) & (predictions['hour'] == hour)]

    low_bike_threshold = low_availability_threshold
    high_bike_threshold = high_availability_threshold
    max_distance = max_distance
    max_bikes_rebalanced = max_bikes_input
    min_cargo_size = min_cargo_size

    data_low = query[query['avail_bikes_proportion'] <= low_bike_threshold]
    data_high = query[query['avail_bikes_proportion'] >= high_bike_threshold]

    data_low['deficit'] = round((low_bike_threshold - data_low['avail_bikes_proportion']) * data_low['tot_docks']).astype('int')
    data_high['surplus'] = round((data_high['avail_bikes_proportion'] - high_bike_threshold) * data_high['tot_docks']).astype('int')

    data_low = data_low.sort_values(by = 'deficit', ascending = False)
    data_high = data_high.sort_values(by = 'surplus', ascending = False)

    rebalancing_dict = {}
    print('are we here?')
    low_copy = data_low.copy()
    high_copy = data_high.copy()
    bikes_rebalanced = 0
    for low in low_copy.index:
        if low_copy.loc[low, 'deficit'] == 0:
            continue
        for high in high_copy.index:
            if high_copy.loc[high, 'surplus'] == 0:
                continue
            if manhattan_distance(low_copy.loc[low, 'latitude'], low_copy.loc[low, 'longitude'],
                                  high_copy.loc[high, 'latitude'], high_copy.loc[high, 'longitude']) < max_distance:
                stations_key = (low_copy.loc[low, 'dock_id'], high_copy.loc[high, 'dock_id'])
                change = min(low_copy.loc[low, 'deficit'], high_copy.loc[high, 'surplus'])
                low_copy.loc[low, 'deficit'] -= change
                high_copy.loc[high, 'surplus'] -= change
                bikes_rebalanced += change
                if stations_key in rebalancing_dict.keys():
                    rebalancing_dict[stations_key] += change
                else:
                    rebalancing_dict[stations_key] = change
                if low_copy.loc[low, 'deficit'] == 0:
                    break
    print('are we here 2?')
    sorted_rebalancing = dict(sorted(rebalancing_dict.items(), key=lambda x: x[1], reverse = True))
    filtered_rebalancing = {key: value for key, value in sorted_rebalancing.items() if value >= min_cargo_size}
    filtered_bikes_rebalanced = 0
    final_rebalancing_dict = {}
    for k, v in filtered_rebalancing.items():
        if filtered_bikes_rebalanced < max_bikes_rebalanced:
            final_rebalancing_dict[k] = v
            filtered_bikes_rebalanced += v

    rebalancing_df = pd.DataFrame(final_rebalancing_dict.items(), columns = ['dock_ids', 'num_bikes'])
    rebalancing_df[['dock_id_receive', 'dock_id_give']] = rebalancing_df['dock_ids'].tolist()
    rebalancing_df.drop(['dock_ids'], axis = 1, inplace = True)
    data_df = query[['dock_id', 'latitude', 'longitude']]
    new_docks = new[['dock_id', 'dock_name']]
    rebalancing_df = rebalancing_df.merge(data_df, how = 'left', left_on = 'dock_id_receive', right_on = 'dock_id').rename(
    columns = {'latitude': 'latitude_receive', 'longitude': 'longitude_receive'})
    rebalancing_df = rebalancing_df.merge(data_df, how = 'left', left_on = 'dock_id_give', right_on = 'dock_id').rename(
    columns = {'latitude': 'latitude_give', 'longitude': 'longitude_give'})
    rebalancing_df.drop(['dock_id_x', 'dock_id_y'], axis = 1, inplace = True)

    rebalancing_df = rebalancing_df.merge(new_docks, how = 'left', left_on = 'dock_id_receive', right_on = 'dock_id').rename(
    columns = {'dock_name': 'dock_name_receive'})
    rebalancing_df = rebalancing_df.merge(new_docks, how = 'left', left_on = 'dock_id_give', right_on = 'dock_id').rename(
    columns = {'dock_name': 'dock_name_give'})
    rebalancing_df.drop(['dock_id_x', 'dock_id_y'], axis = 1, inplace = True)

    GREEN_RGB = [0, 255, 0, 150]
    RED_RGB = [240, 100, 0, 150]

    # Specify a deck.gl ArcLayer
    arc_layer = pdk.Layer(
        "ArcLayer",
        data = rebalancing_df,
        get_width="num_bikes",
        get_source_position=["longitude_give", "latitude_give"],
        get_target_position=["longitude_receive", "latitude_receive"],
        get_tilt=15,
        get_source_color=GREEN_RGB,
        get_target_color=RED_RGB,
        pickable=True,
        auto_highlight=True,
    )

    view_state = pdk.ViewState(latitude=40.74, longitude=-74, bearing=290, pitch=50, zoom=12)


    TOOLTIP_TEXT2 = {"html": "{num_bikes} bikes need rebalancing from<br />{dock_name_give} to {dock_name_receive}"}
    TOOLTIP_TEXT2 = {"html": "hello?"}

    r = pdk.Deck(arc_layer, initial_view_state=view_state, tooltip=TOOLTIP_TEXT2, map_style = 'light')

    rv = dash_deck.DeckGL(r.to_json(),style = {'height' : '100%',"position": 'relative'},
                              id='rebalancing-strategy-graphic',
                              mapboxKey=mapbox_key)

    table = rebalancing_df[['dock_name_give', 'dock_name_receive', 'num_bikes']]
    table = table.rename(columns = {'dock_name_give': 'dock origin', 'dock_name_receive': 'dock destination', 'num_bikes': 'number of bikes'})
    rv2 = dash_table.DataTable(
    id = 'whatever',
    columns = [{'name': i, 'id' : i} for i in table.columns],
    data = table.to_dict('records')
    )


    return [rv,rv2]

    #TODO: need to return a whole ass child here




#------------------------- RUN APP
if __name__ == '__main__':
    app.run_server(debug=True)
