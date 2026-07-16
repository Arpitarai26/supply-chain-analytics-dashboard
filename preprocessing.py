import pandas as pd
df=pd.read_csv("supply_chain_deliveries.csv")
print("The shape of dataset supply_chain_deliveries.csv is: \n",df.shape)
print("The null values in the dataset is: \n",df.isnull().sum())
print("The features of supply_chain_deliveries.csv are: \n",df.columns)
print("The first five rows: \n",df.head())
print("The last five rows: \n",df.tail())
print("The description of the dataset is: \n",df.describe)
df.describe()
