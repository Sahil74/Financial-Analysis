CREATE TABLE dim_date AS
SELECT
    date_value::DATE AS date,
    EXTRACT(YEAR FROM date_value)::INT AS year,
    EXTRACT(QUARTER FROM date_value)::INT AS quarter,
    EXTRACT(MONTH FROM date_value)::INT AS month_number,
    TO_CHAR(date_value, 'Mon') AS month_short,
    TO_CHAR(date_value, 'YYYY-MM') AS year_month,
    EXTRACT(DAY FROM date_value)::INT AS day_of_month,
    EXTRACT(ISODOW FROM date_value)::INT AS weekday_number,
    TO_CHAR(date_value, 'Dy') AS weekday_short,
    EXTRACT(ISODOW FROM date_value) >= 6 AS is_weekend,
    DATE_TRUNC('month', date_value)::DATE AS month_start,
    DATE_TRUNC('week', date_value)::DATE AS week_start
FROM GENERATE_SERIES(
    DATE '2024-01-01',
    DATE '2027-12-31',
    INTERVAL '1 day'
) AS date_value;