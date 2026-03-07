from loaddata import load_data
from clean_data import clean_data

def main():
    df = load_data()
    print("Before cleaning:", df.shape)

    cleaned_df = clean_data(df)
    print("After cleaning:", cleaned_df.shape)

    print(cleaned_df.head())

if __name__ == "__main__":
    main()