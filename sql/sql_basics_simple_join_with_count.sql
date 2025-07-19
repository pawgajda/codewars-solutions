-- Create your SELECT statement here
SELECT p.id,
  p.name,
  COUNT(t.name) AS toy_count
FROM people as p
JOIN toys as t ON p.id = t.people_id
GROUP BY p.id;
