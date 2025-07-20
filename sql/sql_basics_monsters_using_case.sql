/*  SQL  */
SELECT t.id,
  t.heads,
  t.arms,
  b.legs,
  b.tails,
  CASE
    WHEN t.heads > t.arms AND b.tails > b.legs THEN 'BEAST'
    WHEN t.heads > t.arms THEN 'BEAST'
    WHEN b.tails > b.legs THEN 'BEAST'
    ELSE 'WEIRDO'
  END AS species
FROM top_half AS t
JOIN bottom_half AS b
  ON t.id = b.id
ORDER BY species;
