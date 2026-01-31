from flask import Blueprint, request, jsonify
from app.models.users import User
from app.extensions.extensions import db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=['POST'])
def login():

    data = request.get_json(force=True)

    print (data)
    return jsonify({"msg":f"Pagina de Login \n {data}"})



@auth_bp.route("/register", methods=['POST'])
def register():

    data = request.get_json(force=True)

    user  = User.query.filter_by(email=data['email']).first()

    if user:
        return jsonify({"msg":f"Email já cadastrado: {data['email']}"}), 400
    
    new_user = User(name=data['name'], email=data['email'])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg":f"Usuário <{data['name']}> cadastrado com sucesso"}), 200