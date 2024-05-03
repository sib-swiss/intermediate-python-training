# 1. Load the data as a pandas DataFrame.
import pandas as pd 

df = pd.read_csv("data/swiss_census_1880.csv" )
df.head()

# 2. How many people are in the smallest town ?
df.Total.min()

# 3. Which fraction of the population live in a town with more than 1'000 inhabitants?
#     *hint:* as a first step, compute how many people live in a town larger than 1'000 inhabitants

cities = df.Total[ df.Total > 1000 ] # selecting town with >1000 inhabitants
print( "how many people live in a town larger than 1'000 inhabitants:" , cities.sum() )

print( "Fraction of the population that lives in a town larger than 1'000 inhabitants:" , cities.sum() / df.Total.sum() )


# 4. **if you have the time:** How many town have more than 50% of their population speaking french?

# number of french speaker / number of people = fraction of french people in each town
frenchFraction = df["French speakers"] / df.Total 
(frenchFraction>0.5).sum()
