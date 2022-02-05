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


    