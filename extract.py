import pandas as pd

def extract_csv(csv_name):
    csv_df = pd.read_csv(csv_name,nrows=25000)               
    return csv_df

if __name__ == '__main__':
    extract_csv("credit_card_transactions.csv")