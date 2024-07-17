import pandas as pd
df=pd.read_csv('input.csv')
df2=pd.read_csv('output.csv')
print(pd.concat([df,df2],axis=1))