from app import db
from app.api import bp
from app.models import Product, ProductUser
from app.producer import publish
from flask import abort, jsonify
import requests, json


@bp.route('/products')
def index():
    queries = db.session.execute(db.select(Product)).fetchall()
    products = [query[0].serialized for query in queries]
    return jsonify(products)

@bp.route('/products/<int:id>/like', methods=['POST'])
def like(id):
    req = requests.get('http://172.18.0.1:8000/api/user')
    data = req.json()

    try:
        product_user = ProductUser(user_id=data['id'], product_id=id)
        db.session.add(product_user)
        db.session.commit()

        publish('product_liked', id)

    except:
        abort(400, 'You already liked this product.')

    return jsonify({
        'message': 'success'
    })


