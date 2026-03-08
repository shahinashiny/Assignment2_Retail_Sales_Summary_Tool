import matplotlib.pyplot as plt


def plot_sales_profit_by_category(df):
    category_summary = df.groupby("Category")[["Sales", "Profit"]].sum()

    category_summary.plot(kind="bar", figsize=(8,5))
    plt.title("Sales and Profit by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_top_products(top_products):
    top_products.plot(
        x="Product Name",
        y="Sales",
        kind="bar",
        legend=False,
        figsize=(10,5)
    )

    plt.title("Top 10 Products by Sales")
    plt.xlabel("Product")
    plt.ylabel("Sales")
    plt.xticks(rotation=75)
    plt.tight_layout()
    plt.show()


def plot_top_customers(top_customers):
    top_customers.plot(
        x="Customer Name",
        y="Sales",
        kind="bar",
        legend=False,
        figsize=(10,5)
    )

    plt.title("Top 10 Customers by Sales")
    plt.xlabel("Customer")
    plt.ylabel("Sales")
    plt.xticks(rotation=75)
    plt.tight_layout()
    plt.show()


def plot_repeated_products(repeated_products):
    repeated_products.plot(
        x="Product Name",
        y="Count",
        kind="bar",
        legend=False,
        figsize=(10,5)
    )

    plt.title("Top 10 Repeated Products")
    plt.xlabel("Product")
    plt.ylabel("Frequency")
    plt.xticks(rotation=75)
    plt.tight_layout()
    plt.show()