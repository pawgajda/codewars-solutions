SELECT 
  DATE(s.transaction_date) as day,
  d.name AS department,
  COUNT(s.id) AS sale_count
  FROM department d
    JOIN sale s on d.id = s.department_id
  GROUP BY day, d.name
  ORDER BY day ASC;
