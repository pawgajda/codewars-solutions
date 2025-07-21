SELECT 
  j.job_title,
  CAST(
    ROUND(
      CAST(
        AVG(j.salary) AS NUMERIC
      ), 2
    ) AS DOUBLE PRECISION
  ) AS average_salary,
  COUNT(p.id) AS total_people,
  CAST(
    ROUND(
      CAST(
        SUM(j.salary) AS NUMERIC
      ), 2
    ) AS DOUBLE PRECISION
  ) AS total_salary
  FROM people p
  JOIN job j ON p.id = j.people_id
  GROUP BY j.job_title
  ORDER BY average_salary DESC;
