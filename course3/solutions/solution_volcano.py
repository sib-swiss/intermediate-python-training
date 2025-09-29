## adding gene name as hover data 
##
## using plotly.graph_object hover_template

import plotly.graph_objects as go
import numpy as np

# to get the colors, we get the ones whose
# adjusted p-value is < 0.01 and absolute log-fold change is >1
significant = (df.padj<0.01) * (df.log2FoldChange.abs()>1)

# add the log fold change sign to have a different color for UP and DOWN genes
signed_significant = (significant * np.sign( df.log2FoldChange )).astype(int)

colors = signed_significant.map( {0:"lightgrey",1:'red',-1:'blue' } )


fig = go.Figure()
fig.add_trace( go.Scatter( x = df.log2FoldChange , y=df.padj , 
                           mode='markers',
                           marker_color = colors ,
                           hovertemplate = "gene name\t : %{text}<br>"+ # hovertemplate text is in html,
                                           "logFC\t\t : %{x:.1f}", # so use <br> instead of \n
                           text = df.gene_name ) )

fig.update_yaxes(type='log',autorange="reversed", exponentformat = 'power',
                 title_text = 'adjusted p-value')
fig.update_xaxes(title_text = 'log2 Fold Change')
fig.add_hline(y=0.01, line_dash="dash")
fig.add_vline(x=-1, line_dash="dash")
fig.add_vline(x=+1, line_dash="dash")
fig
