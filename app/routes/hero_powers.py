from flask import Blueprint, jsonify, request
from app.models import HeroPower, Hero, Power, db

hero_powers_bp = Blueprint('hero_powers', __name__)

@hero_powers_bp.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    strength = data.get('strength')
    power_id = data.get('power_id')
    hero_id = data.get('hero_id')

    if strength not in ['Strong', 'Weak', 'Average']:
        return jsonify({'errors': ['Strength must be one of: Strong, Weak, Average']}), 400

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)

    if not hero or not power:
        return jsonify({'errors': ['Hero or Power not found']}), 404

    hero_power = HeroPower(
        strength=strength,
        hero_id=hero_id,
        power_id=power_id
    )

    db.session.add(hero_power)
    db.session.commit()

    response = {
        'id': hero_power.id,
        'hero_id': hero_power.hero_id,
        'power_id': hero_power.power_id,
        'strength': hero_power.strength,
        'hero': hero.to_dict(),
        'power': power.to_dict()
    }

    return jsonify(response), 201