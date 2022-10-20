import pandas as pd
import seaborn as sns

# Load the input data frame.
df_census = pd.read_table("data/swiss_census_1880.csv", sep=",")


# 1. Compute a new column "fraction_60+" representing the fraction of
#    60+ years old people in each town.
#
# Hints:
#  * Column '60+ y.o.' contains the number of 60+ years old 
#  * Column 'Total' contains the total number of inhabitant
df_census["fraction_60+"] = df_census["60+ y.o."] / df_census["Total"]


# 2. Represent the proportion of people more 60 years old ('60+ y.o.') across
#    all cantons. Choose the most appropriate kind of plot.
#
# Both "box" or "violin" types give good results. With "violin", the plot
# needs to be large enough to look good.
sns.catplot(x='fraction_60+', y="canton name", data=df_census, kind="box", height=10)
sns.catplot(x='fraction_60+', y="canton", data=df_census, kind="violin", height=15)

# It's also possible to use displot(), but it's less readable.
sns.displot(x='fraction_60+', data=df_census, hue="canton" , kind="kde")

# To display the stats without plotting them.
df_census.groupby("canton")["fraction_60+"].describe()
