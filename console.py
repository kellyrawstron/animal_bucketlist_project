import pdb

from models.type import Type
from models.animal import Animal

import repositories.type_repository as type_repository
import repositories.animal_repository as animal_repository

type_repository.delete_all_types()
animal_repository.delete_all_animals()



animal1 = Animal('Dog')
animal_repository.save(animal1)



type1 = Type("Alaskan Malamute", animal1, True)
type_repository.save(type1)

result = type_repository.select_all_types()

for type in result:
    print(type.__dict__)





pdb.set_trace()

