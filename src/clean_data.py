import pandas as pd

def clean_data(df):
    df = df.copy()

    df.columns = df.columns.str.replace('"', '', regex=False).str.strip()

    if "Order Date" in df.columns:
        df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

    if "Ship Date" in df.columns:
        df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

    numeric_cols = ["Sales", "Profit", "Quantity", "Discount"]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    if "Sales" in df.columns and "Profit" in df.columns:
        df = df.dropna(subset=["Sales", "Profit"])

    return df