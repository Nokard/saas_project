from flask import Blueprint, request, jsonify



auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=['POST'])
def login():

    data = request.get_json(force=True)

    print (data)
    return jsonify({"msg":f"Pagina de Login \n {data}"})
