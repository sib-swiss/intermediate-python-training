import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Load the data as DataFrame.
df = pd.read_csv("data/titanic.csv")

# 1. Plot the age distribution among first class passengers. Try to choose an
# appropriate mode of representation (histogram? density line? number of bins?)

# To display the data, we will here use histograms. To define the histogram
# bins, we can either give a number (of bins), or a set of boundaries between
# bins using np.arange(), I get my bins to be 2.5 years wide
sns.histplot(df["Age"], bins=np.arange(0, 85, 2.5))


# 2. Create a figure with 3 panels. In the panels, plot the histogram of the
# `Fare` among passengers in first, second, and third class, respectively.
# Note the usage of the `sharex=True` option to have the same x-axis range
# across all subplots.
fig, ax = plt.subplots(3, 1, figsize=(10, 10), sharex=True)
for i, pclass in enumerate([1, 2, 3]):
    sns.histplot(df.loc[df["Pclass"] == pclass, "Fare"], ax=ax[i], binwidth=10)
    ax[i].set_title(f"passenger class {pclass}")
    ax[i].xaxis.grid()  # Add vertical lines.

# Makes the different subplot organize better - no collision between labels,
# titles, etc.
plt.tight_layout()
