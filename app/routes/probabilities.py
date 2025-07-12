from flask import Blueprint, render_template, redirect, url_for, request
from app.services.probabilities_service import calculate
probabilities_bp = Blueprint('probabilities', __name__)

@probabilities_bp.route('/probabilities')
def probabilities():
    difficulty = request.args.get("difficulty")
    result = request.args.get("result")

    return render_template(
        'probabilities.html',
        title="Calculate Probabilities",
        difficulty=difficulty,
        result=result
    )

@probabilities_bp.route('/calculate_probability/<difficulty>')
def calculate_probability(difficulty):
    try:
        result = calculate(difficulty)

        return redirect(url_for(
            'probabilities.probabilities',
            difficulty=difficulty,
            result=result
        ))
    except Exception as e:
        return redirect(url_for(
            'probabilities.probabilities',
            difficulty="",
            result=""
        ))
