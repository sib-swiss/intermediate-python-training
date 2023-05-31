import pandas as pd
import seaborn as sns

# Load the input data as a pandas DataFrame
df_census = pd.read_csv("data/swiss_census_1880.csv")
df_census.head()

# Task 1: Compute a new column "fraction60+" representing the fraction
#         of 60+ years old people in each town.
df_census["fraction60+"] = df_census["60+ y.o."] / df_census["Total"]
df_census.head()

# Task 2: Graphically represent the proportion of people more 60 years old
#         across all cantons.
sns.catplot(x="fraction60+", y="canton", data=df, kind="box", aspect=3, height=7)
plt.grid()
