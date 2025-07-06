import csv
import random

folder = "app/static/critical_failures"
extension = '.txt'

def pick_random_row(types):
    path = f"{folder}/{types}{extension}"
    try:
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = list(csv.DictReader(csvfile, delimiter=';'))
            return random.choice(reader)
    except FileNotFoundError as e:
        print(f"File {path} not found")
    except Exception as e:
        print("An error occurred while picking an effect.")