from db.run_sql import run_sql

from models.animal import Animal
from models.type import Type

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

def update_animal(animal):
    sql = "UPDATE animals SET (animal_name) = (%s) WHERE id = %s"
    values = [animal.animal_name]
    run_sql(sql, values)




def delete_all_animals():
    sql = "DELETE  FROM animals"
    run_sql(sql)
    
def delete_animal_id(id):
    sql = "DELETE  FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
    
def types(animal):
    types = []
    
    sql = "SELECT * FROM types WHERE animal_id = %s"
    values = [animal.id]
    results = run_sql(sql, values)
    
    for row in results:
        type = Type(row['animal_name'], animal, row['type_seen'], row['id'])
        types.append(type)
    return types 