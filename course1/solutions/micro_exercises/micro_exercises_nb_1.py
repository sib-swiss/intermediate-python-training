# Course 1 - Notebook 1 micro-exercise corrections
# ******************************************************************************
import numpy as np
import pandas as pd


# ******************************************************************************
# Micro-Exercise 1
# ****************
# Since read_table expects tab-delimited files by default, we must pass the
# argument `sep=","` when loading a CSV file.
df = pd.read_table("data/titanic.csv", sep=",")
df.head()

# Alternatively, we could also set "sep=None" to let Pandas auto-detect
# the type of separator.
df = pd.read_table("data/titanic.csv", sep=None, engine="python")
df.head()

# Display the first 5 and last 3 lines.
df.head()
df.tail(3)
# ******************************************************************************


# ******************************************************************************
# Micro-Exercise 2
# ****************
# Adding columns to a DataFrame.

# Create the initial DataFrame.
size_data = {
    "Name": ["Alice", "Bob", "Jim", "Zoe"],
    "Height": [163, 180, 172, 173],
    "Weight": [58, 97, 63, 60],
}
df_size = pd.DataFrame(size_data)

# Add columns and "Age" column.
df_size["Age"] = 23

# Add a "BMI" column.
height = df_size["Height"]
weight = df_size["Weight"]
df_size["BMI"] = weight / height ** 2
# Alternatively:
df_size["BMI"] = df_size.Weight / df_size.Height ** 2

# Additional Task:
df_size_copy = df_size[ ["Age", "BMI"] ]
df_size_copy.index = df_size["Name"]
df_size_copy
# ******************************************************************************


# ******************************************************************************
# Micro-Exercise 3
# ****************
# Adding columns to a DataFrame.

# Load the DataFrame.
df = pd.read_csv("data/titanic.csv")
df.head()

# Delete columns.
df_copy = df.drop(columns=["Name", "Sex"])

# Delete rows.
df_copy.drop(index=range(1, len(df.index), 2), inplace=True)

# Note: to generate the sequence of rows to delete, we can use:
range(1, len(df.index), 2)
range(1, df.shape[0], 2)
range(1, df.index[-1] + 1, 2)
# ******************************************************************************


# ******************************************************************************
# Micro-Exercise 4
# ****************
# Curate a badly formatted data set.

# Remove the trailing "%" sign and convert to an integer.
percent_column = pd.Series(np.random.randint(0, 100, 100), dtype="str") + "%"

# Check the type is really "Object", also abbreviated 'O'.
print("Type of the Series:", percent_column.dtype)

# Solution using pandas DataFrame methods.
new_column = percent_column.str.strip("%").astype(int)
new_column = percent_column.str.replace("%", "").astype(int)
print("Type of the Series:", new_column.dtype)
new_column.head()

# Solution using base python.
new_column = pd.Series([int(x.strip("%")) for x in percent_column])
print("Type of the Series:", new_column.dtype)
new_column.head()

# Solution that updates values in the existing series.
percent_column.update([int(x.strip("%")) for x in percent_column])
percent_column = percent_column.astype(int)
print("Type of the Series:", percent_column.dtype)
percent_column

# Benchmarking:
%timeit percent_column.str.strip("%").astype(int)
%timeit percent_column.str.replace("%", "").astype(int)
%timeit pd.Series([int(x.strip("%")) for x in percent_column])  # Fastest !!


# Rename the categories of the "Embarked" column to full city names.
df["Embarked"].astype("category").cat.rename_categories({"C": "Cherbourg", "Q": "Queenstown", "S": "Southampton"})
# ******************************************************************************


# ******************************************************************************
# Micro-Exercise 5
# ****************
df = pd.read_csv("data/titanic.csv")

# Select all odd rows from the Titanic data frame, as well as the columns
# "Name", "Age" and "Fare".
df.loc[range(1, df.shape[0], 2), ["Name", "Age", "Fare"]]

# Re-order the columns so that "Age" is first and "Name" is second.
df.loc[range(1, df.shape[0], 2), ["Age", "Name", "Fare"]]

# Same, but using .iloc[]
df.iloc[range(1, df.shape[0], 2), [0, 2, 6]]
df.iloc[range(1, df.shape[0], 2), df.columns.get_indexer(("Name", "Age", "Fare"))]

# Using a conditional selection (will be seen later in the class).
df.loc[df.index % 2 == 1, ["Name", "Age", "Fare"]]

# ******************************************************************************


# ******************************************************************************
# Micro-Exercise 6
# ****************
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
# Micro-Exercise 7
# ****************
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
# Micro-Exercise 8
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
# Micro-Exercise A3
# *****************

def age_category(x):
    age_classes = {"child": 12, "teenager": 17, "adult": 64, "senior": 200}
    for label, threshold in age_classes.items():
        if x <= threshold:
            return label


# Make a copy of the "df" DataFrame.
dfc = df.copy()

# Add a new column "Age_category".
dfc["Age_category"] = df["Age"].map(age_category)
# or
dfc["Age_category"] = df["Age"].apply(age_category)

# Compute survival rates by gender, age category and passenger class.
dfc.groupby(["Sex", "Age_category", "Pclass"]).mean()
# ******************************************************************************