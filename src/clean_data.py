import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize text, parse dates/numeric fields, and retain valid sales rows."""
    cleaned = df.copy()
    cleaned.columns = (
        cleaned.columns.str.replace('"', "", regex=False).str.strip()
    )

    # Normalize inconsistent whitespace so categories/names group consistently.
    for column in cleaned.select_dtypes(include=["object", "string"]).columns:
        cleaned[column] = (
            cleaned[column]
            .str.replace(r"\s+", " ", regex=True)
            .str.strip()
            .replace("", pd.NA)
        )

    for column in ["Order Date", "Ship Date"]:
        if column in cleaned.columns:
            cleaned[column] = pd.to_datetime(cleaned[column], errors="coerce")

    for column in ["Sales", "Profit", "Quantity", "Discount"]:
        if column in cleaned.columns:
            cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")

    if {"Sales", "Profit"}.issubset(cleaned.columns):
        cleaned = cleaned.dropna(subset=["Sales", "Profit"])

    return cleaned
