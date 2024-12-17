from db import db


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    products = db.Column(db.JSON, nullable=False)  # List of product ID and quantity
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String, default='pending', nullable=False)
