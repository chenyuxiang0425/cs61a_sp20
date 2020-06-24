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

-- copy your solution from prev hw!
-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT a.name as name,b.size as size from dogs as a, sizes as b where a.height > b.min and a.height <= b.max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT a.child from parents as a, dogs as b where a.parent = b.name order by height DESC;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.child as first, b.child as second from parents as a, parents as b where a.parent = b.parent and a.child < b.child;

-- Sentences about siblings that are the same size
CREATE TABLE siblings_have_same_size AS
  SELECT a.first as first, a.second as second, b.size as size
  from siblings as a, size_of_dogs as b, size_of_dogs as c
  where a.first = b.name and a.second = c.name and b.size = c.size;

CREATE TABLE sentences AS
  SELECT first || ' and ' || second || ' are ' || size || ' siblings' from siblings_have_same_size;