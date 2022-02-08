import pdb

from models.breed import Breed
from models.animal import Animal


import repositories.breed_repository as breed_repository
import repositories.animal_repository as animal_repository

breed_repository.delete_all()
animal_repository.delete_all()



animal1 = Animal('Dog')
animal_repository.save(animal1)

animal2 = Animal('Cat')
animal_repository.save(animal2)

animal3 = Animal('Bird')
animal_repository.save(animal3)

animal4 = Animal('Fish')
animal_repository.save(animal4)

animal5 = Animal('Rabbit')
animal_repository.save(animal5)

animal_repository.select_all()











pdb.set_trace()

