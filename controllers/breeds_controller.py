from flask import Flask, render_template, Blueprint, request, redirect
import repositories.breed_repository as breed_repository
import repositories.animal_repository as animal_repository
from models.breed import Breed


breeds_blueprint = Blueprint("breeds", __name__)

@breeds_blueprint.route("/breeds", methods=['GET'])
def breeds():
    breeds = breed_repository.select_all()
    return render_template('breeds/index.html', breeds = breeds)

@breeds_blueprint.route("/breeds/new")
def new_breed():
    animals = animal_repository.select_all()
    return render_template('breeds/new.html', animals = animals)