from sqlalchemy import create_engine

def main_load(df, load_type):

    def json_load():
        try:
            json_df = df.to_json("credit_card_transactions_clean_dataset.json", orient='records', indent=4)
            print("DataFrame loaded into JSON format.")
        except Exception as e:
            print(f"Error occurred while saving JSON: {e}")
    
    def excel_load():    
        excel_df = df.to_excel("credit_card_transactions_clean_dataset.xlsx",index=False)
        print("DataFrame loaded into Excel format.")
    
    def csv_load():
        csv_df = df.to_csv("credit_card_transactions_clean_dataset.csv",index=False)
        print("DataFrame loaded into CSV format.")
    
    def sqllite():
        engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
        print(f'created an engine to use with in-memory SQLite database: {engine}')
        return engine

    def db_load():
        sql_df = df.to_sql("credit_card_transactions_clean_dataset", sqllite(), if_exists="replace", index=False)
        print("DataFrame loaded into SQLite database.")
    

    if load_type == 'json':
        return json_load()
    elif load_type == 'excel':
        return excel_load()
    elif load_type == 'csv':
        return csv_load()
    elif load_type == 'db':
       return  db_load()
    else:
        print("Invalid load type specified. Please choose from 'json', 'excel', 'csv', or 'db'.")