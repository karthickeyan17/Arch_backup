import pandas as pd
df=pd.read_csv('input.input.csv')
melted_df = pd.melt(df, id_vars=['date', 'rollNo'], var_name='level', value_name='count')
pivot_df = pd.pivot_table(melted_df, columns=['date', 'level'], index='rollNo', values='count', aggfunc='sum')