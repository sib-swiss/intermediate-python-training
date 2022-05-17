# 1. Plot the Age distribution among first class passengers. Try to choose an appropriate mode of representation (histogram? density line? number of bins?)

# here I prefer the histogram
## bins can be a number, but also a set of boundaries between bins
# using np.arange, I get my bins to be 2.5 years wide 
sns.histplot( df.Age , bins= np.arange(0,85,2.5) ) 
#2. Make a figure with 3 panels. In the panels, plot the histogram of the `Fare` among passengers in
#   the first, second, and third class, respectively.

fig, ax = plt.subplots(3,1 , figsize=(10,10))

for i, pclass in enumerate([1,2,3]):
    sns.histplot( df.loc[ df.Pclass == pclass, 'Fare'] , ax = ax[i] )
    ax[i].set_title("passenger class {}".format(pclass))
plt.tight_layout() # this makes the different subplot organize better, 
# with no collision between labels, titles, ...
