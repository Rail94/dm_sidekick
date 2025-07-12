import random

ranges = {
	'easy': 70,
	'medium': 50,
	'hard': 30,
	'impossible': 10
}

def calculate(difficulty):
	if difficulty in ranges:
		calc = random.randint(1,100)

		if calc <= ranges[difficulty]:
			result = "<span style='color: green;'>Success!</span>"
			return result
		else:
			result = "<span style='color: red;'>Failure!</span>"
			return result