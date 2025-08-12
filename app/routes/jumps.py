from flask import Blueprint, render_template, redirect, url_for, request
from app.services.jumps_service import get_jump
jumps_bp = Blueprint('jumps', __name__)

@jumps_bp.route('/jumps')
def jumps():
    msg = request.args.get("msg")

    return render_template(
        'jumps.html',
        title="Jumps Calculator",
        msg=msg
    )

@jumps_bp.route('/calculate_jump', methods=['POST'])
def calculate_jump():
    try:
        score = int(request.form.get('score') or 0)

        if score > 30:
            return redirect(url_for('jumps.jumps', msg="Strength score cannot be more than 30"))
        elif score < 1:
            return redirect(url_for('jumps.jumps', msg="Strength score cannot be less than 1"))

        res = get_jump(score)
        return render_template('jumps.html', title="Jumps Calculator", res=res)

    except ValueError as e:
        return redirect(url_for('jumps.jumps', msg="You must insert a number!"))
    except Exception as e:
        return redirect(url_for('jumps.jumps', msg="An error occurred!"))