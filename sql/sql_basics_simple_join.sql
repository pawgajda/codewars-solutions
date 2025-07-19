SELECT p.id,
  p.name,
  p.isbn,
  p.company_id,
  p.price,
  c.name AS company_name
FROM products AS p
JOIN companies AS c ON p.company_id = c.id;
