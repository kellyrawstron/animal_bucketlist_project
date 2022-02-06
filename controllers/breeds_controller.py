from flask import Flask, render_template, Blueprint, request, redirect
from models.breed import Breed
import repositories.breed_repository as breed_repository
import repositories.animal_repository as animal_repository



breeds_blueprint = Blueprint("breeds", __name__)

@breeds_blueprint.route("/breeds", methods=['GET'])
def breeds():
    breeds = breed_repository.select_all()
    return render_template('breeds/index.html', breeds = breeds)

@breeds_blueprint.route("/breeds/new")
def new_breed():
    animals = animal_repository.select_all()
    return render_template('breeds/new.html', animals = animals)

@breeds_blueprint.route("/breeds", methods=['POST'])
def create_breed():
    breed_kind = request.form['breed_kind']
    animal_id = request.form['animal_id']
    breed_seen = request.form['breed_seen']
    animal = animal_repository.select(animal_id)
    breed = Breed(breed_kind, animal, breed_seen)
    breed_repository.save(breed)
    return redirect('/breeds')

@breeds_blueprint.route("/breeds/<id>/delete", methods=['POST'])
def delete_breed(id):
    breed_repository.delete(id)
    return redirect('/breeds')

@breeds_blueprint.route("/breeds/<id>")
def show_breed(id):
    breed = breed_repository.select(id)
    return render_template('breeds/show.html', breed = breed)

@breeds_blueprint.route("/breeds/<id>/edit")
def edit_breed(id):
    breed = breed_repository.select(id)
    animals = animal_repository.select_all()
    return render_template('breeds/edit.html', breed = breed, animals = animals)

@breeds_blueprint.route("/breeds/<id>", methods=['POST'])
def update_breed(id):
    breed_kind = request.form['breed_kind']
    animal_id = request.form['animal_id']
    breed_seen = request.form['breed_seen']
    animal = animal_repository.select(animal_id)
    breed = Breed(breed_kind, animal, breed_seen, id)
    breed_repository.update(breed)
    return redirect('/breeds')
    