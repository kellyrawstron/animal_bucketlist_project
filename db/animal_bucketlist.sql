DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS animal_types;


CREATE TABLE animal_types (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE animals (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  breed VARCHAR(255),
  seen BOOLEAN,
  animal_type_id INT REFERENCES animal_types(id) ON DELETE CASCADE
);



