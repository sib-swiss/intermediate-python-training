# A more fancy solution inspired by  https://seaborn.pydata.org/examples/kde_ridgeplot.html
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the input data as a pandas DataFrame
df_census = pd.read_csv("data/swiss_census_1880.csv")
df_census["fraction60+"] = df_census["60+ y.o."] / df_census["Total"]

# Set the theme.
sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})

# Let's plot the canton in order of their median fraction of 60+ y.o.
order = df_census.groupby("canton")["fraction60+"].median().sort_values().index

# Initialize the FacetGrid object.
pal = sns.cubehelix_palette(10, rot=-0.25, light=0.7)  # setting color palette

# Create a grid: multiple subplots on which different subsets of the data
# are drawn.
g = sns.FacetGrid(
    df_census,
    row="canton",
    row_order=order,
    hue="canton",
    hue_order=order,
    aspect=30,
    height=0.5,
    palette=pal,
)

# Draw the densities in a few steps.
g.map(
    sns.kdeplot,
    "fraction60+",
    bw_adjust=0.5,
    clip_on=False,
    fill=True,
    alpha=1,
    linewidth=1.5,
)
g.map(sns.kdeplot, "fraction60+", clip_on=False, color="w", lw=2, bw_adjust=0.5)

# Passing color=None to refline() uses the hue mapping.
g.map(plt.axhline, y=0, linewidth=2, linestyle="-", color=None, clip_on=False)


# Define and use a simple function to label the plot in axes coordinates.
def label(x, color, label):
    ax = plt.gca()
    ax.text(
        0,
        0.2,
        label,
        fontweight="bold",
        color=color,
        ha="left",
        va="center",
        transform=ax.transAxes,
    )


g.map(label, "fraction60+")

# Set the subplots to overlap.
g.fig.subplots_adjust(hspace=-0.25)

# Remove axes details that don't play well with overlap.
g.set_titles("")
g.set(yticks=[], ylabel="")
g.set(xlabel="fraction of people over 60 in 1880 - distribution by towns")
g.despine(bottom=True, left=True)
