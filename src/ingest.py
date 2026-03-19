import os
import pandas as pd

def load_latest_file(input_path):
    # get all files
    files = os.listdir(input_path)

    # filter only CSV files
    csv_files = [f for f in files if f.endswith(".csv")]

    if not csv_files:
        raise Exception("No CSV files found in folder")

    # find latest file based on creation time
    latest_file = max(
        csv_files,
        key=lambda x: os.path.getctime(os.path.join(input_path, x))
    )

    full_path = os.path.join(input_path, latest_file)

    # read file
    df = pd.read_csv(full_path)

    return df, latest_file