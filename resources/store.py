from flask import request
from db import stores, items
import uuid
from flask.views import MethodView
from flask_smorest import Blueprint,abort

blp = Blueprint("store", __name__, description = "store operation")

@blp.route("/store/<string:store_id>")
class StoreId(MethodView):
    def get (self,store_id):
        try:
            return stores[store_id]
        except KeyError:
             abort (404 ,message = "store not found in database")
             
             
    def delete(self,store_id):
        try:
            del stores[store_id]
            return {"message": "store deleted"}
        except KeyError:
                abort (404,message="store not found")
                
                
@blp.route("/store")                
class StoreList(MethodView):
    def get(self):
        return {"stores": list(stores.values())}
    def post(self):
        store_data = request.get_json()
        if ("store_name" not in store_data):
            abort(400,message="store_name not in json payload")
        for store in stores.values():
            if (store_data["store_name"]==store["store_name"]):
                abort(400,message="store_name already exists")
            
        store_id = uuid.uuid4().hex
        store = {**store_data,"store_id": store_id}
        stores[store_id] = store
        return store, 201
