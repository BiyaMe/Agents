import pandas as pd
import io

def clean_data(df: pd.DataFrame):
    """Fills missing values and removes duplicates."""
    df.fillna(df.median(numeric_only=True), inplace=True)
    df.drop_duplicates(inplace=True)
    return df

def load_csv(contents: bytes):
    """Loads CSV data from uploaded file."""
    return pd.read_csv(io.StringIO(contents.decode("utf-8")))

def log_interaction(query, result):
    # Log interaction for future reference
    with open("interaction_log.txt", "a") as log_file:
        log_file.write(f"Query: {query}, Result: {result}\n")