# Graphically represent the proportion of people over 60 years old (60+ y.o.) across all cantons. Choose the most appropriate kind of plot.
sns.catplot(x="60+ y.o.", y="canton", data=df_census, kind="box", aspect=3, height=7)
plt.grid()
# Graphically represent the proportion of people of the Catholic faith (Catholic) depending on
# the main language (majority language). 
# Choose the most appropriate kind of plot, and setup a color scheme such that:
#    German speakers : '#D81B60'
#    French speakers : '#1E88E5'
#    Italian speakers : '#004D40'
#    Romanche speakers : '#FFC107'

sns.catplot(x="Catholic", 
            y="majority language", 
            data=df_census, 
            kind="strip", 
            alpha=0.5,
            hue = "majority language", 
            palette = {'German speakers' : '#D81B60',
                       'French speakers' : '#1E88E5',
                       'Italian speakers' : '#004D40',
                       'Romanche speakers' : '#FFC107'},
            aspect=2, height=7, )
plt.grid()
