import pandas as pd
import os

def transform_and_save(csv_path, output_dir):
    # READ
    df = pd.read_csv(csv_path)

    # chunks = pd.read_csv(csv_path, chunksize=500_000)
    # dfs = []

    # for chunk in chunks:
    #     chunk = chunk.dropna(subset=['symbol'])
    #     chunk = chunk.drop_duplicates(subset=['transaction_id'])
    #     chunk['price'] = chunk['price'].round(2)
    #     chunk['total'] = chunk['price'] * chunk['quantity']
    #     dfs.append(chunk)

    # df_final = pd.concat(dfs, ignore_index=True)

    # df = pd.read_csv(csv_path, encoding='utf-8', errors='replace')

    # required_columns = ['transaction_id', 'symbol', 'price', 'quantity', 'timestamp']
    # missing = [col for col in required_columns if col not in df.columns]

    # if missing:
    #     raise ValueError(f"Missing required columns: {missing}")

    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    # Renomear colunas com espaços ou má formatação
    # df.columns = df.columns.str.strip().str.lower()

    # CLEAN
    df = df.dropna(subset=['symbol'])
    df = df.drop_duplicates(subset=['transaction_id'])
    df['symbol'] = df['symbol'].str.upper().str.strip()
    df['price'] = df['price'].round(2)
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df = df.dropna(subset=['timestamp'])
    df = df[(df['price'] > 0) & (df['quantity'] > 0)]

    # FEATURE ENGINEERING
    df['total'] = df['price'] * df['quantity']
    df['value_level'] = pd.cut(df['total'], bins=[0, 1000, 5000, float('inf')],
                               labels=['low', 'medium', 'high'])

    # SAVE CLEANED
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(os.path.join(output_dir, "transactions_clean.csv"), index=False)

    # SAVE SUMMARY
    summary = df.groupby('symbol').agg({
        'total': 'sum',
        'transaction_id': 'count'
    }).rename(columns={'transaction_id': 'transaction_count'}).reset_index()

    summary.to_csv(os.path.join(output_dir, "transactions_summary.csv"), index=False)

    print("Arquivos CSV gerados com sucesso.")

if __name__ == "__main__":
    csv_path = os.path.join("..", "data", "transactions.csv")
    output_dir = os.path.join("..", "output")

    transform_and_save(csv_path, output_dir)
