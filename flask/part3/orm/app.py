from flask import Flask
from flask_smorest import Api
from db import db
from models import User, Board
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:746472@localhost/oz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# blurprint
app.config["API_TITLE"] = "MY API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.3/"

api = Api(app)

from routes.board import board_blp
from routes.users import user_blp

api.register_blueprint(board_blp)
api.register_blueprint(user_blp)

if __name__ == "__main__":
    app.run(debug=True)
