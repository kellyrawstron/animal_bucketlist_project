from db.run_sql import run_sql

from models.animal import Animal
from repositories import animal_type_repository


def save(animal):
    sql = "INSERT INTO animals (name, breed, seen, animal_type_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.breed, animal.seen, animal.animal_type.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal 

def select_all():
    animals = []
    
    sql = "SELECT * FROM animals"
    results = run_sql(sql)

    for row in results:
        animal_type = animal_type_repository.select(row['animal_type_id'])
        animal = Animal(row['name'], row['breed'], animal_type, row['seen'] ,row['id'] )
        animals.append(animal)
    return animals

def select(id):
    animal = None
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        animal_type = animal_type_repository.select(result['animal_type_id'])
        animal = Animal(result['name'], result['breed'], animal_type, result['seen'], result['id'] )
    return animal 





def delete_all():
    sql = "DELETE  FROM animals"
    run_sql(sql)
    
def delete(id):
    sql = "DELETE  FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
    
def update(animal):
    sql = "UPDATE animals SET (name, breed, animal_type_id, seen) = (%s, %s, %s, %s) WHERE id = %s"
    values = [animal.name, animal.breed, animal.animal_type.id, animal.seen,animal.id]
    run_sql(sql, values)
    
    
# def breeds(animal):
#     breeds = []
    
#     sql = "SELECT * FROM breeds WHERE animal_id = %s"
#     values = [animal.id]
#     results = run_sql(sql, values)
    
#     for row in results:
#         breed = Breed(row['breed_kind'], row['animal_id'], row['breed_seen'], row['id'])
#         breeds.append(breed)
#     return breeds 
def select_not_seen():
    sql = "SELECT * FROM animals WHERE seen = 'f'"
    results = run_sql(sql)
    
    animals = []

    for row in results:
        animal_type = animal_type_repository.select(row['animal_type_id'])
        animal = Animal(row['name'], row['breed'], animal_type, row['seen'] ,row['id'] )
        animals.append(animal)
    return animals

def select_seen():
    sql = "SELECT * FROM animals WHERE seen = 't'"
    results = run_sql(sql)
    
    animals = []

    for row in results:
        animal_type = animal_type_repository.select(row['animal_type_id'])
        animal = Animal(row['name'], row['breed'], animal_type, row['seen'] ,row['id'] )
        animals.append(animal)
    return animals