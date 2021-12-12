import dash 
from dash.dependencies import Input, Output
from dash import dcc
from dash import html

app = dash.Dash()

app.layout = html.Div(children = [
	dcc.Input(id = 'shit', value = 'enter something', type = 'text'),
	html.Div(id = 'output')
	])

@app.callback(
	Output(component_id = 'output', component_property = 'children'),
	[Input(component_id = 'shit', component_property = 'value')])
def update_value(input_data):
	try:
		return str(float(input_data)**2)
	except:
		return "are you dumb? is that a number?"

if __name__ == '__main__':
	app.run_server(debug = True)