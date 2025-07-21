/*  SQL  */
SELECT project,
  REGEXP_REPLACE(address, '\d', '', 'g') AS letters,
  REGEXP_REPLACE(address, '[a-zA-Z]', '', 'g') AS numbers
FROM repositories;
