import pandas as pd
import scraper as Scraper
from datetime import date, datetime, timedelta
import os

DB_PATH = "./Student_db.csv"
OUTPUT_PATH = "./leetcode_stats.csv"
CACHE = "./cache.txt"

def fetch_stats(date):
    df = pd.read_csv(DB_PATH)
    stats = []
    for index, row in df.iterrows():
        problems_by_date = Scraper.getProblems(row['Leetcode ID'])
        val = problems_by_date.get(date)
        if val:
            stats.append(process_stats(val, row['Name'], date))
    if stats:
        df2 = pd.concat(stats, axis=0)
        if os.path.isfile(OUTPUT_PATH):
            df1 = pd.read_csv(OUTPUT_PATH, header=[0, 1], index_col=[0])

            if date in df1:df1.update(df2)
            else : df1 = pd.merge(df2,df1,left_index=True,right_index=True)
            
            df1.to_csv(OUTPUT_PATH)
        else:
            df2.to_csv(OUTPUT_PATH)
    print(pd.read_csv(OUTPUT_PATH))

def process_stats(val, name, date):
    t = pd.DataFrame(val if val else {'Easy': 0, 'Medium': 0, 'Hard': 0}, index=[0])
    t['date'] = date
    t['Name'] = name
    melted_df = pd.melt(t, id_vars=['date', 'Name'], var_name='level', value_name='count')
    pivot_df = pd.pivot_table(melted_df, columns=['date', 'level'], index='Name', values='count', aggfunc='sum')
    return pivot_df

if __name__ == "__main__":
    for i in range(2,-1,-1):
        date = datetime.now() - timedelta(days=i)
        print("Fetching for date:", date)
        fetch_stats(date.date())