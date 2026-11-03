from connection import get_connection
conn = get_connection()

def execute(query):
    try:
        with conn:
            conn.execute(query)
            print("done")
    finally:
        conn.close()


Query = """
create table fact_scenarios AS WITH main AS 
(
    SELECT
        DATE_TRUNC('month', TO_DATE(transaction_date, 'DD.MM.YYYY')) AS transaction_month,
        store_code,
        account_number,
        SUM(amount_local) AS amount_local
    FROM fact_transactions
    GROUP BY
        transaction_month,
        store_code,
        account_number
)

SELECT
    transaction_month,
    store_code,
    account_number,
    'Actual' AS Scenario,
    amount_local AS amount_local
FROM main

UNION ALL

SELECT
    transaction_month,
    store_code,
    account_number,
    'BestCase' AS Scenario,
    CASE
        WHEN amount_local >= 0 THEN amount_local * 1.10
        ELSE amount_local * 0.90
    END AS amount_local
FROM main

UNION ALL

SELECT
    transaction_month,
    store_code,
    account_number,
    'WorstCase' AS Scenario,
    CASE
        WHEN amount_local >= 0 THEN amount_local * 0.90
        ELSE amount_local * 1.10
    END AS amount_local
FROM main

ORDER BY
    transaction_month,
    store_code,
    account_number,
    Scenario;
"""
execute(Query)