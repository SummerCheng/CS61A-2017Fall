CREATE TABLE pairs AS
  with digit(num) 
  	as (select a.d* 10 + b.d 
  		from (select 0 as d union select 1 union select 2 union select 3 union select 4) as a, (select 1 as d union select 2 union select 3 union select 4 union select 5 union select 6 union select 7 union select 8 union select 9 union select 0) as b)
  SELECT a.num as x,b.num as y
  	FROM digit as a, digit as b
  	where a.num <= b.num and b.num <= 42


