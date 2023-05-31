df.Pclass = df.Pclass.astype("category")
df.Survived = df.Survived.astype("bool")
df.describe()
