# Course 1 - Notebook 3 micro-exercise corrections
# ******************************************************************************
import numpy as np
import pandas as pd

# ******************************************************************************
# Micro-Exercise 1
# ****************
# Load the dataset.
mice_data = pd.read_csv("data/mice_data.csv")
mice_data.head()

# Plot the distribution of values.
sns.catplot(x="weight", y="diet", data=mice_data, kind="violin")

# Perform a t-test, splitting mice by their diet.
HFD_data = mice_data.loc[mice_data.diet == "HFD", "weight"]
CHOW_data = mice_data.loc[mice_data.diet == "CHOW", "weight"]

tstat, pval = stats.ttest_ind(HFD_data, CHOW_data, equal_var=False)
print("test statistic:", tstat)
print("p-value       :", pval)


# Draw QQplots to check normality of distribution.
fig, ax = plt.subplots(1, 2, figsize=(14, 7))
stats.probplot(HFD_data, dist="norm", plot=ax[0], rvalue=True)
ax[0].set_title("HFD data")
stats.probplot(CHOW_data, dist="norm", plot=ax[1], rvalue=True)
ax[1].set_title("CHOW data")
fig.tight_layout()


# Alternative, using `.groupby()`.
grouped_by_diet = mice_data.groupby("diet").weight
tstat, pval = stats.ttest_ind(
    list(grouped_by_diet)[0][1],
    list(grouped_by_diet)[1][1],
    equal_var=False,
)
print("test statistic:", tstat)
print("p-value       :", pval)

# ******************************************************************************
