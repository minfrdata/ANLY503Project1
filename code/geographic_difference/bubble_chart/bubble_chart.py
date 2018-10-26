import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

########## Read in the datasets ###############
## The truecar.com dataset
trueCar = pd.read_csv("TrueCar_cleaned.csv", index_col = 0)
## The dataset describing transportation usage of each state
state_trans = pd.read_excel("state_transportation.xlsx")
## The last row of the state transportation dataset is the data for the United States in total.
## We only need the transportation usage data for each state.
## Thus, drop the last row of the state transportation dataset
state_trans = state_trans.drop(state_trans.index[51])
## The characteristics data for each state
state_char = pd.read_excel("us-income-density-gdp-2017-by-state.xlsx")

## To later merge the dataset more conveniently, rename the joint key column.
trueCar = trueCar.rename(columns = {'State': 'State Abbreviation'})
#trueCar.head()

## Merge the dataset of state characteristics and the dataset of state transportation usage
statesDF = pd.merge(state_char, state_trans, on = 'State')

## To obtain the used car sales volume of each state and the average sales price,
### first group by the state abbreviation and aggregate
trueCar_avgPrice = pd.DataFrame(trueCar.groupby('State Abbreviation', as_index = False)['Price'].mean())
trueCar_avgPrice = trueCar_avgPrice.rename(columns = {'Price': 'avgPrice'})
trueCar_sales = pd.DataFrame(trueCar.groupby('State Abbreviation', as_index = False)['Price'].count())
trueCar_sales.columns = ['State Abbreviation', 'salesVolume']

## Merge the dataset with state characteristics and state transportation with the sales volume data
### and the average sales price data.
mergedDF = pd.merge(statesDF, trueCar_avgPrice, on = 'State Abbreviation')
mergedDF = pd.merge(mergedDF, trueCar_sales, on = 'State Abbreviation')
## For convenience, save the merged dataframe, 
### since the following plot in this section will use the merged data
mergedDF.to_csv('mergedDF.csv', index = False)

## The plot the bubble chart
plt.figure(figsize = (8, 6))
sns1 = sns.relplot(x = 'Population estimate July 1, 2016', y = 'Public transportation (excluding taxicab) %',
           size = 'salesVolume', sizes = (5, 400),
            data = mergedDF)
plt.title("Sales Volume vs Public Transportation Usage and Population")
# Save the figure
#sns1.savefig("../project_web_1.0/img/PubTrans_Population_salesVol.png", dpi = 200)

