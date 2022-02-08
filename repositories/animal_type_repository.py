from db.run_sql import run_sql

from models.animal_type import AnimalType


def save(animal_type):
    sql = "INSERT INTO animal_types (name) VALUES (%s) RETURNING *"
    values = [animal_type.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal_type.id = id
    return animal_type


def select_all():
    animal_types = []
    
    sql = "SELECT * FROM animal_types"
    results = run_sql(sql)

    for row in results:
        animal_type = AnimalType(row['name'], row['id'] )
        animal_types.append(animal_type)
    return animal_types

def select(id):
    animal_type = None
    sql = "SELECT * FROM animal_types WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        animal_type = AnimalType(result['name'], result['id'] )
        
    return animal_type




def delete_all():
    sql = "DELETE  FROM animal_types"
    run_sql(sql)
    
def delete(id):
    sql = "DELETE  FROM animal_types WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
    
def update(animal_type):
    sql = "UPDATE animal_types SET name = %s WHERE id = %s"
    values = [animal_type.name, animal_type.id]
    run_sql(sql, values)
    
    



    