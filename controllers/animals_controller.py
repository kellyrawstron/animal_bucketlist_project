from flask import Flask, render_template, Blueprint, request, redirect
from models.animal_type import AnimalType
from models.animal import Animal
import repositories.animal_type_repository as animal_type_repository
import repositories.animal_repository as animal_repository


animals_blueprint = Blueprint("animals", __name__)


@animals_blueprint.route("/animals", methods=['GET'])
def animals():
    animals = animal_repository.select_all()
    return render_template('animals/index.html', animals = animals, header = "All Animals")

@animals_blueprint.route("/animals/new")
def new_animal():
    animal_types = animal_type_repository.select_all()
    return render_template('animals/new.html', animal_types = animal_types, header = "Add Animal")

@animals_blueprint.route("/animals", methods=['POST'])
def create_animal():
    name = request.form['name']
    animal_type_id = request.form['animal_type_id']
    seen = request.form['seen']
    breed = request.form['breed']
    animal_type =  animal_type_repository.select(animal_type_id)
    animal = Animal(name, breed, animal_type, seen)
    animal_repository.save(animal)
    return redirect('/animals')

@animals_blueprint.route("/animals/<id>/delete", methods=['POST'])
def delete_animal(id):
    animal_repository.delete(id)
    return redirect('/animals')

@animals_blueprint.route("/animals/<id>")
def show_animal(id):
    animal = animal_repository.select(id)
    return render_template('animals/show.html', animal = animal, header = "Add Animal")

@animals_blueprint.route("/animals/<id>/edit")
def edit_animal(id):
    animal_types = animal_type_repository.select_all()
    animal = animal_repository.select(id)
    return render_template('animals/edit.html', animal = animal, animal_types = animal_types)

@animals_blueprint.route("/animals/<id>", methods=['POST'])
def update_animal(id):
    name = request.form['name']
    animal_type_id = request.form['animal_type_id']
    seen = request.form['seen']
    breed = request.form['breed']
    animal_type =  animal_type_repository.select(animal_type_id)
    animal = Animal(name, breed, animal_type, seen, id)
    animal_repository.update(animal)
    return redirect('/animals')

@animals_blueprint.route("/animals/not_seen")
def not_seen_animals():
    animals = animal_repository.select_not_seen()
    return render_template('animals/index.html', animals = animals, header = "Animals Not Seen")
    # render the template to show all anjmals not seen.
    
@animals_blueprint.route("/animals/seen")
def seen_animals():
    animals = animal_repository.select_seen()
    return render_template('animals/index.html', animals = animals, header = "Animals Seen")
    