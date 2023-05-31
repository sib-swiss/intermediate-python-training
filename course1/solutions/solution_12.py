import pandas as pd
import math
import statistics

# Load the data as DataFrame.
df = pd.read_csv("data/titanic.csv")


# Implementing our own custom `mean` function that skips NaN values.
def custom_mean(seq):
    total = 0
    count = 0
    for x in seq:
        if not math.isnan(x):
            total += x
            count += 1
    return total / count


# Apply `custom_mean()` function to both the "Age" and "Fare" columns.
print(
    "Mean values from our function:\n",
    df.loc[:, ["Age", "Fare"]].apply(custom_mean),
    sep="",
    end="\n\n",
)
print(
    "Mean values from built-in mean function:\n",
    df.loc[:, ["Age", "Fare"]].mean(),
    sep="",
    end="\n\n",
)


# Alternative implementation using .isna()
def custom_mean_2(seq):
    return statistics.mean(seq[~seq.isna()])


# Apply `custom_mean_2()` function to both the "Age" and "Fare" columns.
print(
    "Mean values from our function:\n",
    df.loc[:, ["Age", "Fare"]].apply(custom_mean_2),
    sep="",
    end="\n\n",
)
print(
    "Mean values from built-in mean function:\n",
    df.loc[:, ["Age", "Fare"]].mean(),
    sep="",
    end="\n\n",
)
