DROP TABLE IF EXISTS types;
DROP TABLE IF EXISTS animals;

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    animal_name VARCHAR(255)
);

CREATE TABLE types (
    id SERIAL PRIMARY KEY,
    animal_type VARCHAR(255),
    type_seen BOOLEAN,
    animal_id INT REFERENCES animals(id)
);

