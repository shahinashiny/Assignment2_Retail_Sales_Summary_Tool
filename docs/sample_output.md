# Sample output

This sample is based on the checked-in `data/superstore.csv` and the cleaning rules in `src/clean_data.py`. Monetary values below are rounded to two decimal places for readability. Recalculate these figures after changing the source data or transformation logic.

## Summary statistics

```text
===== SUMMARY STATISTICS =====
Total Sales: 2242104.82
Total Profit: 278000.04
Average Sales: 229.44
```

The cleaning pipeline retains **9,772 rows** with valid numeric `Sales` and `Profit` values from the input file.

## Top products by sales

| Product | Sales |
|---|---:|
| Canon imageCLASS 2200 Advanced Copier | 51,099.85 |
| Fellowes PB500 Electric Punch Plastic Comb Binding Machine with Manual Bind | 27,453.38 |
| Cisco TelePresence System EX90 Videoconferencing Unit | 22,638.48 |
| HON 5400 Series Task Chairs for Big and Tall | 21,870.58 |
| GBC DocuBind TL300 Electric Binding System | 19,823.48 |

## Sales and profit by category

| Category | Sales | Profit |
|---|---:|---:|
| Furniture | 724,997.53 | 17,396.15 |
| Office Supplies | 701,083.11 | 120,217.30 |
| Technology | 816,024.18 | 140,386.59 |

## Charts created by the script

When you run `python src/main.py`, the script opens charts for:

1. Sales and profit by category.
2. Top 10 products by sales.
3. Top 10 customers by sales.
4. Top 10 repeated products by frequency.

The project displays these charts using Matplotlib; it does not currently save them as image files automatically.
