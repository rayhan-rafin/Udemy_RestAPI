from db import db

class ItemModel(db.Model):
    __tablename__ = "items"
    
    item_id = db.Column(db.Integer,primaary_key = True)
    item_name = db.Column(db.string(80), unique=False, nullable = False)
    item_price = db.Column(db.Float(precision=2),unique=False,nullable=False)
    store_id = db.Column(db.Integer,db.ForeignKey("stores.store_id"),Unique=False,nullable=False)
    store = db.relationship("StoreModel",backpopulates = "items")
    