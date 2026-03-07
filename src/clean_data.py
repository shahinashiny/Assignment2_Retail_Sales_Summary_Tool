import pandas as pd

def clean_data(df):
    """
    Clean the dataset
    """

    df = df.copy()

    # remove extra spaces in column names
    df.columns = df.columns.str.strip()

    # convert date columns
    if "Order Date" in df.columns:
        df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

    if "Ship Date" in df.columns:
        df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

    # convert numeric columns
    numeric_cols = ["Sales", "Profit", "Quantity", "Discount"]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # remove rows with missing Sales or Profit
    if "Sales" in df.columns and "Profit" in df.columns:
        df = df.dropna(subset=["Sales", "Profit"])

    return df