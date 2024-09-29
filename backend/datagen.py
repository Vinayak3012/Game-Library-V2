from application.data.database import db
from application.data.datastore import ds
from application.data.model import Game as game_model
from application.data.model import Role as role_model
from application.data.model import RolesUsers as roles_users
from application.data.model import User as user_model
from werkzeug.security import generate_password_hash

GAMES = [
    {
        "title": "The Elder Scrolls V: Skyrim",
        "genre": "RPG",
        "played": True,
    },
    {
        "title": "Grand Theft Auto V",
        "genre": "Action",
        "played": False,
    },
    {
        "title": "The Witcher 3: Wild Hunt",
        "genre": "Fantasy",
        "played": False,
    },
    {
        "title": "World of Warcraft",
        "genre": "MMORPG",
        "played": True,
    },
    {
        "title": "Civilization VI",
        "genre": "Strategy",
        "played": True,
    },
    {
        "title": "Settlers of Catan",
        "genre": "Board",
        "played": False,
    },
    {
        "title": "Tetris Effect",
        "genre": "Puzzle",
        "played": False,
    },
]


def gen():
    ds.find_or_create_role(
        name="admin", description="Admin manages the system")
    ds.find_or_create_role(
        name="user", description="User interacts with the system")
    db.session.commit()
    if not ds.find_user(email="manager.gamevault@gmail.com"):
        ds.create_user(username="manager", email="manager.gamevault@gmail.com",
                       password=generate_password_hash("12345"), roles=["admin"])
        db.session.commit()
    if not ds.find_user(email="user.gamevault@gmail.com"):
        ds.create_user(username="user1", email="user.gamevault@gmail.com",
                       password=generate_password_hash("12345"), roles=["user"])
        db.session.commit()
    games = game_model.query.all()
    if not games:
        for i in GAMES:
            new_game = game_model(
                title=i["title"], genre=i["genre"], played=i["played"])
            db.session.add(new_game)
        db.session.commit()
