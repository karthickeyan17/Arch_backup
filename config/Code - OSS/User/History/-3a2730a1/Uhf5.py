import pandas as pd
import scraper as Scraper
from datetime import datetime, timedelta
import os
import streamlit as st

# Define file paths
DB_PATH = "./Student_db.csv"
OUTPUT_PATH = "./leetcode_stats.csv"
CACHE = "./cache.txt"

# Function to process the statistics
def process_stats(val, name, rollno):
    if not val:
        val = {'Easy': 0, 'Medium': 0, 'Hard': 0}
    return pd.DataFrame(val, index=[f"{rollno}-{name}"])

# Function to fetch statistics
def fetch_stats(date):
    df = pd.read_csv(DB_PATH)
    stats = []

    # Process the stats for each student
    for index, row in df.iterrows():
        problems_by_date = Scraper.getProblems(row['Leetcode ID'])
        val = problems_by_date.get(date)
        stats.append(process_stats(val, row['Name'], row['Roll No.']))

    # Concatenate all student stats into a single DataFrame
    df2 = pd.concat({date: pd.concat(stats, axis=0)}, axis=1, names=['Date', 'Difficulty'])

    if os.path.isfile(OUTPUT_PATH):
        df1 = pd.read_csv(OUTPUT_PATH, header=[0, 1], index_col=[0])

        # Remove existing date column if it exists
        if str(date) in df1.columns.get_level_values(0):
            df1 = df1.drop(columns=[str(date)], level=0)
        # Merge with existing data
        df2 = df2.merge(df1, left_index=True, right_index=True, how='outer')
    
    df2.to_csv(OUTPUT_PATH)
    return df2

# Streamlit app
def main():
    st.title("Leetcode Statistics App")

    # Date input
    date = st.date_input("Select a date", datetime.today())

    # Fetch and display statistics
    if st.button("Fetch Statistics"):
        date_str = date.strftime("%Y-%m-%d")
        df2 = fetch_stats(date_str)
        st.write(df2)

    # Display the existing database
    if st.checkbox("Show Student Database"):
        if os.path.isfile(DB_PATH):
            df = pd.read_csv(DB_PATH)
            st.write(df)
        else:
            st.write("Student database not found.")

    # Display the output file
    if st.checkbox("Show Output File"):
        if os.path.isfile(OUTPUT_PATH):
            df_output = pd.read_csv(OUTPUT_PATH, header=[0, 1], index_col=[0])
            st.write(df_output)
        else:
            st.write("Output file not found.")

if __name__ == "__main__":
    main()
