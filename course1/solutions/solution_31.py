# Exercise 3.1
# ************
import pandas as pd
import scipy.stats as stats

# Load the swiss census data from 1880 and display its first few rows.
df_census = pd.read_csv("data/census1880_fractions.csv")
df_census.head()

# 1. Evaluate the association between majority religion and language .
# Create the contingency table.
table = pd.crosstab(df_census["majority religion"], df_census["majority language"])
table

# Assess the strength of the association using a chi-square test.
chi2, pval, df, expected = stats.chi2_contingency(table, correction=False)

# Expected value counts under the null hypothesis. As all values are > 5,
# the Chi2 tests is probably a valid approximation.
expected

# Checking the assumption that all expected values should be > 5
print("All expected values >5 ?", (expected > 5).all())
print("Chi-square contingency p-value: {:.1e}".format(pval))


# 2. How could you make Fisher's test work here ?
#
# The problem with Fisher's test, is that it only works on 2x2 tables. If
# we try "stats.fisher_exact(table)", we get an error.
# To nevertheless try to apply Fisher's test, we need to reduce the number
# dimensions in our contingency table, e.g. by regrouping different
# categories or perform the test by pairs of categories (so that each time
# we have a 2x2 table).

# To nevertheless use Fisher's exact test here, we could:
#  * Regroup different categories.
#  * Perform the test with different combinations of only 2 categories at
#    a time.
# The first option is not obvious here (which to merge?), so we go with the
# second one.
sub_table = table.iloc[:, :2]  # Keep french and german speakers only.
odds_ratio, pvalue = stats.fisher_exact(sub_table)
print("Fisher's exact test on sub-table")
print("\todds ratio:", odds_ratio)
print("\tp-value:", pvalue)


# To automate Fisher's exact test for all category combinations, we can do:
from itertools import combinations

for category1, category2 in list(combinations(table.columns, 2)):
    # Create a sub-table with only 2 categories of language speakers.
    sub_table = table.loc[:, [category1, category2]]

    # Compute Fisher's exact test.
    odds_ratio, pvalue = stats.fisher_exact(sub_table)
    print(f"Fisher's exact test for {category1} vs. {category2}")
    print("\t odds ratio:", odds_ratio)
    print("\t p-value:", pvalue, "\n")
