# Course 1 - Notebook 1 micro-exercise corrections
# ******************************************************************************
import numpy as np
import pandas as pd


# ******************************************************************************
# Micro-Exercise 1
# ****************
#
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
# Micro-Exercise 2 - Adding columns
# *********************************

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

# Alternative, without creating intermediate variables:
df_size["BMI"] = df_size.Weight / df_size.Height ** 2

# Additional Task:
df_size_copy = df_size[["Age", "BMI"]]
df_size_copy.index = df_size["Name"]
df_size_copy
# ******************************************************************************


# ******************************************************************************
# Micro-Exercise 3 - Deleting columns and rows
# ********************************************

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
# Micro-Exercise 4 - Curate a badly formatted dataset
# ***************************************************

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
# For a more realistic benchmarking, we use a Series with more values (100'000).
percent_column = pd.Series(np.random.randint(0,100,100_000), dtype="str") + '%'
%timeit percent_column.str.strip("%").astype(int)               # Fastest !!
%timeit percent_column.str.replace("%", "").astype(int)
%timeit pd.Series([int(x.strip("%")) for x in percent_column])


# Rename the categories of the "Embarked" column to full city names.
port_of_embarkation_mapping = {
    "C": "Cherbourg",
    "Q": "Queenstown",
    "S": "Southampton"
}
df["Embarked"].astype("category").cat.rename_categories(port_of_embarkation_mapping)
# ******************************************************************************
