# Exercise 3.1
# ************
import pandas as pd

# Load the swiss census data from 1880 and display its first few rows.
df_census = pd.read_csv("data/census1880_fractions.csv")
df_census.head()

# Creating the contingency table
table = pd.crosstab(df_census["majority religion"], df_census["majority language"])
table

# Evaluate the association between majority religion and language using
# a chi-square test.
chi2, pval, df, expected = stats.chi2_contingency(table, correction=False)

# Checking the assumption that all expected values should be > 5
print("All expected values >5 ?", (expected > 5).all())
print("Chi-square contingency p-value: {:.1e}".format(pval))

# To use Fisher's exact test here, we could regroup different categories,
# or perform the test with different couple of categories
