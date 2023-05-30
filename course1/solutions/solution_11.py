import pandas as pd

# Load the data as DataFrame.
df = pd.read_table("data/titanic.csv", sep=",")

# 1. Select passengers which survived. How many are males/females?
survived = df.Survived == 1
survivors = df.loc[survived, "Sex"].value_counts()
for gender in survivors.index:
    print(f"Number of surviving {gender}: {survivors[gender]}")

# Bonus: compute the survival rates among women/men.
# Note: "survival_rate:.1f" allows to format the number so it becomes rounded
# at 1 digit after the decimal.
for gender in survivors.index:
    survival_rate = survivors[gender] / sum(df["Sex"] == gender) * 100
    print(f"Number of surviving {gender}: {survivors[gender]} [{survival_rate:.1f}%]")


# 2. Create a new column named "Title" in the DataFrame, representing
#    the title by which passengers should be addressed. The title can
#    be found in the passenger name and is the only word ending with a '.'

# First we create a short function that extracts a passenger title from
# its name.
def get_passenger_title(name):
    """Takes a name and return the appropriate title. Only works if
    the title is the only word in the name ending with a "."
    """
    split_name = name.split()
    for word in split_name:
        if word.endswith("."):
            return word
    else:
        return 'no_title'
    
# Use our function on each name to create the new "Title" column.
df["Title"] = [get_passenger_title(name) for name in df["Name"]]
df.head()

# To quickly check the list of unique values stored in "Title" (can be
# useful to check if we have a bad value in our column).
print(set(df["Title"]))

# Alternatively, this can also be written using the pandas "apply()"
# method, which applies a function to each element of a column:
df["Title"] = df["Name"].apply(get_passenger_title)
df.head()
