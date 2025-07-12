from flask import Blueprint, render_template, redirect, url_for, request
import random
from jinja2 import Template
from app.services.critical_failures_service import pick_random_row, roll_d4, roll_d6, select_direction, random_animal, random_saving_throw
critical_failures_bp = Blueprint('critical_failures', __name__)

@critical_failures_bp.route('/critical_failures')
def critical_failures():
    effect_id = request.args.get("id")
    effect_type = request.args.get("type")
    effect_title = request.args.get("effect")
    effect_description = request.args.get("description")

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
    try:
        effect = pick_random_row(type)

        description = effect['description']
        description = description.replace('{{ d4 }}', str(roll_d4(1)))
        description = description.replace('{{ d6 }}', str(roll_d6(1)))
        description = description.replace('{{ 4d6 }}', str(roll_d6(4)))
        description = description.replace('{{ direction }}', select_direction())
        description = description.replace('{{ animal }}', random_animal())
        description = description.replace('{{ saving_throw }}', str(random_saving_throw()))

        return redirect(url_for(
            'critical_failures.critical_failures',
            id=effect['id'],
            type=type,
            effect=effect['effect'],
            description=description
        ))
    except Exception as e:
        return redirect(url_for(
            'critical_failures.critical_failures',
            id="0",
            type="",
            effect="",
            description="Cannot find effects!"
        ))
