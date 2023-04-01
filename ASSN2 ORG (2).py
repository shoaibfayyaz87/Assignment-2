# -*- coding: utf-8 -*-


from operator import itemgetter 
from itertools import chain 
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import operator
import collections
from heapq import nlargest
from collections import defaultdict
import seaborn as sns
from sklearn.datasets import load_iris


def read_file(fname): #read csv file
    '''
    This is a generic function with one argument to read a file 
    the name and type is passed as an argument while calling this function
    Parameter : fname is the name of the file
    variable1 data: file is saved in this variable
    variable 2 pd: panda variable
    variable 3 df: dataframe to store file
    
    '''
    
    data=pd.read_csv(fname)
    df1 = pd.DataFrame(data);
    df2=df1.T
    return df1,df2


def exploration(ddf):  #Data exploration
     '''
    This is a generic function with one argument to read a file 
    the name and type is passed as an argument while calling this function
    Parameter : fname is the name of the file
    variable1 data: file is saved in this variable
    variable 2 pd: panda variable
    variable 3 df: dataframe to store file
    
    '''
     print(ddf.describe())
     print(ddf.info())
     print(ddf.head())
     print(ddf.tail()) 
     print(ddf. columns. values. tolist())
     print(ddf.dtypes)
     print(ddf.isna())
     print(ddf.duplicated())

  
def cleaning(ddf):
    to_drop = ['Country Code','Indicator Name','Indicator Code']
    ddf.drop(to_drop, inplace=True, axis=1)
    df2= ddf.T
    df2.dropna()
    l=[0,32,39,45,50,55,58]
    l2=[7,30,40,55,65,109,130,190,205,251]
    dfc=df2.iloc[l,l2]
    dfc.reset_index(drop=True)
    return dfc


def dtypes(dfc):
    dfc.dtypes

    dfct=dfc.T

    dfct['1991']=dfct['1991'].astype(float)
    dfct['2014']=dfct['2014'].astype(float)
    dfct['2017']=dfct['2017'].astype(float)
    dfct['1998']=dfct['1991'].astype(float)
    dfct['2004']=dfct['1991'].astype(float)
    dfct['2009']=dfct['1991'].astype(float)
    dfct.plot()
    return dfct
    



#data1, calling methods
df,df2= read_file('CO2.csv')
exploration(df)
exploration(df2)
df2=cleaning(df)
d=dtypes(df2)

d.plot(x=df.index[0], kind='bar', 
    title='Countries CO2 EMISSION')
    
    
#data2, calling methods

dff,dff2= read_file('gdp.csv')
exploration(dff)
exploration(dff2)
dff2=cleaning(dff)
d2=dtypes(dff2)
d2.plot(x=df.index[0], kind='bar', 
    title=' GDP of Countries')


#data3, calling methods
df3,df33= read_file('population.csv')
exploration(df3)
exploration(df33)
l=[32,39,40]
l2=[0,30,40,55,65]
df3.reset_index(drop=True)
df3=df3.iloc[l]
dfff=df3.iloc[:,l2]
display('                         Population growth (annual %)')
display(dfff)













#data4, calling methods
df4,df44= read_file('forest.csv')
exploration(df4)
exploration(df44)
#df44=cleaning(df4)
d4=dtypes(df44)

l2=[0,30,40,55,65]
df4.reset_index(drop=True)
df4=df4.iloc[l]
dff=df4.iloc[:,l2]
display('                  forest growth (annual %)')
display(dff)






#all data, calling methods
dfa,dfa2= read_file('all.csv')
exploration(dfa)
exploration(dfa2)

#correlation for china
data=pd.read_csv('all.csv',usecols= [1,2,5,36,37,45,50,60])
dfa1 = pd.DataFrame(data);
spec=dfa1.iloc[3042:3052,:]
spec.dropna()
x=list(["Urban population growth (annual %)","  Population, total","Population growth (annual %)","Poverty headcount","underweight","health workers","Mortality rate"])
spec.corr(method='kendall')
plt.figure(figsize=(10,10))
plt.xlabel('Years')
plt.ylabel('indicators')
plt.title('China correlation matrix')
spec.reset_index(drop=True)
ax=plt.axes()
sns.heatmap(spec.corr(method='kendall'),xticklabels= x,  annot=True)
plt.show()


#correlation for United Kingdom
dfa2 = pd.DataFrame(data);
spec2=dfa2.iloc[6158:6168,:]
spec2.dropna()
x=list(["Urban population growth (annual %)","  Population, total","Population growth (annual %)","Poverty headcount","underweight","health workers","Mortality rate"])
spec2.corr(method='kendall')
plt.figure(figsize=(10,10))
plt.xlabel('Years')
plt.ylabel('indicators')
plt.title('United Kingdom correlation matrix')
spec2.reset_index(drop=True)
ax=plt.axes()
sns.heatmap(spec2.corr(method='kendall'),xticklabels= x,  annot=True)
plt.show()
