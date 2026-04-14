# Course 1 - Notebook 2 micro-exercise corrections
# ******************************************************************************
import pandas as pd


# ******************************************************************************
# Micro-Exercise 1 - Row and columns selection with .loc[]
# ********************************************************

df = pd.read_csv("data/titanic.csv")

# Select all odd rows from the Titanic data frame, as well as the columns
# "Name", "Age" and "Fare".
df.loc[range(1, df.shape[0], 2), ["Name", "Age", "Fare"]]

# Re-order the columns so that "Age" is first and "Name" is second.
df.loc[range(1, df.shape[0], 2), ["Age", "Name", "Fare"]]

# Additional tasks:
# Same selection, but using the .iloc[] indexer (selects on row and column
# position)
df.iloc[range(1, df.shape[0], 2), [0, 2, 6]]
df.iloc[range(1, df.shape[0], 2), df.columns.get_indexer(("Name", "Age", "Fare"))]

# Using a conditional selection (will be seen later in the class).
df.loc[df.index % 2 == 1, ["Name", "Age", "Fare"]]

# ******************************************************************************


# ******************************************************************************
# Micro-Exercise 2 - Conditional selection
# ****************************************

# Select the fare and name of passengers in first class (Pclass is 1) that
# are less than 18 years old.
mask = (df.Age < 18) & (df.Pclass == 1)
df.loc[mask,]

# What fraction of these passengers survived.
df.loc[mask, "Survived"].mean()
df.loc[mask, ].Survived.mean()

# We can also compute this fraction without using the `.mean()` method, but
# it's slightly more work:
mask_survived = (df.Age < 18) & (df.Pclass == 1) & (df.Survived == 1)
df.loc[mask_survived, ].shape[0] / df.loc[mask, ].shape[0]
# or
sum(mask_survived) / sum(mask)

# Number of women and children:
mask = (df.Age < 18) | (df.Sex == "female")
print("Number of women and children:", df.loc[mask, ].shape[0])

# Compute the median ticket price and age for men and women.
for gender in ("female", "male"):
    print(f"Median ticket price for {gender}:", df.loc[df.Sex == gender, "Fare"].median())
    print(f"Median age of {gender}:", df.loc[df.Sex == gender, "Age"].median())

# Median ticket price and age for men and women, using the `.groupby()` method.
df.groupby("Sex")[["Fare", "Age"]].median()
# ******************************************************************************


# ******************************************************************************
# Micro-Exercise 3 - Conditional assignment
# *****************************************

# Load the titanic dataset as a DataFrame and display it for reference.
df = pd.read_csv("data/titanic.csv")
df.loc[[0, 1, 2, 3, 4, 10, 27],]      # Display some rows with children and
                                      # some with adults.

# Divide by 2 the fare of passengers < 10 years old.
mask = df.Age < 10
df.loc[mask, "Fare"] /= 2
df.loc[[0, 1, 2, 3, 4, 10, 27],]  # Display some rows with children and adults.


# Create a mask to filter the Swiss census 1880 dataset for towns that have a
# majority of Italian and Romansh speakers.
# In which cantons are these towns located, and how many are in each canton?
df_census = pd.read_csv("data/swiss_census_1880.csv")
mask = ((df_census["Italian speakers"] + df_census["Romansch speakers"]) / df_census.Total) > 0.5
df_census.loc[mask,]
df_census.loc[mask, "canton"].value_counts()
# ******************************************************************************


# ******************************************************************************
# Micro-Exercise 4 - Applying custom functions
# ****************
# Add a new column to the DataFrame that contains the full name of the port of
# embarkation of each passenger.

# Load the dataset.
df = pd.read_csv("data/titanic.csv")
df.head()

# Function that expands the port of embarkation abbreviation.
def expand_port_of_embarkation(input_value):
    """Converts the abbreviated port of embarkation to its full name."""
    abbreviations = {"C": "Cherbourg", "Q": "Queenstown", "S": "Southampton"}
    return abbreviations.get(input_value, None) if len(str(input_value)) == 1 else input_value


# Apply the custom function to each value of the "Embarked" column.
df["Embarked_city"] = df["Embarked"].map(expand_port_of_embarkation)
# Or using .apply(), which also works as we work on a single column (Series).
df["Embarked_city"] = df["Embarked"].apply(expand_port_of_embarkation)
df.head()


# Note: an even better solution in this specific case, is to use the ability
# of .map() to directly take a dictionary as input argument (instead of a
# function).
df["Embarked_city"] = df["Embarked"].map({"C": "Cherbourg", "Q": "Queenstown", "S": "Southampton"})
# ******************************************************************************


# ******************************************************************************
# Micro-Exercise 5 - using groupby
# ********************************

# Load the Titanic dataset.
df = pd.read_csv("data/titanic.csv")
df.head()

# Compute the mean fare by passenger class.
df.groupby("Pclass").Fare.mean()

# Compute the mean fare for all combinations of passenger class and gender.
df.groupby(["Pclass", "Sex"]).Fare.mean()
df.groupby("Pclass")["Fare"].mean()
# ******************************************************************************

