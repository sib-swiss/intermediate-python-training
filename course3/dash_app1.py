from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import numpy as np

## reading data from the 1880 Swiss census
df = pd.read_csv('../course1/data/census1880_fractions.csv')

app = Dash()

app.layout = [
    html.H1(children='1880 swiss census', style={'textAlign':'center'}),
    dcc.Dropdown(df['canton name'].unique(), 'Basel-Stadt', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
]

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    
    dff = df.loc[ df['canton name']==value , : ]
    
    fig = px.histogram( np.log10( dff.Total ) ) # using numpy log10 here because plotly histogram and axis log scale does not work
    fig.update_xaxes(title_text = 'log10 number of inhabitants')
    
    return fig

if __name__ == '__main__':
    app.run(debug=True , host='127.0.0.1' , port = 8051)
