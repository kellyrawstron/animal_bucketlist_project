from flask import Flask, render_template, Blueprint
from models.type import Type
import repositories.type_repository as type_repository
import repositories.animal_repository as animal_repository

types_blueprint = Blueprint("types", __name__)

@types_blueprint.route("/types")
def types():
    types = type_repository.select_all_types()
    return render_template('types/index.html', types = types)

@types_blueprint.route("/types/new")
def new_type():
    animals = animal_repository.select_all_animals()
    return render_template('types/new.html', animals = animals)

