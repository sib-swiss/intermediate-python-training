def make_plot( df , dateMax , dateMin ):
    
    # subset df based on the given range
    #  because each fossil also has a min and max date, we will decide to 
    #  show anything that intersect with the chose range
    #
    # in these case I find it easier to go with the inverse of:
    #  max date of fossil lower than min of range
    # or 
    #  min date of fossil higher than max of range
    sdf = df.loc[ ~((( df.max_ma ) < -dateMin) |  (( df.min_ma ) > -dateMax) ) , :]
    
    
    # Create figure with subplots
    fig = make_subplots(rows=1, cols=2)


    ### subplot 1

    # coastlines
    fig.add_trace( go.Scatter( visible=True, 
                              x=coastlines.lon, y=coastlines.lat,
                              mode='lines',
                              line_color="lightgrey",
                              showlegend=False,
                              hoverinfo="none" 
                             ) ,
                  row=1, col=1  # this is how we say in which subplot this traces goes
                 )
    def make_label(row):
        return f"{row.accepted_name} ({row.identified_rank})<br>" + f"{row.max_ma:.1f}MYA - {row.min_ma:.1f}MYA"


    # add fossils
    fig.add_trace( go.Scatter( x=sdf['lng'],
                               y=sdf['lat'], 
                               opacity=0.75 , 
                               mode='markers',
                               hovertemplate = "%{text}<br>"+ # custom label
                                             "coords : (%{y:.1f}N, %{x:.1f}E)" ,
                             text = [make_label(row) for i,row in  sdf.iterrows()],
                             showlegend=False
                             ),
                  row=1, col=1
                 )


    ### subplot 2
    R = np.arange(-60, 0.1, 1) ## define a timeline, from -60MYA to now
    nG = [df.loc[ (df.max_ma > -T) & (df.min_ma < -T) , 'genus' ].nunique() for T in R] ## count number of genus at each time

    fig.add_trace( go.Scatter( x=R, 
                               y=nG, 
                               line_color="black",
                               mode='lines',showlegend=False),
                               row=1, col=2) 
    
    ## adding a colored area to visualize the chosen time range
    fig.add_trace(go.Scatter(x=[dateMax,dateMin,dateMin,dateMax], 
                             y=[-10,-10,max(nG)*2,max(nG)*2],
                             fill='toself', 
                             fillcolor = 'grey',
                             mode='lines',
                             line_width=0,
                             opacity=0.5,
                             showlegend=False,
                             hoverinfo="none"
                            ),
                  row=1, col=2
                 )

    ## restricting back the range of the plot's y-axis
    fig.update_layout(yaxis2_range=[0,max(nG)]) # yaxis2 because this is the second plot

    return fig

from dash import Dash, dcc, html

app = Dash()

app.layout = html.Div([
    dcc.Graph(id='graph-content'),
    dcc.RangeSlider(-60, 0, value=[-40, -20] , id = "date-picker")
])


@callback(
    Output('graph-content', 'figure'),
    Input('date-picker', 'value'))
def update_graph(chosen_range):

    dateMax , dateMin = chosen_range
    return make_plot( df , dateMax , dateMin )



if __name__ == '__main__':
    
    app.run(debug=True , host='127.0.0.3')
