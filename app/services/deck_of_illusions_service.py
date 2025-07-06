import csv
import random

folder = "app/static/illusion_deck_files"
deck_list = f"{folder}/deck_list.txt"
used_cards = f"{folder}/used_cards.txt"
backup = f"{folder}/backup_list.txt"

def pick_card():
    """
     Pick one random card from deck
    """
    try:
        remaining_cards = get_cards()
        random_card = get_random_card(remaining_cards)

        if random_card is None:
            return "\nNo cards remaining!\n"

        update_cards(remaining_cards, random_card)

        return random_card['card']

    except Exception as e:
        return "\nSomething went wrong while picking a card!\n"

def get_cards():
    """
    Get remaining cards ids
    """
    try:
        with open(deck_list, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            remaining_cards = []
            for row in reader:
                remaining_cards.append(row)
            return remaining_cards

    except FileNotFoundError:
        return "\nFile deck_list.txt not found!\n"
    except Exception as e:
        print("\nSomething went wrong while getting a card number!\n")

def get_random_card(remaining_cards):
    """
    Pick one random remaining card id and append to used cards file
    """
    if remaining_cards != []:
        try:
            random_card = random.choice(remaining_cards)

            with open(used_cards, "a", encoding="utf-8") as file:
                file.write(f"{random_card['id']},{random_card['card']}\n")
            return random_card

        except FileNotFoundError:
            return "\nFile deck_list.txt not found!\n"
        except Exception as e:
            print("\nSomething went wrong while getting a random card!\n")
    else:
        return

def update_cards(remaining_cards, random_card):
    """
    Excludes picked card from txt file and rewrites it without that card
    """
    try:
        updated_cards = []
        for card in remaining_cards:
            if random_card == card:
                continue
            updated_cards.append(card)

        #Overwrite updated new file
        with open(deck_list, "w", encoding="utf-8") as file:
            # Write headers
            file.write("id,card\n")

            for row in updated_cards:
                file.write(f"{row['id']},{row['card']}\n")

    except FileNotFoundError:
        print("\nFile txt not found!\n")

    except Exception as e:
        print("\nSomething went wrong!\n")

def show_deck():
	"""
	 Show number of cards
	"""
	try:
		deck = get_cards()
		total_cards = len(deck)
		return total_cards

	except Exception as e:
		print("\nSomething went wrong while showing deck!\n")

def show_figures():
	"""
	Show remaining figures
	"""
	try:
		with open(deck_list, "r", encoding="utf-8") as file:
			reader = csv.DictReader(file)

			remaining_cards = []
			for row in reader:
				remaining_cards.append(row)
			return remaining_cards

	except FileNotFoundError:
		return "\nFile deck_list.txt not found!\n"
	except Exception as e:
		print("\nSomething went wrong while getting a card number!\n")


def reset_deck():
	"""
	Reset cards
	"""
	try:
		# Get data from backup file
		with open(backup, "r", encoding="utf-8") as file:
			reader = csv.DictReader(file)

			backup_cards = []
			for row in reader:
				backup_cards.append(row)

		# Overwrites txt file with backup
		with open(deck_list, "w", encoding="utf-8") as file:
			# Write headers
			file.write("id,card\n")

			for row in backup_cards:
				file.write(f"{row['id']},{row['card']}\n")

		# Removes used cards
		with open(used_cards, "w", encoding="utf-8") as file:
			# Write headers
			file.write("id,card\n")

		return "\nGenerated new deck!\n"

	except FileNotFoundError:
		print("\nFile txt not found!\n")
	except Exception as e:
		print("\nSomething went wrong while resetting the deck!\n")

def incomplete_deck():
	"""
	Generate a deck with 1/20 - 1 random cards
	"""
	try:
		with open(backup, "r", encoding="utf-8") as file:
			backup_cards = list(csv.DictReader(file))

			total_cards = len(backup_cards)
			missing_cards = total_cards - (random.randint(1, 20)) - 1

			deck = random.sample(backup_cards, missing_cards)

			# Overwrites deck_list file with random cards
			with open(deck_list, "w", encoding="utf-8") as file:
				# Write headers
				file.write("id,card\n")

				for row in deck:
					file.write(f"{row['id']},{row['card']}\n")

			# Removes used cards
			with open(used_cards, "w", encoding="utf-8") as file:
				# Write headers
				file.write("id,card\n")

			return "Generated incomplete deck!"

	except FileNotFoundError:
		print("\nFile txt not found!\n")
	except Exception as e:
		print("\nSomething went wrong while resetting the deck!\n")


def restore_card(id):
	"""
	Restore the card you select in your deck
	"""
	try:
		used_list = get_used_list()

		restored_card = ""
		if used_list != []:
			for card in used_list:
				print(f"{card['id']}, {card['card']}")
		else:
			restored_card = "\nNo cards used!\n"
			return restored_card

		print("\nInput card number to restore. Digit 0 to cancel\n")
		select = id

		if select == 0:
			restored_card = "\nNo card selected\n"
			return restored_card

		elif select != 0:
			for card in used_list:
				if select == int(card['id']):
					restored_card = {
						'id': card['id'],
						"card": card['card']
					}

		if restored_card == "":
			return "\nNo card found\n"

		# Append card to main deck
		with open(deck_list, "a", encoding="utf-8") as file:
			file.write(f"{restored_card['id']},{restored_card['card']}\n")

		# Check updated cards
		updated_used_cards = []
		for card in used_list:
			if restored_card == card:
				continue
			updated_used_cards.append(card)

		# Update used cards
		with open(used_cards, "w", encoding="utf-8") as file:
			# Write headers
			file.write("id,card\n")

			for row in updated_used_cards:
				file.write(f"{row['id']},{row['card']}\n")
			return f"Restored {restored_card['card']} to deck!"

	except FileNotFoundError:
		print("\nFile txt not found!\n")
	except ValueError as e:
		return "\nInvalid input, you must insert a number.\n"
	except Exception as e:
		return "\nSomething went wrong while restoring a card!\n"

def get_used_list():
	try:
		with open(used_cards, "r", encoding="utf-8") as file:
			reader = csv.DictReader(file)

			used_list = []
			for card in reader:
				used = {
					'id': card['id'],
					"card": card['card']
				}
				used_list.append(used)
		return used_list

	except FileNotFoundError:
		return "\nFile used_cards.txt not found!\n"
	except Exception as e:
		return "\nSomething went wrong while restoring a card!\n"