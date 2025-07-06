from flask import Blueprint, render_template, redirect, url_for, request
import random
from jinja2 import Template
from app.services.critical_failures_service import pick_random_row
critical_failures_bp = Blueprint('critical_failures', __name__)

@critical_failures_bp.route('/critical_failures')
def critical_failures():
    effect_id = request.args.get("id")
    effect_type = request.args.get("type")
    effect_title = request.args.get("effect")
    effect_description = request.args.get("description")

    #with open("melee.txt") as f:
    #    raw_text = f.read()

    #template = Template(raw_text)
    #rendered_text = template.render(d4=d4, d4_sum=d4_sum)

    return render_template(
        'critical_failures.html',
        title="Critical Fumbles",
        effect_id=effect_id,
        effect_type=effect_type,
        effect_title=effect_title,
        effect_description=effect_description
    )

@critical_failures_bp.route('/fumble_effect/<type>')
def fumble_effect(type):
    d4 = random.randint(1, 4)
    direction = random.randint(1,8)
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
    effect = pick_random_row(type)

    description = effect['description']
    description = description.replace('{{ d4 }}', str(d4))
    description = description.replace('{{ d4_sum }}', str(d4+1))
    description = description.replace('{{ direction }}', directions[direction])

    return redirect(url_for(
        'critical_failures.critical_failures',
        id=effect['id'],
        type=effect['type'],
        effect=effect['effect'],
        description=description
    ))