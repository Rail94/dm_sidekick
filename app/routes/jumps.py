from flask import Blueprint, render_template, redirect, url_for, request
#from app.services.probabilities_service import calculate
jumps_bp = Blueprint('jumps', __name__)

@jumps_bp.route('/jumps')
def jumps():
    
    return render_template(
        'jumps.html',
        title="Jumps Calculator"
    )
