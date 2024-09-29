from application.api.auth.auth_api import LoginResource, RegisterResource
from application.api.game.game_api import GameResource, SingleGameResource
from flask_restx import Api

# ? id, title, genre, played


def initialize_api(app):
    api = Api(app)
    api.add_resource(LoginResource, '/api/login')
    api.add_resource(RegisterResource, '/api/register')
    api.add_resource(GameResource, '/games')
    api.add_resource(SingleGameResource, '/game/<int:id>')
    return api
