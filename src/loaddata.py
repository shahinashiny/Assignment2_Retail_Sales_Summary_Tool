import pandas as pd

def load_data():
    df = pd.read_csv("data/superstore.xls", sep=",", engine="python")
    df.columns = df.columns.str.strip()
    return df


if __name__ == "__main__":
    data = load_data()
    print(data.head())
    print(data.columns)