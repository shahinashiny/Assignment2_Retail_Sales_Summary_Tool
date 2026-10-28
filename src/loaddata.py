from pathlib import Path
from typing import Union

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DATA_PATH = PROJECT_ROOT / "data" / "superstore.csv"


def load_data(path: Union[str, Path, None] = None) -> pd.DataFrame:
    """Load the Superstore CSV, independent of the caller's working directory."""
    data_path = Path(path).expanduser() if path is not None else DEFAULT_DATA_PATH
    if not data_path.is_absolute():
        data_path = (Path.cwd() / data_path).resolve()

    if not data_path.is_file():
        raise FileNotFoundError(
            f"Dataset not found at: {data_path}. "
            "Expected the file data/superstore.csv in the project."
        )

    df = pd.read_csv(data_path)
    df.columns = df.columns.str.replace('"', "", regex=False).str.strip()

    if df.empty:
        raise ValueError(f"The dataset is empty: {data_path}")

    return df


if __name__ == "__main__":
    data = load_data()
    print(data.head())
    print("Rows:", len(data))
    print("Columns:", list(data.columns))
