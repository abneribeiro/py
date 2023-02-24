# %%
import pandas as pd
base = pd.read_csv('titanic_train.csv')
#base.tail()
#base.head()
#base.shapeo
#base.info()
#base.isnull().sum()
#base.describe()
base[['Survived','Sex', 'Age']]



# %%
base[base.Fare > 100]

# %%
base.loc[(base.Parch > 1) & (base.SibSp > 1)].head()

# %%
import matplotlib.pyplot as plt

#base.Fare.hist(bins = 20)
base.Pclass.plot.bar();


