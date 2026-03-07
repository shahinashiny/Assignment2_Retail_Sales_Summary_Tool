from loaddata import load_data
from clean_data import clean_data
from analyze import sales_summary

def main():
    df = load_data()
    print("Before cleaning:", df.shape)

    cleaned_df = clean_data(df)
    print("After cleaning:", cleaned_df.shape)

    print("\nColumns:")
    print(cleaned_df.columns)

    print("\nSales Summary")
    sales_summary(cleaned_df)

if __name__ == "__main__":
    main()