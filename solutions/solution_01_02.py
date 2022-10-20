# 1. Plot the Age distribution among first class passengers.
# Try to choose an appropriate mode of representation (histogram?
# density line? number of bins?)
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load the Titanic dataset.
df = pd.read_table("data/titanic.csv", sep=",")

# 1. Plot the Age distribution among first class passengers. Try to choose an
# appropriate mode of representation (histogram? density line? number of bins?).
#
# Here we will prefer a regular histogram.
# Note: Bins can be be given as a number (the number of bins), but also as a
# set of boundaries between bins using np.arange(). Here we set our bins to
# be 2.5 years wide.
plot_title = "Age distribution among first class passengers"
mask = df.Pclass == 1
sns.histplot(df.loc[mask, "Age"] , bins=np.arange(0, 85, 2.5)).set(title=plot_title)


# 2. Make a figure with 3 panels. In the panels, plot the histogram of the
#   "Fare" among passengers in the first, second, and third class, respectively.
#
# Create an empty figure with 2 subplots.
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

# Fill the subplots.
sns.histplot(df.loc[df.Pclass == 1, "Fare"], ax=ax[0])
ax[0].set_title("passenger class 1")
sns.histplot(df.loc[df.Pclass == 2, "Fare"], ax=ax[1])
ax[1].set_title("passenger class 2")
sns.histplot(df.loc[df.Pclass == 3, "Fare"], ax=ax[2])
ax[2].set_title("passenger class 3")

plt.tight_layout() # This makes the different subplot organize better, 
                   # with no collision between labels, titles, ...


# 3. Additional tasks:
#  * Use a "for loop" to draw the subplots.
#  * Standardize the x axis among the plots.
#  * Use different colors for each passenger category.
#  * Add a title to each subplot.
fig, ax = plt.subplots(1, 3, figsize=(15, 5), sharex=True)
colors = ("goldenrod", "teal", "orangered")

# Fill the subplots.
for i, pclass in enumerate([1, 2, 3]):
    sns.histplot( df.loc[ df.Pclass == pclass, 'Fare'] , ax=ax[i], color=colors[i] )
    ax[i].set_title(f"passenger class {pclass}")

plt.tight_layout()