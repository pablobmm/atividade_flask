from flask import Blueprint, request, jsonify
import users.route_user as modUser

bd_user = Blueprint('User', __name__)


@bd_user.route("/user", methods=["GET"])
def listar_user():