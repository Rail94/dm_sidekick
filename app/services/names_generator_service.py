import random
import csv

folder = "app/static/names/"

name_types = {
	'dnd_base': 'dnd_base',
	'norse': 'norse'
}

extension = ".txt"

def get_name(path):
	try:
		with open(path, 'r', encoding='utf-8') as f:
			reader = list(csv.DictReader(f, delimiter=','))
			return random.choice(reader)
	except FileNotFoundError as e:
		return "File not found!"

def generate_standard(species, gender):
	if gender == "male":
		species_path = species.replace("_male", "")
	else:
		species_path = species.replace("_female", "")

	path_name = f"{folder}{name_types['dnd_base']}/{species_path}{extension}"
	path_surname = f"{folder}{name_types['dnd_base']}/{species_path}{extension}"

	name = get_name(path_name)
	if gender == "male":
		first_name = name['male']
	else:
		first_name = name['female']

	second_name = get_name(path_surname)

	generated_name = {
		'id': name['id'],
		'name': first_name.strip(),
		'surname': second_name['surname'].strip(),
		'species': species_path,
		'gender': gender
	}
	return generated_name

def generate_norse(species, gender):
	try:
		if gender == "male":
			species_path = species.replace("_male", "")
		else:
			species_path = species.replace("_female", "")

		path_name = f"{folder}{name_types['norse']}/{species_path}{extension}"

		while True:
			name = get_name(path_name)
			if gender == "male" and name['male']:
				first_name = name['male']
				break
			elif gender == "female" and name['female']:
				first_name = name['female']
				break

		if species_path == "dwarf":
			gender = "/ dwarven female names are not mentioned in old norse mythology"

		if first_name == "Alfhildr":
			gender += "/ only elven female name mentioned in old norse mythology"

		generated_name = {
			'id': name['id'],
			'name': first_name,
			'meaning_en': name[f'meaning_en'],
			'meaning_it': name[f'meaning_it'],
			'source': name['source'],
			'species': species_path,
			'gender': gender
		}
		return generated_name

	except FileNotFoundError as e:
		print("File not found!")
	except Exception as e:
		print("An error occurred while generating name!")