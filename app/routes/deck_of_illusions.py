from flask import Blueprint, render_template, redirect, url_for, request
from app.services.deck_of_illusions_service import show_deck, get_cards, pick_card, reset_deck, incomplete_deck, get_used_list, restore_card

deck_of_illusions_bp = Blueprint('deck_of_illusions', __name__)

@deck_of_illusions_bp.route('/deck_of_illusions')
def deck_of_illusions():
    try:
        picked_card = request.args.get('picked_card')

        # Count total number of cards
        total_cards = show_deck()

        # Get all remaining cards
        remaining_cards = get_cards()

        # Get used cards
        used_cards = get_used_list()

        return render_template('deck_of_illusions.html', title="Deck of illusions", total_cards=total_cards, remaining_cards=remaining_cards, picked_card=picked_card, used_cards=used_cards)
    except Exception as e:
        return render_template('deck_of_illusions.html', title="Deck of illusions")
@deck_of_illusions_bp.route('/pick_card')
def draw_card():
    picked_card = pick_card()
    return redirect(url_for('deck_of_illusions.deck_of_illusions', title="Deck of illusions", picked_card=picked_card))

@deck_of_illusions_bp.route('/generate_deck/<int:option>')
def generate(option):
    if option == 0:
        reset_deck() # Generate full deck
    elif option == 1:
        incomplete_deck() # Generate incomplete deck

    return redirect(url_for('deck_of_illusions.deck_of_illusions', title="Deck of illusions"))

@deck_of_illusions_bp.route('/restore_card/<int:id>')
def restore(id):
    # Restore card to deck
    restore_card(id)

    return redirect(url_for('deck_of_illusions.deck_of_illusions', title="Deck of illusions"))