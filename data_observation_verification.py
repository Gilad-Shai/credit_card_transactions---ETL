from extract import extract_csv

df = extract_csv("credit_card_transactions.csv")

def shape():
    print(df.shape)

def info():
    print(df.info())

def describe():
    print(df.describe())

def total_null_values():
    print(df.isnull().sum())

def duplicates_check():
    print(df.duplicated().sum())

def unique_value():
    for column in df.columns:
        print(df[column].unique())

def count_value():
    for column in df.columns:
        print(df[column].value_counts())

