px.box( df , x = "Body Mass (g)" )
px.box( df , x = "Body Mass (g)" , y = 'Sex')
px.box( df , x = "Body Mass (g)" , y = 'Species')
px.box( df , x = "Body Mass (g)" , y = 'Species' , color = "Sex")
## an alternative would be to create a new column that regroups Species and Sex and use that as y
px.violin( df , x = "Body Mass (g)" , y = 'Species' , color = "Sex")
px.violin( df , x = "Body Mass (g)" , y = 'Species' , 
          color = "Sex",
          color_discrete_map= {"MALE" : "fuchsia",
                               "FEMALE" : "cyan"
                              })