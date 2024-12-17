from flask import Flask
from flask_restful import Api
from models import db,Product ,Order
from flask import request, jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.errorhandler(500)
def internal_error(error):
    return {"error": "An unexpected error occurred"}, 500

@app.errorhandler(400)
def bad_request(error):
    return {"error": str(error)}, 400

with app.app_context():
    db.create_all()
    print("Tables created:", db.inspect(db.engine).get_table_names())

api = Api(app)

@app.route("/postorder",methods = ["POST"])
def Orderpost():
    data = request.get_json()
    products = data['products']
    order_total = 0.0

    for item in products:
        product = Product.query.get(item['id'])
        if product and product.stock >= item['quantity']:
            product.stock -= item['quantity']
            order_total += product.price * item['quantity']

        else:
            return jsonify({"error": f"Not enough stock for product {item['id']}"}), 400

    new_order = Order(products=products, total_price=order_total)
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"id": new_order.id, "status": new_order.status}), 201

@app.route("/getproducts",methods = ["GET"])
def get():
    products = Product.query.all()
    return jsonify([{
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "stock": product.stock
    } for product in products])

@app.route("/postproduct",methods = ["POST"])
def create_product():
    data = request.get_json()
    print(data)

    # Validate the incoming data
    if not data or 'name' not in data or 'price' not in data or 'stock' not in data:
        return jsonify({"message": "Invalid input"}), 400  # Bad request response

    new_product = Product(
        name=data['name'],
        description=data.get('description'),  # use get to avoid KeyError
        price=data['price'],
        stock=data['stock']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"id": new_product.id}), 201  # Created response

if __name__ == '__main__':
    app.run(debug=True)
