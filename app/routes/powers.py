from flask import Blueprint, jsonify, request
from app.models import Power, db

powers_bp = Blueprint('powers', __name__)

@powers_bp.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers])

@powers_bp.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({'error': 'Power not found'}), 404
    return jsonify(power.to_dict())

@powers_bp.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({'error': 'Power not found'}), 404

    data = request.get_json()
    description = data.get('description')

    if not description or len(description) < 20:
        return jsonify({'errors': ['Description must be at least 20 characters long']}), 400

    power.description = description
    db.session.commit()

    return jsonify(power.to_dict())