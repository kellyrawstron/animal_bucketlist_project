import pdb

from models.breed import Breed
from models.animal import Animal


import repositories.animal_repository as animal_repository


animal_repository.delete_all()



animal1 = Animal('Dog')
animal_repository.save(animal1)

animal2 = Animal('Cat')
animal_repository.save(animal2)

animal3 = Animal('Bird')
animal_repository.save(animal3)

animal_repository.select_all()








pdb.set_trace()

