from flask import Flask, render_template, Blueprint, request, redirect
from models.animal_type import AnimalType
from models.animal import Animal
import repositories.animal_type_repository as animal_type_repository
import repositories.animal_repository as animal_repository



animal_types_blueprint = Blueprint("animal_types", __name__)

@animal_types_blueprint.route("/animal_types", methods=['GET'])
def animal_types():
    animals = animal_repository.select_all()
    return render_template('animal_types/index.html', animals = animals)

@animal_types_blueprint.route("/animal_types/new")
def new_type():
    animal_types = animal_type_repository.select_all()
    return render_template('animal_types/new.html', animal_types = animal_types)

@animal_types_blueprint.route("/animal_types", methods=['POST'])
def create_type():
    name = request.form['name']
    animal_type_id = request.form['animal_type_id']
    seen = request.form['seen']
    breed = request.form['breed']
    animal_type =  animal_type_repository.select(animal_type_id)
    animal = Animal(name, breed, animal_type, seen)
    animal_repository.save(animal)
    return redirect('/animal_types')

@animal_types_blueprint.route("/animal_types/<id>/delete", methods=['POST'])
def delete_type(id):
    animal_repository.delete(id)
    return redirect('/animals')

@animal_types_blueprint.route("/animal_types/<id>")
def show_type(id):
    animal = animal_repository.select(id)
    return render_template('animal_types/show.html', animal = animal)

@animal_types_blueprint.route("/animal_types/<id>/edit")
def edit_type(id):
    animal_types = animal_type_repository.select_all()
    animal = animal_repository.select(id)
    return render_template('animal_types/edit.html', animal = animal, animal_types = animal_types)

@animal_types_blueprint.route("/animal_types/<id>", methods=['POST'])
def update_type(id):
    name = request.form['name']
    animal_type_id = request.form['animal_type_id']
    seen = request.form['seen']
    breed = request.form['breed']
    animal_type =  animal_type_repository.select(animal_type_id)
    animal = Animal(name, breed, animal_type, seen, id)
    animal_repository.update(animal)
    return redirect('/animal_types')