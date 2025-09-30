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
        html.Div(children='''Pick a canton:'''),
        dcc.Dropdown(list(range(1,11)), 1, id='K-selection'),
        dcc.RadioItems(['UMAP','PCA'], 'UMAP', inline=True, id='DR-selection')
    ]),
    
    dcc.Graph(id='graph-content'),
    
    
    
    html.Div([ ## This is where we print the click results
            dcc.Markdown("" , id = "click-field",dangerously_allow_html= True)
        ]),
])



@callback(
    Output('graph-content', 'figure'),
    Input('DR-selection', 'value'),
    Input('K-selection', 'value'), 
)
def update_DR(DR , K):
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


def make_table(VC):
    """make a table from the result of a pandas value_counts()"""
    res = "<table>\n"
    res += "<tr><th>value</th><th>count</th></tr>\n"
    for i,c in VC.items():
        res += f"<tr><td>{i}</td><td>{c}</td></tr>\n"
    
    res += "</table>"
    
    return res


@callback(
    Output('click-field', 'children'),
    Input('graph-content', 'clickData'))
def display_click_data(clickData):
    if clickData is None:
        return f""
    else:
        selected_point = clickData['points'][0]['pointNumber']
        current_cluster = CLUSTER_ASSIGNMENT[selected_point]
        
        VC = df_pca.loc[ CLUSTER_ASSIGNMENT == current_cluster , "labels" ].value_counts()
        
        res = make_table(VC)        
        return res





app.layout = dbc.Container([row] , fluid = True)

app.run(debug=True , host='127.0.0.1')
