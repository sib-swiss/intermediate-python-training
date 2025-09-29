fig = px.scatter(df , x = 'Body Mass (g)' , y = 'Culmen Depth (mm)' , color = 'Species' )
fig.layout.xaxis.title.text = "Penguin Body Mass (gr.)"
fig.layout.xaxis.title.font = {'color':"blue"}
fig
