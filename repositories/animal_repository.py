from db.run_sql import run_sql

from models.animal import Animal

def save(animal):
    sql = "INSERT INTO animals (animal_name) VALUES (%s) RETURNING *"
    values = [animal.animal_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal 

def select_all_animals():
    animals = []
    
    sql = "SELECT * FROM animals"
    results = run_sql(sql)

    for row in results:
        animal = Animal(row['animal_name'], row['id'] )
        animals.append(animal)
    return animals

def select_animal(id):
    animal = None
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        animal = Animal(result['animal_name'], result['id'] )
    return animal 