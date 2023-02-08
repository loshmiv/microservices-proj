from flask import jsonify, abort
from flask.cli import FlaskGroup
from flask_cors import CORS
from sqlalchemy import UniqueConstraint
#from models import Product, ProductUser
import requests
from app import create_app

#env_path = Path('./env') / '.env'
#load_dotenv(dotenv_path=env_path)

#app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{os.getenv("USERNAME")}:{os.getenv("PASSWORD")}@\
#    {os.getenv("HOST")}/{os.getenv("DATABASE_NAME")}'

app = create_app()
app.app_context().push()
cli = FlaskGroup(create_app=create_app)

@app.route('/api/products')
def index():
    return jsonify(Product.query.all()) 

    #@app.route('/api/products/<int:id>/like', methods=['POST'])


if __name__ == '__main__':
    cli()
