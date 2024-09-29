from application.api.initialize_api import initialize_api
from application.data.database import db
from application.data.datastore import ds
from config import devconfig
from datagen import gen
from flask import Flask, current_app
from flask_cors import CORS
from flask_security import Security


# from flask_security import Security
def create_app():
    app = Flask(__name__)
    # app['JDSHJSHFJHSJF']=sfdfds
    # 12345+"brycrypt"->dfdfdr4f
    app.config.from_object(devconfig)
    CORS(app, resources={r"/*": {"origins": "*"}})
    db.init_app(app)
    security = Security(app, ds)
    api = initialize_api(app)
    with app.app_context():
        db.create_all()
        gen()

    return app


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        # Now you can safely use app-related functionality here
        app.run(debug=True)


'''
add genre model with backref
genre api - for genre with and without id

'''
