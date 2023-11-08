# Course 1 - Notebook 2 micro-exercise corrections
# ******************************************************************************
import numpy as np
import pandas as pd

# ******************************************************************************
# Micro-Exercise 1
# ****************
# Load the Titanic data set.
df = pd.read_csv("data/titanic.csv")
df.head()

# Compute the mean fare for each passenger class (Pclass).
for pclass in sorted(df.Pclass.unique()):
    mask = df.Pclass == pclass
    print(f"Mean fare for passengers in class {pclass}:", df.loc[mask, "Fare"].mean())

# A shorter way to obtain the same result (but that we have not seen yet),
# is to use the `.groupby()` method.
df.groupby("Pclass")["Fare"].mean()
df.groupby("Pclass").Fare.mean()

# ******************************************************************************


# ******************************************************************************
# Micro-Exercise 2
# ****************
# Load the single cell dataset.
df_sc = pd.read_table("data/pbmc_data.countMatrix.50.txt.zip", sep=" ", index_col=0)
# or
df_sc = pd.read_table(
    "data/pbmc_data.countMatrix.50.txt.zip", sep=" ", index_col="gene"
)
df_sc.head()

# 1. Compute the sum for each column.
col_sums = df_sc.sum()

# 2. Normalize each column by dividing its values by the column-wise sum.
df_normalized = df_sc / col_sums
print("Are all columns sums == 1 after normalization:", all(df_normalized.sum() > 0.99))

# ******************************************************************************


# ******************************************************************************
# Micro-Exercise 3
# ****************
# Load the Titanic dataset.
df = pd.read_csv("data/titanic.csv")
df.head()

# Make a copy of the dataset and compute the "Age_category" column values.
dfc = df.copy()


def age_category(x):
    age_classes = {"child": 12, "teenager": 17, "adult": 64, "senior": 200}
    for label, threshold in age_classes.items():
        if x <= threshold:
            return label


dfc["Age_category"] = dfc.Age.map(age_category)
dfc.head()


# Compute the survival rate by age, gender and passenger class.
dfc.groupby(["Sex", "Pclass", "Age_category"]).Survived.mean()

# Create a DataFrame that contains both the survival rates and the counts
# (i.e. number of people) per category.
grouped = dfc.groupby(["Sex", "Pclass", "Age_category"])
survival_rates = pd.DataFrame(
    [grouped["Survived"].count(), grouped["Survived"].mean()],
    index=["Counts", "Survival_rate"],
).transpose()
survival_rates["Counts"] = survival_rates["Counts"].astype(int)
survival_rates["Survival_rate"] = survival_rates["Survival_rate"].round(2)
survival_rates

# ******************************************************************************
