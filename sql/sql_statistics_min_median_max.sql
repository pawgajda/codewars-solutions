-- Create your SELECT statement here (PostgreSQL 9.6)
SELECT
  MIN(score) AS min,
  PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY score) AS median,
  MAX(score) AS max
FROM result;
