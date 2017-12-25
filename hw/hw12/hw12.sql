CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT a.name AS name, b.size AS size 
    FROM dogs AS a, sizes AS b 
    WHERE a.height <= b.max AND a.height > b.min ;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_height AS
  SELECT a.name 
    FROM dogs AS a, dogs AS b, parents AS c 
    WHERE a.name = c.child AND b.name = c.parent 
    ORDER BY b.height DESC;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  WITH 
    siblings(name1,name2) AS (
      SELECT a.name, b.name 
        FROM dogs AS a, dogs AS b, parents AS c, parents AS d 
        WHERE a.name < b.name AND a.name = c.child AND b.name = d.child AND c.parent = d.parent) 
  SELECT a.name1 || " and " || a.name2 || " are " || b.size || " siblings" 
    FROM siblings AS a, size_of_dogs AS b, size_of_dogs AS c 
    WHERE a.name1 = b.name AND a.name2 = c.name AND b.size = c.size 
    ORDER BY b.size;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks AS
  WITH 
    stackhelper(name, height, preheight, n) AS (
      SELECT name, height, height, 1 FROM dogs UNION 
      SELECT b.name || ", " || a.name, a.height+b.height, a.height, b.n+1 
        FROM dogs AS a, stackhelper AS b
        WHERE n<4 AND a.height > b.preheight)
  SELECT name, height 
    FROM stackhelper 
    WHERE n = 4 AND height > 170
    ORDER BY height;
