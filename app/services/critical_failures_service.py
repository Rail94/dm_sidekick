import csv
import random

folder = "app/static/critical_failures"
extension = '.txt'

def roll_d4(roll):
    for i in range(roll):
        return sum(random.randint(1, 4) for _ in range(roll))

def roll_d6(roll):
    return sum(random.randint(1, 6) for _ in range(roll))

def random_animal():
    animals = ['Goat', 'Fish', 'Frog', 'Cat']
    select = random.randint(0,len(animals)-1)
    animal = animals[select]
    return animal

def lingering_injuries():
    injuries = {
        'Lose an eye'
    }

def random_saving_throw():
    base = 10
    roll = random.randint(1,10)
    saving_throw = base + roll
    return saving_throw

def select_direction():
    random_direction = random.randint(1, 8)
    directions = {
        1: 'Up-Left',
        2: 'Up',
        3: 'Up-Right',
        4: 'Left',
        5: 'Right',
        6: 'Down-Left',
        7: 'Down',
        8: 'Down-Right'
    }
    direction = directions[random_direction]
    return direction

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