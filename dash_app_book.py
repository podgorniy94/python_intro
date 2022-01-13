# Základní Dash aplikace (19)
# Interaktivní aplikace (26)
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go

app = dash.Dash()

app.layout = html.Div([
    html.Label('Hello, what do you like to do in your free time?',
    style={
        'display': 'inline-block', 'vertical-align': 'middle',
        'textAlign': 'center', 'font-size': '1.6em', 'width':
        '40%'
        }
    ),
    dcc.Dropdown(
        id='example-dropdown',
        options=[
            {'label': 'Read books', 'value': 'read'},
            {'label': 'Bake cakes', 'value': 'bake'},
            ],
        value=''
        ),
    dcc.Graph(
        id='example-plot',
        figure={
            'data': [
                go.Bar(x=[1], y=[628], name='Paperback'),
                go.Bar(x=[1], y=[796], name='Hard book')
                ],
            'layout': {
                'title': 'Book weight in grams'
                }
            }
        ),
    dcc.Input(id='day', type="text", value='Day'),
    dcc.Input(id='time', type="text", value='Time'),
    html.Button(id='submit-button', n_clicks=0, children='Show weather forecast'),
    html.Div(id='show-weather')
])

@app.callback(Output('show-weather', 'children'),
        Input('submit-button', 'n_clicks'),
        State('day', 'value'), State('time', 'value'))

def update_output(n_clicks, day, time):
    return u'''The Button has been pressed {} times,
        Today is "{}",
        and entered time is "{}"
     '''.format(n_clicks, day, time)


if __name__ == '__main__':
        app.run_server(debug=True)
