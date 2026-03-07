# Assignment2_Retail_Sales_Summary_Tool
# Project Overview
This project is a Python-based Retail Sales Summary Tool that analyzes the Superstore sales dataset and generates useful summaries and insights such as sales performance, profit trends, and top products.

# Requirements
- Python 3.10+ (or Python 3.x)
- Recommended packages:
  - pandas
  - numpy (optional)
  - matplotlib (optional for charts)

## How to Run
1. Clone the repository:
   ```bash
   git clone <REPO_URL>
   
2. Go inside the project folder
cd Assignment2_Retail_Sales_Summary_Tool

3. (Optional) Create a virtual environment
python -m venv .venv

4. Install required packages
pip install pandas

5. Run the program
python src/main.py

## Sprint Goal
Deliver a working Python tool that reads the Superstore dataset, processes the sales data, and produces useful summaries such as total sales, profit analysis, and top products.

## User Stories Implementation

### US1 – Load Dataset

#### User Story
As a data analyst,  
I want to load the retail sales dataset  
so that it can be processed and analyzed.

#### Implementation
- Created `loaddata.py` module
- Implemented `load_data()` function
- Loaded the Superstore dataset using pandas
- Ensured the dataset is read correctly from the `data` folder

#### Definition of Done
- Dataset loads successfully using `load_data()`
- DataFrame is returned for further processing
- First rows of data can be displayed for verification


---

### US2 – Clean Dataset

#### User Story
As a data analyst,  
I want to clean the dataset  
so that it is ready for accurate analysis.

#### Implementation
- Created `clean_data.py` module
- Implemented `clean_data()` function
- Converted date columns to datetime format
- Converted numeric fields (Sales, Profit, Quantity, Discount) to numeric types
- Removed rows with missing values in important columns

#### Definition of Done
- Dataset is cleaned successfully
- Data types are corrected
- Missing values in critical columns are handled
- Cleaned dataset is returned for analysis


---

### US3 – Analyze Sales Data

#### User Story
As a data analyst,  
I want to analyze the cleaned retail dataset  
so that I can understand overall sales performance.

#### Implementation
- Created `analyze.py` module
- Implemented `sales_summary()` function
- Calculated:
  - Total Sales
  - Total Profit
  - Average Sales
- Integrated analysis into `main.py`

#### Definition of Done
- Sales summary statistics are calculated correctly
- Program runs successfully from `main.py`
- Results are displayed in the terminal

## Team Members
- Member 1: Shahina Shailk
- Member 2: Simran Kaur
