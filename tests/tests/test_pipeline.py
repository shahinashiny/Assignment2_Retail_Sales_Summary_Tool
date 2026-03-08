from src.loaddata import load_data
from src.clean_data import clean_data
from src.analyze import sales_summary

def test_load_data():
    df = load_data()
    assert df is not None
    assert not df.empty

def test_clean_data():
    df = load_data()
    cleaned_df = clean_data(df)
    assert cleaned_df is not None
    assert not cleaned_df.empty

def test_sales_summary():
    df = load_data()
    cleaned_df = clean_data(df)
    summary = sales_summary(cleaned_df)
    assert "Total Sales" in summary
    assert "Total Profit" in summary
    assert "Average Sales" in summary