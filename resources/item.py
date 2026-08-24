from flask import request
from db import stores, items
import uuid
from flask.views import MethodView
from flask_smorest import Blueprint,abort

blp = Blueprint("item", __name__, description = "item operation")

@blp.route("/item")
class ItemList(MethodView):
    def get(self):
        return {"items": list(items.values())}
    def post(self):
        item_data = request.get_json()
        if ("store_id" not in item_data 
            or "item_name" not in item_data
            or "item_price" not in item_data):
            abort(400, message = "payload must have store_id,item_name,item_price")
            
        for item in items.values():
            if (item_data["item_name"]==item["item_name"]
                and item_data["store_id"]==item["store_id"]):
                abort(400,message = "duplictae item")
                
        if item_data["store_id"] not in stores:
            return {"message": "store not in database"}, 404
        
        item_id = uuid.uuid4().hex
        item = {**item_data,"item_id":item_id}
        items[item_id] = item
        return item,201

    
@blp.route("/item/<string:item_id>")
class ItemID(MethodView):
    def get (self,item_id):
        try:
            return items[item_id]
        except KeyError:
            abort (404 ,message = "item not found in database")
            
    def delete(self,item_id):
        try:
            del items[item_id]
            return {"message": "item deleted"}
        except KeyError:
            abort(404,message="item not found")
            
    def put(self,item_id):
        item_data = request.get_json()
        if ("item_name" not in item_data or
            "item_price" not in item_data):
            abort(400,message="add item_name and item_price")
        try:
            item = items[item_id]
            item |= item_data
            return item
        except KeyError:
            abort (400,message="item not found")