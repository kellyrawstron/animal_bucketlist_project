import pdb
from models.animal import Animal

import repositories.animal_repository as animal_repository

animal1 = Animal('Dog')
animal_repository.save(animal1)

