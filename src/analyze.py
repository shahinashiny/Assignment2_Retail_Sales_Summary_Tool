def sales_summary(df):
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    average_sales = df["Sales"].mean()

    print("Total Sales:", total_sales)
    print("Total Profit:", total_profit)
    print("Average Sales:", average_sales)

    return {
        "Total Sales": total_sales,
        "Total Profit": total_profit,
        "Average Sales": average_sales
    }


def top_10_products(df):
    top_products = (
        df.groupby("Product Name")[["Sales"]]
        .sum()
        .reset_index()
        .sort_values(by="Sales", ascending=False)
        .head(10)
    )
    return top_products


def top_10_customers(df):
    top_customers = (
        df.groupby("Customer Name")[["Sales"]]
        .sum()
        .reset_index()
        .sort_values(by="Sales", ascending=False)
        .head(10)
    )
    return top_customers


def top_10_repeated_products(df):
    repeated_products = (
        df["Product Name"]
        .value_counts()
        .reset_index()
    )
    repeated_products.columns = ["Product Name", "Count"]
    return repeated_products.head(10)