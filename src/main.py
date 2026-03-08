from loaddata import load_data
from clean_data import clean_data
from analyze import (
    sales_summary,
    top_10_products,
    top_10_customers,
    top_10_repeated_products
)

from visualize import (
    plot_sales_profit_by_category,
    plot_top_products,
    plot_top_customers,
    plot_repeated_products
)


def main():
    df = load_data()
    cleaned_df = clean_data(df)

    print("\n===== SUMMARY STATISTICS =====")
    sales_summary(cleaned_df)

    print("\n===== TOP 10 PRODUCTS BY SALES =====")
    top_products = top_10_products(cleaned_df)
    print(top_products)

    print("\n===== TOP 10 CUSTOMERS BY SALES =====")
    top_customers = top_10_customers(cleaned_df)
    print(top_customers)

    print("\n===== TOP 10 REPEATED PRODUCTS =====")
    repeated_products = top_10_repeated_products(cleaned_df)
    print(repeated_products)

    # Visualizations
    plot_sales_profit_by_category(cleaned_df)
    plot_top_products(top_products)
    plot_top_customers(top_customers)
    plot_repeated_products(repeated_products)


if __name__ == "__main__":
    main()