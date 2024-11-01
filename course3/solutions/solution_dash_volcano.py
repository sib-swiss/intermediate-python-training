from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
import numpy as np



def make_volcano_plot( df ):
    colors = np.array(['lightgrey','blue','red'])[ 1*(df.padj<0.01)*(df.log2FoldChange.abs()>1)*(1+(df.log2FoldChange>0)) ]

    fig = go.Figure()
    fig.add_trace( go.Scatter( x = df.log2FoldChange , y=df.padj , 
                               mode='markers',
                               marker_color = colors ,
                               hovertemplate = "gene name\t: %{text}<br>"+
                                               "logFC\t\t: %{x:.1f}",
                               text = df.gene_name,
                               customdata = df.index ) )

    fig.update_yaxes(type='log',autorange="reversed", exponentformat = 'power',
                     title_text = 'adjusted p-value')
    fig.update_xaxes(title_text = 'log2 Fold Change')
    fig.add_hline(y=0.01, line_dash="dash")
    fig.add_vline(x=-1, line_dash="dash")
    fig.add_vline(x=+1, line_dash="dash")

    fig.update_layout(clickmode='event+select')
    
    return fig


df = pd.read_csv( 'data/Ruhland2016.DESeq2.results.csv' , index_col=0)
df_count = pd.read_csv( "data/Ruhland2016.norm_counts.csv" , index_col= 0 )
df_count_t = df_count.transpose()
df_count_t['condition'] = [ x[:-1] for x in  df_count_t.index ]

fig_volcano = make_volcano_plot( df )
fig_volcano

external_stylesheets = [dbc.themes.CERULEAN]
app = Dash("NAME", external_stylesheets=external_stylesheets)




row = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='volcano-plot',figure=fig_volcano)),
                dbc.Col(dcc.Graph(id='graph-content'))
            ]
        )
    ]
)
app.layout = dbc.Container([row] , fluid = True)


@callback(
    Output('graph-content', 'figure'),
    Input('volcano-plot', 'clickData')
)
def update_graph(clickData):
    
    ## I add a "default" behavior for when the click is None at the beginnig
    if clickData is None:
        return px.strip( df_count_t , x = 'condition' , y = 'ENSMUSG00000100480' )
    gid = clickData['points'][0]['customdata']
    label = clickData['points'][0]['text']
    logFC = clickData['points'][0]['x']
    padj = clickData['points'][0]['y']

    print("click:" , clickData)
    print("click:" , gid)

    fig2 = px.strip( df_count_t , 
                    x = 'condition' , y = gid,
                    title="log2-FC {:.1f} - adjusted p-value {:.1e}".format( logFC , padj ) )
    fig2.update_yaxes(title_text = label )    

    return fig2
    
    
app.run(debug=True , host='127.0.0.1'  , port = 8053)
