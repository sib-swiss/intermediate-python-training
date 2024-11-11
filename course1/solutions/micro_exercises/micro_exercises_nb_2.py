# Course 1 - Notebook 2 micro-exercise corrections
# ******************************************************************************
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
    print(f"Mean fare in class {pclass}:", df.loc[mask, "Fare"].mean())

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

# Make sure all columns now sum to 1:
df_normalized.sum()
# ******************************************************************************


# ******************************************************************************
# Micro-Exercise 3
# ****************
# Load the Titanic dataset.
df = pd.read_csv("data/titanic.csv")

# Compute the mean fare by passenger class.
df.groupby("Pclass").Fare.mean()

# Compute the mean fare for all combinations of passenger class and gender.
df.groupby(["Pclass", "Sex"]).Fare.mean()
# ******************************************************************************
