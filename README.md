# Data Smoke Test Project

This project simulates a common smoke test scenario for data engineering candidates. It involves reading a transactional CSV file, applying data transformations, and loading the results into a PostgreSQL database.

## Features
- Cleans data: removes rows with null 'symbol' and duplicate 'transaction_id'
- Calculates a derived 'total' column based on price and quantity
- Rounds the 'price' field to two decimal places
- Loads the clean data into a PostgreSQL table

## Requirements
- Python 3.7+
- PostgreSQL
- Python packages listed in requirements.txt

## How to Run
1. Create and activate the virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Place your input CSV file in the `data/` directory as `transactions.csv`

4. Run the transformation and load script:

   ```bash
   python scripts/transform.py
   ```

## PostgreSQL Setup (Optional: via Docker)

To spin up a local PostgreSQL instance for testing:

```yaml
version: '3.1'

services:
  postgres:
    image: postgres
    restart: always
    environment:
      POSTGRES_USER: usuario
      POSTGRES_PASSWORD: senha
      POSTGRES_DB: seubanco
    ports:
      - "5432:5432"
```

## Notes
- Adjust the PostgreSQL connection string in `transform.py` as needed.
- This setup is designed for fast testing and demo purposes during interviews or development.