import pandas as pd

# Read input and output CSVs
df = pd.read_csv('input.csv')
df2 = pd.read_csv('output.csv')

# Add a 'date' column to df
df['date'] = len(df) * [0]

# Melt the DataFrame
melted_df = pd.melt(df, id_vars=['date', 'Roll No.'], var_name='level', value_name='count')

# Pivot the melted DataFrame
pivot_df = pd.pivot_table(melted_df, columns=['date', 'level'], index='Roll No.', values='count', aggfunc='sum')

# Ensure column name consistency for merging
# pivot_df.rename(columns={'Roll No.': 'rollNo'}, inplace=True)  # Rename for consistency
print(pivot_df)
# merged_df = df2.merge(pivot_df, on='rollNo')

# print(merged_df)
