# 1. Load the data as a pandas DataFrame.
import pandas as pd

# Load the Swiss census 1880 dataset.
df = pd.read_csv("data/swiss_census_1880.csv")
df.head()


# 2. How many people are in the smallest town ?
df.Total.min()

# Bonus: if we want to know which town is the smallest:
df.loc[df.idxmin()["Total"],]
# or
df.loc[df.Total == df.Total.min(),]


# 3. Which fraction of the population live in a town with more than 1'000
#    inhabitants?
cities = df.Total[df.Total > 1000]  # Selecting town with >1000 inhabitants.
print("how many people live in a town larger than 1'000 inhabitants:", cities.sum())
print(
    "Fraction of the population that lives in a town larger than 1'000 inhabitants:",
    cities.sum() / df.Total.sum(),
)

# Alternatively:
df.loc[df.Total > 1000, "Total"].sum() / df.Total.sum()


# 4. How many town have more than 50% of their population speaking french?
#    Number of french speaker / number of people = fraction of french people in each town.
frenchFraction = df["French speakers"] / df.Total
(frenchFraction > 0.5).sum()

# Alternatively:
df.loc[df["French speakers"] / df.Total > 0.5,].shape[0]
