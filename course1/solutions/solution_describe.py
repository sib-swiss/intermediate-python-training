df.Pclass = df.Pclass.astype('object')
df.Survived = df.Survived.astype('bool')
df.describe()