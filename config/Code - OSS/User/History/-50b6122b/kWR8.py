import pandas as pd
from datetime import datetime
import os
import scraper as Scraper  # Assuming scraper module exists for getting data

DB_PATH = "./Student_db.csv"
OUTPUT_PATH = "./leetcode_stats.csv"

def fetch_stats(date):
    # Read the student database and existing stats if available
    df_students = pd.read_csv(DB_PATH)
    if os.path.isfile(OUTPUT_PATH):
        df_stats = pd.read_csv(OUTPUT_PATH, header=[0, 1], index_col=[0])
    else:
        df_stats = pd.DataFrame()

    new_data = []

    # Iterate over each student
    for _, student in df_students.iterrows():
        problems_by_date = Scraper.getProblems(student['Leetcode ID'])  # Assuming this function gets data
        val = problems_by_date.get(date)
        if not val:
            val = {'Easy': 0, 'Medium': 0, 'Hard': 0}

        # Prepare a DataFrame for the current student and date
        temp_df = pd.DataFrame({
            'date': [date],
            'Name': [student['Name']],
            'Easy': [val['Easy']],
            'Medium': [val['Medium']],
            'Hard': [val['Hard']]
        })

        new_data.append(temp_df)

    if new_data:
        new_data_df = pd.concat(new_data, ignore_index=True)

        # Set 'Name' as index for both new data and existing stats
        if not df_stats.empty:
            df_stats.set_index('Name', inplace=True)
            new_data_df.set_index('Name', inplace=True)

        # Merge new data with existing stats
        df_stats = pd.concat([df_stats, new_data_df], axis=0)

        # Reset index before saving
        df_stats.reset_index(inplace=True)

        # Save to CSV
        df_stats.to_csv(OUTPUT_PATH, index=False)

if __name__ == "__main__":
    date_today = datetime.now().date()
    print(f"Fetching stats for date: {date_today}")
    fetch_stats(date_today)
