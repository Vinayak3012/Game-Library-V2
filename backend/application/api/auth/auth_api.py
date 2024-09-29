from application.data.database import db
from application.data.datastore import ds
from application.data.model import Game as game_model
from application.data.model import Role as role_model
from application.data.model import RolesUsers as roles_users
from application.data.model import User as user_model
from flask_restx import Resource, fields, marshal, reqparse
from werkzeug.security import check_password_hash, generate_password_hash

login_parser = reqparse.RequestParser()
login_parser.add_argument(
    'email', type=str, required=True, help="Email is required !")
login_parser.add_argument('password', type=str,
                          required=True, help="Password is required !")


register_parser = reqparse.RequestParser()
register_parser.add_argument(
    'username', type=str, required=True, help="Username is required !")
register_parser.add_argument(
    'email', type=str, required=True, help="Email is required !")
register_parser.add_argument(
    'password', type=str, required=True, help="Password is required !")


class RegisterResource(Resource):
    def post(self):
        args = register_parser.parse_args()
        if not args.get('username') or not args.get('email') or not args.get('password'):
            return {"status": "failure", "message": "Incomplete Request Data"}, 400
        uname, email, pw = args.get('username'), args.get(
            'email'), args.get('password')
        already1 = user_model.query.filter_by(username=uname).first()
        already2 = user_model.query.filter_by(email=email).first()
        if already1 or already2:
            return {"status": "failure", "message": "User with same username/email already exists !"}, 400
        ds.create_user(username=uname, email=email,
                       password=generate_password_hash(pw), roles=["user"])
        db.session.commit()
        return {"status": "success", "message": "Registered successfully ! Please login !"}


class LoginResource(Resource):
    def post(self):
        args = login_parser.parse_args()
        if not args.get('email') or not args.get('password'):
            return {"status": "failure", "message": "Incomplete Request Data"}, 400
        email, pw = args.get('email'), args.get('password')
        user = user_model.query.filter_by(email=email).first()
        if not user:
            return {"status": "failure", "message": "User does not exist !"}, 404
        if not check_password_hash(user.password, pw):
            return {"status": "failure", "message": "Wrong password !"}, 404
        at = user.get_auth_token()
        return {"status": "success",
                "message": "You have successfully logged in !",
                "user": {
                    "username": user.username,
                    "email": user.email,
                    "type": user.roles[0].name,
                    "auth_token": str(at),

                }}
