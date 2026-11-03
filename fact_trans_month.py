from connection import get_connection
conn = get_connection()

def execute(query):
    try:
        with conn:
            conn.execute(query)
            print("done")
    finally:
        conn.close()



Query = """CREATE TABLE fact_trans_month AS
    WITH main AS (
        SELECT
            TO_DATE(transaction_date, 'DD.MM.YYYY') AS transaction_date,
            store_code,
            account_number,
            amount_local
        FROM fact_transactions
    )
    SELECT
        DATE_TRUNC('month', transaction_date) AS transaction_month,
        store_code,
        account_number,
        SUM(amount_local) AS amount_local
    FROM main
    GROUP BY
        transaction_month,
        store_code,
        account_number
    ORDER BY
        transaction_month,
        store_code,
        account_number;
"""

execute(Query)
