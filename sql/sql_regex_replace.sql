/*  SQL  */
SELECT project,
  commits,
  contributors,
  REGEXP_REPLACE(address, '\d', '!', 'g') AS address
FROM repositories;
