from flask import Blueprint
from flask import jsonify

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login")
def login():
    return jsonify({"msg":"Pagina de Login"})
