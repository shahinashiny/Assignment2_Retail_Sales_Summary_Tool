import pandas as pd

def load_data():
    """
    Load the Superstore dataset
    """
    df = pd.read_csv("data/superstore.csv", encoding="latin-1")
    return df


if __name__ == "__main__":
    data = load_data()
    print(data.head())