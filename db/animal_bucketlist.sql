DROP TABLE IF EXISTS breeds;
DROP TABLE IF EXISTS animals;


CREATE TABLE animals (
  id SERIAL PRIMARY KEY,
  animal_name VARCHAR(255)
);

CREATE TABLE breeds (
  id SERIAL PRIMARY KEY,
  breed_kind VARCHAR(255),
  breed_seen BOOLEAN,
  animal_id INT REFERENCES animals(id) 
);

