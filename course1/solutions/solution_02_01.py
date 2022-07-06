## creating the contingency table
table = pd.crosstab( dfFractions['majority religion'] , dfFractions['majority language'] )
table
## performing chi-square
chi2,pval , df, expected = stats.chi2_contingency(table, correction=False)
## checking the assumption that all expected values should be > 5
print('All expected values >5 ?',(expected > 5).all()) 
print( 'Chi-square contingency p-value: {:.1e}'.format(pval ) )
## To use Fisher's exact test here, we could regroup different categories, 
## or perform the test with different couple of categories
