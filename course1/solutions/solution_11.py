# 1. Load the data as a pandas DataFrame.
import pandas as pd

# 1. Load the Swiss census 1880 dataset as a pandas DataFrame.
df = pd.read_csv("data/swiss_census_1880.csv")
df.head()


# 2. Subset the DataFrame to keep only certain columns.
df = df[
    [
        "town name",
        "Total",
        "German speakers",
        "French speakers",
        "Italian speakers",
        "Romansch speakers",
        "canton",
    ]
]
df.head()


# 3. How many people are in the least populated town ?
df.Total.min()

# Bonus: if we want to know which town is the least populated:
df.loc[df.Total.idxmin(),]
# or
df.loc[df.Total == df.Total.min(),]


# 4. Which fraction of the population live in a town with more than 1'000
#    inhabitants?
cities = df.Total[df.Total > 1000]  # Selecting town with >1000 inhabitants.
print("Total number of people in towns with > 1'000 inhabitants:", cities.sum())
print(
    "Fraction of the population in towns with > 1'000 inhabitants:",
    cities.sum() / df.Total.sum(),
)

# Same, but in a single expression:
df.loc[df.Total > 1000, "Total"].sum() / df.Total.sum()


# 5. How many town have more than 50% of their population speaking french?
#    Number of french speaker / number of people = fraction of french people in each town.
frenchFraction = df["French speakers"] / df.Total
(frenchFraction > 0.5).sum()

# Same, but in a single expression:
(df["French speakers"] / df.Total > 0.5).sum()
# or
sum(df["French speakers"] / df.Total > 0.5)
# or
df.loc[df["French speakers"] / df.Total > 0.5,].shape[0]
