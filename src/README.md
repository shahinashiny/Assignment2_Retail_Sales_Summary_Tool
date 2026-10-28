# Source modules

- `main.py`: orchestrates loading, cleaning, analysis, and charts.
- `loaddata.py`: reads `data/superstore.csv` using a path anchored to the project, not the caller's working directory.
- `clean_data.py`: normalizes whitespace, parses date columns, converts numeric fields, and removes rows with invalid `Sales` or `Profit`.
- `analyze.py`: calculates summary metrics and ranks products/customers.
- `visualize.py`: plots category, product, customer, and repeat-product summaries.
