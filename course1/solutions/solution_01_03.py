# 1.  compute a new column "fraction60+" representing the fraction of 60+ years old people in each town.
# hint : column '60+ y.o.' contains the number of 60+ years old ; 
#        column 'Total' contains the total number of inhabitant
df_census["fraction60+"] = df_census["60+ y.o."] / df_census["Total"]

#2. Represent the proportion of people more 60 years old ('60+ y.o.') across all cantons. 
#   Choose the most appropriate kind of plot.

sns.catplot( x='fraction60+' , data= df_census , hue = 'canton' , kind='box')
