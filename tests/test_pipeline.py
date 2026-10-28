import pandas as pd
import pytest

from src.analyze import sales_summary, top_10_products
from src.clean_data import clean_data
from src.loaddata import load_data


def test_load_data_has_expected_fields():
    df = load_data()
    assert not df.empty
    assert {"Sales", "Profit", "Product Name", "Customer Name", "Category"}.issubset(
        df.columns
    )


def test_clean_data_normalizes_text_and_numeric_values():
    raw = pd.DataFrame(
        {
            "Category": [" Furniture  ", "Office  Supplies", "Gadgets"],
            "Order Date": ["11/8/2016", "12/9/2016", "not-a-date"],
            "Sales": ["10.50", "11.00", "not-a-number"],
            "Profit": ["2.50", "5.00", "5.00"],
            "Quantity": ["2", "1", "1"],
        }
    )

    cleaned = clean_data(raw)

    assert len(cleaned) == 2
    assert cleaned.iloc[0]["Category"] == "Furniture"
    assert cleaned.iloc[1]["Category"] == "Office Supplies"
    assert cleaned.iloc[0]["Order Date"] == pd.Timestamp("2016-11-08")
    assert cleaned.iloc[0]["Sales"] == pytest.approx(10.5)
    assert cleaned.iloc[0]["Profit"] == pytest.approx(2.5)


def test_sales_summary_returns_correct_totals():
    df = pd.DataFrame(
        {
            "Sales": [10.0, 20.0, 30.0],
            "Profit": [2.0, 5.0, -1.0],
            "Product Name": ["Widget", "Widget", "Gadget"],
        }
    )

    summary = sales_summary(df)

    assert summary["Total Sales"] == pytest.approx(60.0)
    assert summary["Total Profit"] == pytest.approx(6.0)
    assert summary["Average Sales"] == pytest.approx(20.0)


def test_top_products_aggregates_sales_by_product():
    df = pd.DataFrame(
        {
            "Product Name": ["Widget", "Widget", "Gadget"],
            "Sales": [10.0, 20.0, 15.0],
        }
    )

    result = top_10_products(df)

    assert result.iloc[0]["Product Name"] == "Widget"
    assert result.iloc[0]["Sales"] == pytest.approx(30.0)
