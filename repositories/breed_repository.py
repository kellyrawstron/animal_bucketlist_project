from db.run_sql import run_sql

from models.breed import Breed
from models.animal import Animal
import repositories.animal_repository as animal_repository

def save(breed):
    sql = "INSERT INTO breeds (breed_kind, animal_id, breed_seen) VALUES (%s, %s, %s) RETURNING *"
    values = [breed.breed_kind, breed.animal.id, breed.breed_seen]
    results = run_sql(sql, values)
    id = results[0]['id']
    breed.id = id
    return breed 


def select_all():
    breeds = []
    
    sql = "SELECT * FROM breeds"
    results = run_sql(sql)

    for row in results:
        animal = animal_repository.select(row['animal_id'])
        breed = Breed(row['breed_kind'], animal, row['breed_seen'], row['id'] )
        breeds.append(breed)
    return breeds

def select(id):
    breed = None
    sql = "SELECT * FROM breeds WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        animal = animal_repository.select(result['animal_id'])
        breed = Breed(result['breed_kind'], animal, result['breed_seen'], result['id'] )
        
    return breed




def delete_all():
    sql = "DELETE  FROM breeds"
    run_sql(sql)
    
def delete(id):
    sql = "DELETE  FROM breeds WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
    
def update(breed):
    sql = "UPDATE breeds SET (breed_kind, animal_id, breed_seen) = (%s, %s, %s) WHERE id = %s"
    values = [breed.breed_kind, breed.animal_id, breed.breed_seen, breed.id]
    run_sql(sql, values)
    
    



    