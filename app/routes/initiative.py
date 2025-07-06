from flask import Blueprint, render_template

initiative_bp = Blueprint('initiative', __name__)

@initiative_bp.route('/initiative')
def initiative():
    return render_template('initiative.html', title="Roll 4 Initiative!")
