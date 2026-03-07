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