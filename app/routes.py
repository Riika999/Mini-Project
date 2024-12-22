from flask import Blueprint, request, jsonify
from app import db
from app.models import User
from app.services import user_service

api_bp = Blueprint('api', __name__)

@api_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@api_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = user_service.create_user(data)
    return jsonify(user.to_dict()), 201

# ... other API endpoints
