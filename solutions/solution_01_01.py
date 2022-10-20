import pandas as pd
df = pd.read_table("data/titanic.csv", sep=",")

# 1. Select passengers which survived. How many are males/females?

# Solution using the ".value_counts()" or ".describe()" methods of DataFrame.
mask_survived = df.Survived == 1
df[mask_survived, "Sex"].value_counts()
df[mask_survived, "Sex"].describe()

# Solution using a for loop:
for gender in ("male", "female"):
    mask_survived = (df.Survived == 1) & (df.Sex == gender)
    print(f"Number of surviving {gender}: {df.loc[mask_survived, ].shape[0]}")



# 2. Create a new column "Title" in the DataFrame representing the title
#    by which passengers should be addressed.
# 
# The title can be found in the passenger name and is the only word ending
# with a '.'
def get_title(passenger_name):
    """Takes a name and return the appropriate title, which is the only
    word in the name ending with a dot (".").
    """
    split_name = passenger_name.split()
    for word in split_name:
        if word.endswith('.'):
            return word
    
    return 'No title'
    
# use our function on each name to create a new column
df["Title"] = [get_title(name) for name in df.Name]
df.head()

# Alternatively, this can also be written using the map method, which applies
# a function to each element in a column:
df["Title"] = df.Name.map(get_title)
df.head()
