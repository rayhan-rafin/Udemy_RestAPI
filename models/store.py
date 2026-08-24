from db import db

class StoreModel (db.Model):
    __tablename__ = "stores"
    
    store_id = db.Column(db.Integer,primary_key=True)
    store_name = db.Column(db.String(80),unique=False,nullable=False)
    items = db.relationship("ItemModel",backpopulates="store",lazy="dynamic")