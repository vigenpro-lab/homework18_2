from flask_restx import Namespace, Resource
from app.container import user_service
from app.dao.model.user import UserSchema
from flask import request

user_ns = Namespace("users")

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route("/")
class UsersView(Resource):
    def get(self):
        return user_service.get_all(), 200

    def post(self):
        req_data = request.json
        user_service.create(req_data)
        return "", 201


@user_ns.route("/<int:uid>")
class UserView(Resource):

    def put(self):
        data = request.json
        user_service.update(data)
        return "", 204
