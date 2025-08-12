from flask import Blueprint, render_template, request, redirect, url_for
from app.services.names_generator_service import generate_standard, generate_norse

names_bp = Blueprint('names', __name__)

types = ["Standard names", "Norse names"]
species = {
    "Aasimar (Male)": "aasimar_male",
    "Aasimar (Female)": "aasimar_female",
    "Dragonborn (Male)": "dragonborn_male",
    "Dragonborn (Female)": "dragonborn_female",
    "Dwarf (Male)": "dwarf_male",
    "Dwarf (Female)": "dwarf_female",
    "Elf (Male)": "elf_male",
    "Elf (Female)": "elf_female",
    "Gnome (Male)": "gnome_male",
    "Gnome (Female)": "gnome_female",
    "Goliath (Male)": "goliath_male",
    "Goliath (Female)": "goliath_female",
    "Halfling (Male)": "halfling_male",
    "Halfling (Female)": "halfling_female",
    "Human (Male)": "human_male",
    "Human (Female)": "human_female",
    "Orc (Male)": "orc_male",
    "Orc (Female)": "orc_female",
    "Tiefling (Male)": "tiefling_male",
    "Tiefling (Female)": "tiefling_female"
}

norse = {
    "Aasimar/Valkyrie (Female)": "aasimar_female",
    "Dwarf": "dwarf_male",
    "Elf (Male)": "elf_male",
    "Elf (Female)": "elf_female",
    "Goliath/Giant (Male)": "goliath_male",
    "Goliath/Giant (Female)": "goliath_female",
    "Human (Male)": "norse_human_male",
    "Human (Female)": "norse_human_female"
}

@names_bp.route('/names')
def names():
    name = request.args.get('name')
    msg = request.args.get('msg')

    return render_template('names.html', title="Names generator", types=types, species=species, norse=norse, name=name, msg=msg)

@names_bp.route('/generate_standard_name', methods=['GET'])
def generate_standard_name():
    try:
        standard_species = request.args.get('standardSpecies')

        if "_male" in standard_species:
            standard_gender = "male"
        else:
            standard_gender = "female"

        name = generate_standard(standard_species, standard_gender)

        return render_template(
            'names.html',
            title="Names generator",
            types=types,
            species=species,
            norse=norse,
            name=name
        )
    except Exception as e:
        return redirect(url_for('names.names', msg="An error occurred!"))

@names_bp.route('/generate_norse_name', methods=['GET'])
def generate_norse_name():
    try:
        norse_species = request.args.get('norseSpecies')

        if "_male" in norse_species:
            gender = "male"
        else:
            gender = "female"

        name = generate_norse(norse_species, gender)

        return render_template(
            'names.html',
            title="Names generator",
            types=types,
            species=species,
            norse=norse,
            name=name
        )
    except Exception as e:
        return redirect(url_for('names.names', msg="An error occurred!"))