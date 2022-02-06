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