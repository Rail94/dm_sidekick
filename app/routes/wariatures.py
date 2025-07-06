from flask import Blueprint, render_template, redirect, url_for, request
from app.services.wariatures_service import open_pack

wariatures_bp = Blueprint('wariatures', __name__)

@wariatures_bp.route('/wariatures')
def wariatures():
    miniatures = request.args.getlist('miniatures')
    return render_template('wariatures.html', title="Wariatures Unpack", miniatures=miniatures)

@wariatures_bp.route('/open_bag/<size>')
def open_bag(size):
    packs_size = {
        "s": 4,
        "m": 5,
        "l": 6
    }

    miniatures = open_pack(packs_size[size])
    return redirect(url_for('wariatures.wariatures', miniatures=miniatures))