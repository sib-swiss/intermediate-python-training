from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import numpy as np

## reading data from the 1880 Swiss census
df = pd.read_csv('../course1/data/census1880_fractions.csv')

## styling the dcc component with the dbc theme: 
##   https://hellodash.pythonanywhere.com/adding-themes/dcc-components
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
external_stylesheets = [dbc.themes.DARKLY,dbc_css] # try other theme, such as dbc.themes.QUARTZ
app = Dash( external_stylesheets=external_stylesheets )

# App layout
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(dbc.Alert("1880 swiss census", color ='primary'))),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='graph-content') , width = 9),
                dbc.Col(
                    dbc.Container([  
                        dbc.Row(
                            dbc.Col(dcc.Dropdown(df['canton name'].unique(), 
                                                 'Basel-Stadt', 
                                                 id='canton-selection',
                                                 className="dbc"))
                        ),
                        dbc.Row(
                            dbc.Col(dcc.RadioItems(['Log','Linear'], 
                                                   'Log', 
                                                   inline=False, 
                                                   id='scale-selection',
                                                   className="dbc"))
                        )
                    ]), width = 3 )
            ],
            align="center",
        ),
    ]
)


@callback(
    Output('graph-content', 'figure'),
    Input('canton-selection', 'value'), ## the names are all value, the order is what matters
    Input('scale-selection', 'value')
)
def update_graph(canton, scale):
    
    
    dff = df.loc[ df['canton name']==canton , : ]
    
    data = dff.Total
    xlabel = 'number of inhabitants'
    if scale == "Log":
        data = np.log10( data )
        xlabel = 'log10 number of inhabitants'
    
    fig = px.histogram( data , template = 'plotly_dark')
    fig.update_xaxes(title_text = xlabel)
    
    return fig

if __name__ == '__main__':
    app.run(debug=True , host='127.0.0.1')

