import pandas as pd

def null_transform(df):
    columns_with_null = df.columns[df.isnull().any()]
    for column in columns_with_null:
        if column == 'gender':
            df[column] = df[column].fillna("no gender")
        elif column == 'category':
            df[column] = df[column].fillna("category is not detected")
    return df

def create_full_name(df):
    df['full_name'] = df['first'] + ' ' + df['last']
    return df

def extract_date_info(df):
    df['trans_date_trans_time'] = pd.to_datetime(df['trans_date_trans_time'], dayfirst=True, errors='coerce')
    datetime_cols = df.select_dtypes(include=['datetime', 'datetime64']).columns
    for col in datetime_cols:
        df[f'{col}_year'] = df[col].dt.to_period('Y').astype(str)
        df[f'{col}_month_year'] = df[col].dt.to_period('M').astype(str)
    return df

def main_transform(df):
    df = null_transform(df)
    df = create_full_name(df)
    df = extract_date_info(df)
    return df