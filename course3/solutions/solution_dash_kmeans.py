
## first some code to assign colors to cluster arrangments
import matplotlib.colors as mcolors

colors = list( mcolors.TABLEAU_COLORS.values() )
color_dict = {}
for i,lbl in enumerate(set(labels.astype(str))):
    color_dict[ lbl ] = colors[i]
color_list = [ color_dict[l] for l in labels.astype(str) ]


def give_colors(lbls):
    colors = list( mcolors.TABLEAU_COLORS.values() )

    color_dict = {}
    for i,lbl in enumerate(set(lbls)):
        color_dict[ lbl ] = colors[i]
    
    return [ color_dict[l] for l in lbls ]
    
## reading data
import pandas as pd

df_pca = pd.read_csv( "data/digits.PCA20.csv" ,  index_col=0 )
df_umap = pd.read_csv( "data/digits.UMAP.csv" ,  index_col=0 )


## we cluster on the top 20 PCA axes
data = df_pca.loc[ : , [f"PC{i}" for i in range(20)] ].to_numpy()
# helper functions 

from kmeans import Kmeans

import plotly.graph_objects as go
import numpy as np



def make_figure( df , cluster_assigment = None ):


    fig = go.Figure()

    fig.add_trace(
        go.Scatter( x = df.iloc[:,0] ,  ## first column - works for PCA or UMAP
                   y = df.iloc[:,1] , ## second column - works for PCA or UMAP
                   mode='text', 
                   opacity = 0.5,
                   textfont_color=  give_colors( cluster_assigment )  , 
                   text = df.labels.astype(str) ,
                   customdata = np.array( [ df.labels , cluster_assigment ] ).transpose(),  
                   hovertemplate = "<b>label: %{customdata[0]}</b><br>"+
                                   "<b>cluster: %{customdata[1]}</b><br>" 
                  )
    )
    
    return fig
from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc


# setup some default
CURRENT_K = 1 ## remember the current K.
CLUSTER_ASSIGNMENT = Kmeans(data , k = CURRENT_K)



external_stylesheets = [dbc.themes.CERULEAN]
app = Dash("digits Kmeans", external_stylesheets=external_stylesheets)


row = html.Div([
    html.H1(children='digits dataset - Kmeans', style={'textAlign':'center'}),
    
    html.Div([
        html.Div(children='''Pick K:'''),
        dcc.Dropdown(list(range(1,11)), 1, id='K-selection'),
        dcc.RadioItems(['UMAP','PCA'], 'UMAP', inline=True, id='DR-selection')
    ]),
    
    dcc.Graph(id='graph-content')
])



@callback(
    Output('graph-content', 'figure'),
    Input('DR-selection', 'value'),
    Input('K-selection', 'value'), 
)
def update_fig(DR , K):
    ## access these variables as global in order to update them
    global CLUSTER_ASSIGNMENT
    global CURRENT_K

    if K != CURRENT_K:
        CLUSTER_ASSIGNMENT = Kmeans( data , k=K)
        CURRENT_K = K
    
    df = df_pca
    if DR == "UMAP":
        df = df_umap
    return make_figure( df , cluster_assigment = CLUSTER_ASSIGNMENT )






app.layout = dbc.Container([row] , fluid = True)

app.run(debug=True , host='127.0.0.1')
