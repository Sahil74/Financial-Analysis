select 
    (SELECT COUNT(*) FROM transactions_first) as first_count,
    (SELECT COUNT(*) FROM transactions_second) as second_count;

--Duplicates
SELECT transaction_id, count(*) AS countn from transactions_second group by transaction_id HAVING Count(*) > 1;

-- missing
SELECT COUNT(*) AS missing_values from transactions_second s LEFT JOIN transactions_first f ON s.account_number = f.account_number WHERE f.account_number IS NULL;
