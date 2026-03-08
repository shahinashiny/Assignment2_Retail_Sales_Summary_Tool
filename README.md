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

## US1 – Load Dataset
User Story

As a data analyst,
I want to load the retail sales dataset
so that it can be processed and analyzed.

Story Point Estimation

UX: 1
Design: 0
Front: 1
Back: 2
Total: 4

Implementation

Created loaddata.py module

Implemented load_data() function

Loaded the Superstore dataset using pandas

Ensured the dataset is read correctly from the data folder

Definition of Done

Dataset loads successfully using load_data()

DataFrame is returned for further processing

First rows of data can be displayed for verification

## US2 – Clean Dataset
User Story

As a user,
I want the tool to clean the dataset (missing values/format issues)
so that the analysis is accurate.

Story Point Estimation

UX: 1
Design: 0
Front: 2
Back: 4
Total: 7

Implementation

Implemented data cleaning functions

Handled missing values

Converted date columns to correct format

Converted numeric columns correctly

Definition of Done

Clean dataset prepared for analysis

Dataset validated after cleaning

Code committed to GitHub

## US3 – Generate Total Sales and Profit Summary
User Story

As a user,
I want to see total sales and total profit summaries
so that I understand business performance.

Story Point Estimation

UX: 1
Design: 1
Front: 2
Back: 3
Total: 7

Implementation

Implemented function to calculate total sales

Implemented function to calculate total profit

Displayed summary results clearly

Definition of Done

Sales and profit totals calculated correctly

Results verified using dataset

Code pushed to GitHub

## US4 – Analyze Sales and Profit by Category
User Story

As a user,
I want sales and profit breakdown by category and sub-category
so that I know which products perform best.

Story Point Estimation

UX: 1
Design: 1
Front: 2
Back: 4
Total: 8

Implementation

Implemented category analysis

Grouped data by category and sub-category

Calculated sales and profit values

Definition of Done

Category analysis results generated

Results verified using dataset

Code committed to GitHub

## US5 – Identify Top Products and Customers
User Story

As a user,
I want to view top 10 products, repeated products, and customers by sales
so that I can identify key contributors.

Story Point Estimation

UX: 1
Design: 1
Front: 3
Back: 4
Total: 9

Implementation

Calculated top 10 products by sales

Calculated top 10 customers by sales

Identified repeated products

Sorted results by sales value

Definition of Done

Top products and customers calculated correctly

Output verified

Code committed to GitHub
## Team Members
- Member 1: Shahina Shailk
- Member 2: Simran Kaur
