
# ETL Process for Credit Card Transactions

This project is an ETL pipeline designed to extract, transform, and load data from a CSV file of credit card transactions. The data is cleaned, transformed, and then saved in various formats, such as JSON, Excel, CSV, or a database. Additionally, the program can generate visualizations to analyze fraud data.

## Files Included:
- `data_observation_verification.py`: Quick observation of the dataset before starting.
- `extract.py`: Extracts data from a CSV file.
- `transform.py`: Transforms the data by handling missing values, creating a full name column, and extracting date-related information.
- `load.py`: Loads the transformed data into different formats (JSON, Excel, CSV, or SQLite database).
- `main.py`: Main script to orchestrate the ETL process and optionally generate fraud-related visualizations.
- `requirements.txt`: List of required Python packages for the project.

## Requirements

You need to install the following Python libraries to run this project:

```bash
pip install -r requirements.txt
```

This will install the necessary dependencies like `pandas`, `matplotlib`, `openpyxl`, and others for handling data and visualizations.

## ETL Process

The ETL process consists of the following steps:

### 1. Extract
- The `extract.py` file extracts the data from the `credit_card_transactions.csv` file. 
- It reads the first 25,000 rows of the CSV file into a Pandas DataFrame.

### 2. Transform
- The `transform.py` file processes the data in the following ways:
  - **Handling Missing Values**: Fills missing values in the `gender` and `category` columns.
  - **Creating Full Name**: Combines the `first` and `last` columns to create a `full_name` column.
  - **Date Extraction**: Extracts year and month-year information from the `trans_date_trans_time` column.

### 3. Load
- The `load.py` file allows the transformed data to be saved in one of the following formats:
  - **JSON**: Saved as `credit_card_transactions_clean_dataset.json`
  - **Excel**: Saved as `credit_card_transactions_clean_dataset.xlsx`
  - **CSV**: Saved as `credit_card_transactions_clean_dataset.csv`
  - **SQLite Database**: Saved into an SQLite database (table: `credit_card_transactions_clean_dataset`)

## How to Run

To run the script and load data into a chosen format, use the following command:

```bash
python main.py <load_type>
```

Where `<load_type>` can be one of the following:
- `json` — Save the cleaned data as a JSON file.
- `excel` — Save the cleaned data as an Excel file.
- `csv` — Save the cleaned data as a CSV file.
- `db` — Save the cleaned data into an SQLite database.

### Example:

```bash
python main.py json
```

This will extract the data, apply the transformations, and save the results in `credit_card_transactions_clean_dataset.json`.

### Plotting Fraud Data

You can also generate visualizations related to fraud data by using the following options:

#### Top 10 Cities with Highest Fraud:
To plot the top 10 cities with the highest fraud cases (where `is_fraud == 1`), add the `--plot_fraud_cities` argument:

```bash
python main.py json --plot_fraud_cities
```

#### Top 5 Months with Highest Fraud:
To plot the top 5 months with the highest fraud cases (based on the `trans_date_trans_time_month_year` column and `is_fraud == 1`), add the `--plot_fraud_months` argument:

```bash
python main.py json --plot_fraud_months
```

### Example: Run both Plots

You can run the script with both plotting options to generate both plots:

```bash
python main.py json --plot_fraud_cities --plot_fraud_months
```

This will save the cleaned data in the specified format (`json` in this case) and show two plots:
- Top 10 cities with the highest fraud.
- Top 5 months with the highest fraud.

## Notes

- The `main.py` script uses `matplotlib` to generate bar charts for fraud-related visualizations.
- Ensure that the CSV file `credit_card_transactions.csv` is in the same directory as the script, or adjust the file path in the code.
