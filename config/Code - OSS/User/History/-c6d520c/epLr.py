import pandas as pd
df=pd.read_csv('input.csv')
df2=pd.read_csv('output.csv')
df['date']=len(df)*[0]
melted_df = pd.melt(df, id_vars=['date', 'Roll No.'], var_name='level', value_name='count')
pivot_df = pd.pivot_table(melted_df, columns=['date', 'level'], index='Roll No.', values='count', aggfunc='sum')
print(df2.merge(pivot_df,left_index=True,right_index=True))