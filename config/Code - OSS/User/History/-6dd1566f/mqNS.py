import pandas as pd
import scraper as Scraper
from datetime import datetime, timedelta
import os, sys, argparse

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
        if len(stats) == 3:  # Only process the first 3 students
            break

    # Concatenate all student stats into a single DataFrame
    df2 = pd.concat({date: pd.concat(stats, axis=0)}, axis=1, names=['Date', 'Difficulty'])

    if os.path.isfile(OUTPUT_PATH):
        df1 = pd.read_csv(OUTPUT_PATH, header=[0, 1], index_col=[0])

        # Remove existing date column if it exists
        if date in df1.columns.get_level_values(0):
            df1 = df1.drop(columns=date, level=0)

        # Merge with existing data
        df2 = df2.merge(df1, left_index=True, right_index=True, how='outer')

    # df2.to_csv(OUTPUT_PATH)
    print(df2)

# Main function to parse arguments and execute the script
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help="Output File")
    parser.add_argument("-i", "--input", help="Input File")
    args = parser.parse_args()

    # Print help message if no arguments are provided
    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit(1)

    # Update the output file path if provided
    if args.output:
        OUTPUT_PATH = args.output
    
    # Update the input file path if provided and validate its existence
    if args.input:
        DB_PATH = args.input
        if not os.path.isfile(DB_PATH):
            print("Invalid input")
            sys.exit(1)

    # Get the current date
    date = datetime.now().date()
    print("Fetching for date:", date)
    
    # Ensure the cache file exists
    if not os.path.isfile(CACHE):
        open(CACHE, 'w').close()
    
    # Fetch and process the stats
    # fetch_stats((datetime.now()-timedelta(days=1)).date())
    fetch_stats(date)
    # fetch_stats(date)
