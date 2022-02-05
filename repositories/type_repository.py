from db.run_sql import run_sql

from models.type import Type
from models.animal import Animal
import repositories.animal_repository as animal_repository

def save(type):
    sql = "INSERT INTO types (animal_type, animal_id, type_seen) VALUES (%s, %s, %s) RETURNING *"
    values = [type.animal_type, type.animal.id, type.type_seen]
    results = run_sql(sql, values)
    id = results[0]['id']
    type.id = id
    return type 


def select_all_types():
    types = []
    
    sql = "SELECT * FROM types"
    results = run_sql(sql)

    for row in results:
        animal = animal_repository.select_all_animals(row['animal_id'])
        type = Type(row['animal_type'], animal, row['type_seen'], row['id'] )
        types.append(type)
    return types

def select_type(id):
    type = None
    sql = "SELECT * FROM types WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        animal = animal_repository.select_animal(result['animal_id'])
        type = Type(result['animal_type'], animal, result['type_seen'], result['id'] )
        
    return type


def update_type(type):
    sql = "UPDATE types SET (animal_type, animal_id, type_seen) = (%s, %s, %s) WHERE id = %s"
    values = [type.animal_type, type.animal_id, type.type_seen, type.id]
    run_sql(sql, values)



def delete_all_types():
    sql = "DELETE  FROM types"
    run_sql(sql)
    
def delete_type(id):
    sql = "DELETE  FROM types WHERE id = %s"
    values = [id]
    run_sql(sql, values)


    