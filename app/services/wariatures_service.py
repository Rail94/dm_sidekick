import csv
import random

folder = "app/static/wariatures_files"
extension = ".txt"

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

paths = {
	"units": f"{folder}/{categories['u']}{extension}",
	"classes": f"{folder}/{categories['c']}{extension}",
	"legendaries": f"{folder}/{categories['l']}{extension}",
	"spirits": f"{folder}/{categories['s']}{extension}",
	"divinities": f"{folder}/{categories['d']}{extension}"
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

def choose_probability():
	num = random.randint(minimum, maximum)

	# Unit range
	if num >= probabilities['minUnit'] and num <= probabilities['maxUnit']:
		miniature = get_miniature(paths['units'])
		return miniature

	# Class range
	elif num >= probabilities['minClass'] and num <= probabilities['maxClass']:
		miniature = get_miniature(paths['classes'])
		return miniature

	# Legendary range
	elif num >= probabilities['minLegendary'] and num <= probabilities['maxLegendary']:
		miniature = get_miniature(paths['legendaries'])
		return miniature

	# Spirit range
	elif num == probabilities['spirit']:
		miniature = get_miniature(paths['spirits'])
		return miniature

	# Divinity range
	elif num == probabilities['divinity']:
		miniature = get_miniature(paths['divinities'])
		return miniature

	# Doppelganger range
	elif num == probabilities['doppelganger']:
		return "Doppelganger"

def open_pack(packs_size):
	miniatures = []

	for i in range(packs_size):
		miniature = choose_probability()
		miniatures.append(miniature)

	if packs_size == 5:
		class_miniature = get_miniature(paths['classes'])
		miniatures.append(class_miniature)

	if packs_size == 6:
		for i in range(2):
			legendary_miniature = get_miniature(paths['legendaries'])
			miniatures.append(legendary_miniature)

		miniatures.append("Doppelganger")

	return miniatures