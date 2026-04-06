import pandas as pd

# Extract
def extract_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Transform
def transform_data(df):
    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.fillna("Unknown")

    # Standardize column names
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    # Example KPI
    if "age" in df.columns:
        df["age_group"] = df["age"].apply(lambda x: "Adult" if int(x) >= 18 else "Child")

    return df

# Load
def load_data(df, output_path):
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    raw_path = "../data/raw/beneficiaries.csv"
    output_path = "../data/processed/clean_data.csv"

    data = extract_data(raw_path)
    clean_data = transform_data(data)
    load_data(clean_data, output_path)

    print("ETL pipeline executed successfully.")
