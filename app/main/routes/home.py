from flask import Blueprint
from flask import jsonify

home_bp = Blueprint("main", __name__)

@home_bp.route("/")
def home():
    return jsonify({"status":"ok"})
