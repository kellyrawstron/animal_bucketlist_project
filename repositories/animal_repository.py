from db.run_sql import run_sql

from models.animal import Animal
from models.breed import Breed

def save(animal):
    sql = "INSERT INTO animals (animal_name) VALUES (%s) RETURNING *"
    values = [animal.animal_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal 

def select_all():
    animals = []
    
    sql = "SELECT * FROM animals"
    results = run_sql(sql)

    for row in results:
        animal = Animal(row['animal_name'], row['id'] )
        animals.append(animal)
    return animals

def select(id):
    animal = None
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        animal = Animal(result['animal_name'], result['id'] )
    return animal 





def delete_all():
    sql = "DELETE  FROM animals"
    run_sql(sql)
    
def delete(id):
    sql = "DELETE  FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
    
def update(animal):
    sql = "UPDATE animals SET (animal_name) = (%s) WHERE id = %s"
    values = [animal.animal_name, animal.id]
    run_sql(sql, values)
    
    
def breeds(animal):
    breeds = []
    
    sql = "SELECT * FROM breeds WHERE animal_id = %s"
    values = [animal.id]
    results = run_sql(sql, values)
    
    for row in results:
        breed = Breed(row['breed_kind'], row['animal_id'], row['breed_seen'], row['id'])
        breeds.append(breed)
    return breeds 