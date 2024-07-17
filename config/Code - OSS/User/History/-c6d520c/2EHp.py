import pandas as pd

# Read input and output CSV files
df = pd.read_csv('input.csv')
df2 = pd.read_csv('output.csv')

# Set the 'date' column to 0 for each row in df
df['date'] = len(df) * [0]

# Melt the dataframe to long format
melted_df = pd.melt(df, id_vars=['date', 'Roll No.'], var_name='level', value_name='count')

# Pivot the melted dataframe
pivot_df = pd.pivot_table(melted_df, columns=['date', 'level'], index='Roll No.', values='count', aggfunc='sum')

# Reset index of pivot_df to remove multi-index
pivot_df.reset_index(inplace=True)

# Merge df2 with pivot_df on 'Roll No.'
merged_df = df2.merge(pivot_df, on='Roll No.')

# Print the merged dataframe
print(merged_df)
