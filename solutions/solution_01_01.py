# 1. Select passengers which survived. How many are males/females?
m_survived = df.Survived == 1
m_survived.value_counts()
#2. Create a new column Title is the DataFrame representing the title by which passengers should be addressed. The title can be found in the passenger name and is the only word ending with a '.'

def getTitle( name ):
    ''' takes a name and return the appropriate title, which is the only word in the name ending with a "."'''
    splitted_name = name.split()
    for word in splitted_name:
        if word.endswith('.'):
            return word
    else:
        return 'No title'
    
## use our function on each name to create a new column
df["Title"] = [getTitle(name) for name in df.Name]

## alternatively, this can also be written using the apply method,
## which applies a function to each element in a column:
df["Title"] = df.Name.apply(getTitle)

df.head()
