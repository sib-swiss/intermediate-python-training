import pandas as pd

# 1. Load the data as a pandas DataFrame.
df = pd.read_table("data/titanic.csv", sep=",")

# 2. Select passengers which survived. How many are males/females?
df.loc[df.Survived == 1, "Sex"].value_counts()

# Alternative solution using a for loop:
for gender in df.Sex.unique():
    mask_survived = (df.Survived == 1) & (df.Sex == gender)
    print(f"Number of surviving {gender}: {df.loc[mask_survived, ].shape[0]}")

# Bonus: compute the survival rates among women/men.
# Note: ":.1f" allows to format the number so it becomes rounded at 1 digit
# after the decimal.
for gender in df.Sex.unique():
    mask = df.Sex == gender
    survivor_count = sum(df.Survived[mask])
    print(
        f"Number of surviving {gender}: {survivor_count} [{survivor_count / sum(mask) * 100:.1f}%]"
    )

# Bonus: the easiest way to compute the number of female and male survivors,
# as well as the survival rates, is to use the `.groupby()` method.
df.groupby("Sex").Survived.sum()  # Total male/female survivors.
df.groupby("Sex").Survived.mean()  # Survival rates by gender.


# 3. Create a new column named "Title" in the DataFrame, representing
#    the title by which passengers should be addressed.
# First we create a short function that extracts a passenger title from
# its name.
def get_passenger_title(name):
    """Takes a name and return the appropriate title. Only works if
    the title is the first word in the input string ending with a ".".
    """
    for word in name.split():
        if word.endswith("."):
            return word

    return "no_title"


# Then we can apply our custom function to each element of the "Name" column
# using the `.map()` method of pandas Series.
df["Title"] = df["Name"].map(get_passenger_title)
df.head()

# To quickly check the list of unique values stored in "Title" (can be
# useful to check if we have a bad value in our column).
df.Title.unique()
print(set(df["Title"]))  # Alternatively.


# Note: an alternative way of applying the `get_passenger_title()` function
# to the name column would be to use a list comprehension.
# However, this method is SLOWER than using the `.map()` method and you
# should always AVOID AS MUCH AS POSSIBLE this type of non-vectorized
# operations.
df["Title"] = [get_passenger_title(name) for name in df["Name"]]
df.head()


# Alternative implementation of the "get_passenger_title" function.
def get_passenger_title(name):
    if "." not in name:
        return "no_title"
    return name.partition(".")[0].rpartition(" ")[-1]
