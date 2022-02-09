from flask import Flask, render_template, Blueprint, request, redirect
from models.animal_type import AnimalType
from models.animal import Animal
import repositories.animal_type_repository as animal_type_repository
import repositories.animal_repository as animal_repository



animal_types_blueprint = Blueprint("animal_types", __name__)


@animal_types_blueprint.route("/animal_types/new")
def new_type():  
    return render_template('animal_types/new.html', header = "SPECIES")

@animal_types_blueprint.route("/animal_types", methods=['POST'])
def create_type():
    name = request.form['name']
    animal_type = AnimalType(name)
    animal_type_repository.save(animal_type)
    return redirect('/animals/new')