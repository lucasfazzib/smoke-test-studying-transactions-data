import pandas as pd
import numpy as np


n = 1_000_000
df = pd.DataFrame({
    'transaction_id': np.arange(n),
    'symbol': np.random.choice(['AAPL', 'GOOG', 'TSLA', 'MSFT'], size=n),
    'price': np.random.uniform(100, 500, size=n),
    'quantity': np.random.randint(1, 100, size=n),
    'timestamp': pd.date_range('2025-01-01', periods=n, freq='s')
})

# Introduz duplicatas e nulos
df.loc[::50000, 'symbol'] = None
df = pd.concat([df, df.iloc[:1000]])  # geranerate duplicates

df.to_csv('transactions.csv', index=False)
