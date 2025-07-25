/*  SQL  */
SELECT
  CASE
    WHEN SUM(number1) % 2 != 0 THEN MIN(number1)
    ELSE MAX(number1)
  END AS number1,
  CASE
    WHEN SUM(number2) % 2 != 0 THEN min(number2)
    ELSE MAX(number2)
  END AS number2
FROM numbers;
