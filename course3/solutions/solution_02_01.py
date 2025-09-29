# 1. add proper trace names to make the legend reflect the sample name
fig = go.Figure()

for sample in [ 'THZ531_T1','THZ531_T2','NVP2_T1','NVP2_T2', 'THZ1_T1' , 'THZ1_T2' ]:

    fig.add_trace( go.Scatter( x =  df['position'],
                               y = df[sample] ,
                               name = sample) 
                 )

fig
# 2. make replicates of the same color (eg, THZ531_T1 and THZ531_T2 should both be the same color)

def remove_replicate(sampleName):
    return sampleName.partition("_")[0]

condition_to_color = {'THZ531' : "red",
                      'NVP2' : "blue",
                      'THZ1' : "green"
                     }


fig = go.Figure()

for sample in [ 'THZ531_T1','THZ531_T2','NVP2_T1','NVP2_T2', 'THZ1_T1' , 'THZ1_T2' ]:

    fig.add_trace( go.Scatter( x =  df['position'],
                               y = df[sample] , 
                               name = sample,
                               line_color = condition_to_color[ remove_replicate(sample) ] 
                             )
                 )

fig
# 3. change the hovered label so that the position appears as a plain integer (e.g., 3768483 instead of 3.768483M)

def remove_replicate(sampleName):
    return sampleName.partition("_")[0]

condition_to_color = {'THZ531' : "red",
                      'NVP2' : "blue",
                      'THZ1' : "green"
                     }


fig = go.Figure()

for sample in [ 'THZ531_T1','THZ531_T2','NVP2_T1','NVP2_T2', 'THZ1_T1' , 'THZ1_T2' ]:

    fig.add_trace( go.Scatter( x =  df['position'],
                               y = df[sample] , 
                               name = sample,
                               line_color = condition_to_color[ remove_replicate(sample) ] ,
                               hovertemplate = "position : %{x:,}<br>"+  # I went a bit farther and
                                               "avg coverage : %{y:.1f}<br>" # used {:,} to get smthg like 3,845,135
                                                                         # and also added the y

                             ) 
                 )

fig
# 4. *extra*: try to use [grouped legend items](https://plotly.com/python/legend/#grouped-legend-items) to make one group per condition (eg, THZ531, NVP2, THZ1, ...)

def remove_replicate(sampleName):
    return sampleName.partition("_")[0]

condition_to_color = {'THZ531' : "red",
                      'NVP2' : "blue",
                      'THZ1' : "green"
                     }


fig = go.Figure()

for sample in [ 'THZ531_T1','THZ531_T2','NVP2_T1','NVP2_T2', 'THZ1_T1' , 'THZ1_T2' ]:

    fig.add_trace( go.Scatter( x =  df['position'],
                               y = df[sample] , 
                               name = sample,
                               line_color = condition_to_color[ remove_replicate(sample) ] ,
                               hovertemplate = "position : %{x:,}<br>"+ 
                                               "avg coverage : %{y:.1f}<br>",
                               legendgroup=remove_replicate(sample),
                               legendgrouptitle_text=remove_replicate(sample)
                             ) 
                 )

fig
