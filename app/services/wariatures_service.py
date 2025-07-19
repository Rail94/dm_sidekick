import csv
import random

folder = "app/static/wariatures_files"
extension = ".txt"

collections = {
	'bs': 'base_set',
	'is': 'isavar_set'
}

probabilities = {
	"minUnit": 1,
	"maxUnit": 49,
	"minClass": 50,
	"maxClass": 89,
	"minLegendary": 90,
	"maxLegendary": 97,
	"spirit": 98,
	"divinity": 99,
	"doppelganger": 100
}

minimum = 1
maximum = 100

packs_size = {
	"s": 4,
	"m": 5,
	"l": 6
}

categories = {
	"u" : "units",
	"c": "classes",
	"l": "legendaries",
	"s": "spirits",
	"d": "divinities"
}

def build_paths(collection):
	return {
		"units": f"{folder}/{collections[collection]}/{categories['u']}{extension}",
		"classes": f"{folder}/{collections['bs']}/{categories['c']}{extension}",
		"legendaries":f"{folder}/{collections[collection]}/{categories['l']}{extension}",
		"spirits": f"{folder}/{collections['bs']}/{categories['s']}{extension}",
		"divinities": f"{folder}/{collections[collection]}/{categories['d']}{extension}",
	}

def count_lines_txt(paths):
	try:
		with open(paths, 'r', encoding='utf-8') as f:
			next(f)
			return sum(1 for _ in f)
	except FileNotFoundError:
		print(f"File {paths} not found!")
		return 0

def get_miniature(paths):
	try:
		with open(paths, 'r', encoding='utf-8') as f:
			reader = csv.DictReader(f)
			file_size = count_lines_txt(paths)
			num = random.randint(minimum, file_size)

			for row in reader:
				if int(row['number']) == num:
					miniature = row['name'].strip()
		return miniature

	except FileNotFoundError as e:
		print(f"Error, file {paths} not found!")
	except Exception as e:
		print(f"An error occurred while getting a miniature in file: {paths} | number: {num}")

def choose_probability(collection):
	num = random.randint(minimum, maximum)
	paths = build_paths(collection)

	# Unit range
	if num >= probabilities['minUnit'] and num <= probabilities['maxUnit']:
		return get_miniature(paths['units'])

	# Class range
	elif num >= probabilities['minClass'] and num <= probabilities['maxClass']:
		miniature = get_miniature(paths['classes'])
		return miniature

	# Legendary range
	elif num >= probabilities['minLegendary'] and num <= probabilities['maxLegendary']:
		return get_miniature(paths['legendaries'])

	# Spirit range
	elif num == probabilities['spirit']:
		miniature = get_miniature(paths['spirits'])
		return miniature

	# Divinity range
	elif num == probabilities['divinity']:
		return get_miniature(paths['divinities'])

	# Doppelganger range
	elif num == probabilities['doppelganger']:
		return "Doppelganger"

def open_pack(packs_size, collection='bs'):
	paths = build_paths(collection)
	miniatures = []

	for _ in range(packs_size):
		miniature = choose_probability(collection)
		miniatures.append(miniature)

	if packs_size == 5:
		miniatures.append(get_miniature(paths['classes']))

	if packs_size == 6:
		for _ in range(2):
			miniatures.append(get_miniature(paths['legendaries']))
		miniatures.append("Doppelganger")

	return miniatures