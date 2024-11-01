from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import numpy as np

## reading data from the 1880 Swiss census
df = pd.read_csv('../course1/data/census1880_fractions.csv')

app = Dash()

app.layout = html.Div([
    html.H1(children='1880 swiss census', style={'textAlign':'center'}),
    
    html.Div([
        html.Div(children='''Pick a canton:'''),
        dcc.Dropdown(df['canton name'].unique(), 'Basel-Stadt', id='canton-selection'),
        dcc.RadioItems(['Log','Linear'], 'Log', inline=True, id='scale-selection')
    ]),
    
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('canton-selection', 'value'), ## the names are all value, the order is what matters
    Input('scale-selection', 'value')
)
def update_graph(canton, scale):
    
    print(canton,scale)
    
    dff = df.loc[ df['canton name']==canton , : ]
    
    data = dff.Total
    xlabel = 'number of inhabitants'
    if scale == "Log":
        data = np.log10( data )
        xlabel = 'log10 number of inhabitants'
    
    fig = px.histogram( data )
    fig.update_xaxes(title_text = xlabel)
    
    return fig

if __name__ == '__main__':
    app.run(debug=True , host='127.0.0.1')

