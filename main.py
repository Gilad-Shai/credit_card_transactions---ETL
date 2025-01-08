from extract import extract_csv
from transform import main_transform
from load import main_load
import argparse
import matplotlib.pyplot as plt

def plot_top_fraud_cities(df):
    fraud_df = df[df['is_fraud'] == 1]
    top_fraud_cities = fraud_df['city'].value_counts().head(10)

    plt.figure(figsize=(10, 6))
    top_fraud_cities.plot(kind='bar', color='salmon')
    plt.title("Top 10 Cities with Highest Fraud")
    plt.xlabel("City")
    plt.ylabel("Number of Fraud Cases")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def plot_top_fraud_months(df):
    fraud_df = df[df['is_fraud'] == 1]
    top_fraud_months = fraud_df['trans_date_trans_time_month_year'].value_counts().head(5)

    plt.figure(figsize=(10, 6))
    top_fraud_months.plot(kind='bar', color='lightblue')
    plt.title("Top 5 Months with Highest Fraud")
    plt.xlabel("Month-Year")
    plt.ylabel("Number of Fraud Cases")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="Load DataFrame into specified format and optionally plot fraud data")
    parser.add_argument('load_type', choices=['json', 'excel', 'csv', 'db'],
                        help="Specify the format to load the DataFrame into: json, excel, csv, or db")
    parser.add_argument('--plot_fraud_cities', action='store_true',
                        help="Plot the top 10 cities with the highest fraud cases")
    parser.add_argument('--plot_fraud_months', action='store_true',
                        help="Plot the top 5 months with the highest fraud cases")
    args = parser.parse_args()
    
    print(f"Load type chosen: {args.load_type}")
        
    df = extract_csv("credit_card_transactions.csv")
    main_transform(df)
   
    main_load(df, args.load_type)

    if args.plot_fraud_cities:
        plot_top_fraud_cities(df)

    if args.plot_fraud_months:
        plot_top_fraud_months(df)

if __name__ == '__main__':
    main()