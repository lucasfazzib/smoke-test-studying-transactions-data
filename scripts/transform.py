import pandas as pd
from sqlalchemy import create_engine
import os

def transform_and_load(csv_path, db_url, table_name):
    # READ
    df = pd.read_csv(csv_path)

    # CLEAN
    df = df.dropna(subset=['symbol'])
    df = df.drop_duplicates(subset=['transaction_id'])
    df['price'] = df['price'].round(2)
    df['total'] = df['price'] * df['quantity']

    # CONNECTION PostgreSQL
    engine = create_engine(db_url)

    # load
    df.to_sql(table_name, engine, index=False, if_exists='replace')

    print(f"Dados carregados na tabela '{table_name}' com sucesso!")

if __name__ == "__main__":
    csv_path = os.path.join("..", "data", "transactions.csv")
    db_url = "postgresql://usuario:senha@localhost:5432/seubanco"
    table_name = "transactions_clean"

    transform_and_load(csv_path, db_url, table_name)
    ##