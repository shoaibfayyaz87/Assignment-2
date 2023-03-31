# -*- coding: utf-8 -*-


from operator import itemgetter 
from itertools import chain 
import pandas as pd
import matplotlib.pyplot as plot
import networkx as nx
import operator
import collections
from heapq import nlargest
from collections import defaultdict


def read_file(fname):
    '''
    This is a generic function with one argument to read a file 
    the name and type is passed as an argument while calling this function
    Parameter : fname is the name of the file
    variable1 data: file is saved in this variable
    variable 2 pd: panda variable
    variable 3 df: dataframe to store file
    data.plot():
    then that data is plotted just to check in the same function which shall be a line plot for most cases 
    the function returns a dataframe to be used for further visualisation
    '''
    
    data=pd.read_csv(fname)
    df1 = pd.DataFrame(data);
  
    #data2 = pd.read_csv('CO2.csv', usecols= [1,35,45,50,64])
   # data.plot()
   
    data.isna()
    data.duplicated()
    
    #df2.plot(x=df.index[0], kind='bar', stacked=True,
    #title='Stacked Bar Graph of joe biden unpopularity')
    data.plot()
 
    return df1




df= read_file('CO2.csv')
#Data exploration
df.describe()
df.info()
print(df.head())
print(df.tail()) 
df. columns. values. tolist()
df.dtypes
to_drop = ['Country Code','Indicator Name','Indicator Code']
df.drop(to_drop, inplace=True, axis=1)
df2= df.T
df2.dropna()




l=[0,32,39,45,50,55,58]
l2=[7,30,40,55,65,109,130,190,205,251]
dfc=df2.iloc[l,l2]

#dfc=df2.iloc[32:58]
dfc.reset_index(drop=True)
#dfc.to_string(index=False)



dfc.dtypes

dfct=dfc.T

dfct['1991']=dfct['1991'].astype(float)
dfct['2014']=dfct['2014'].astype(float)
dfct['2017']=dfct['2017'].astype(float)
dfct['1998']=dfct['1991'].astype(float)
dfct['2004']=dfct['1991'].astype(float)
dfct['2009']=dfct['1991'].astype(float)
dfct.plot()
dfct.plot(x=df.index[0], kind='bar', stacked=True,
    title='Stacked Bar Graph of Country CO2 EMISSION')

dfct.plot.line()







#data2

dff= read_file('gdp.csv')
#Data exploration
dff.describe()
dff.info()
print(dff.head())
print(dff.tail()) 
dff. columns. values. tolist()
dff.dtypes
to_drop = ['Country Code','Indicator Name','Indicator Code']
dff.drop(to_drop, inplace=True, axis=1)
dff2= dff.T
dff2.dropna()




lf=[0,32,39,45,50,55,58]
lf2=[7,30,40,55,65,109,130,190,205,251]
dffc=dff2.iloc[lf,lf2]

#dfc=df2.iloc[32:58]
dffc.reset_index(drop=True)
#dfc.to_string(index=False)



dffc.dtypes

dffct=dfc.T

dffct['1991']=dffct['1991'].astype(float)
dffct['2014']=dffct['2014'].astype(float)
dffct['2017']=dffct['2017'].astype(float)
dffct['1998']=dffct['1991'].astype(float)
dffct['2004']=dffct['1991'].astype(float)
dffct['2009']=dffct['1991'].astype(float)
dffct.plot()
dffct.plot(x=dffc.index[0], kind='bar', stacked=True,
    title='Stacked Bar Graph of Country GDP')

dffct.plot.line()

