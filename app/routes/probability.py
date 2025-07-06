from flask import Blueprint, render_template

probability_bp = Blueprint('probability', __name__)

@probability_bp.route('/probability')
def probability():
    return render_template('index.html', title="Calculate probabilities")
