import pdb

from models.animal_type import AnimalType
from models.animal import Animal


import repositories.animal_type_repository as animal_type_repository
import repositories.animal_repository as animal_repository

animal_type_repository.delete_all()
animal_repository.delete_all()



animal_type_1 = AnimalType('Dog')
animal_type_repository.save(animal_type_1)

animal_type_2 = AnimalType('Cat')
animal_type_repository.save(animal_type_2)

animal_type_3 = AnimalType('Bird')
animal_type_repository.save(animal_type_3)

animal_type_4 = AnimalType('Fish')
animal_type_repository.save(animal_type_4)

animal_type_5 = AnimalType('Rabbit')
animal_type_repository.save(animal_type_5)

animal_type_repository.select_all()

animal1 = Animal('Goose', 'Alaskan Malamute', animal_type_1)
animal_repository.save(animal1)

animal2 = Animal('panir', 'Mixed Breed', animal_type_1)
animal_repository.save(animal2)









pdb.set_trace()

