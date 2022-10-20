import pandas as pd
import scipy.stats as stats

df_fractions = pd.read_csv('data/census1880_fractions.csv')

# 1. Test the association between "majority religion" and "majority language".
#
# Create the contingency table.
table = pd.crosstab(df_fractions['majority religion'], df_fractions['majority language'])
table

# Perform a chi-square test.
chi2, pval, df, expected = stats.chi2_contingency(table, correction=False)

# Check the assumption that all expected values should be > 5.
print('Are all expected values > 5 ?', (expected > 5).all()) 
print('Chi-square contingency p-value: {:.1e}'.format(pval ))


# 2. How could you make Fisher's test work here ?
#
# The problem with Fisher's test, is that it only works on 2x2 tables. If
# we try "stats.fisher_exact(table)", we get an error.
# To nevertheless try to apply Fisher's test, we would need to reduce the
# number dimensions in our contingency table, e.g. by regrouping different
# categories or perform the test by pairs of categories (so that each time
# we have a 2x2 table).
