from flask import Flask, request
from db import stores, items
import uuid
from flask_smorest import abort


app = Flask(__name__)


# @app.route("/store", methods=['GET'])
@app.get("/store")  # shorthand for above, same for post
# only one method per endpoint, multiple will overwrite (last one remmains)
def get_all_stores():
    return {"stores": list(stores.values())}

@app.get("/item")
def get_all_item():
    return {"items": list(items.values())}

@app.get("/store/<string:store_id>")
def show_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort (404 ,message = "store not found in database")
    
    
@app.get("/store/<string:item_id>") #repurposed from all store item to specific item
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort (404 ,message = "item not found in database")


#store creating
@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**store_data,"store_id": store_id}
    stores[store_id]
    return store, 201


@app.post("/item") #item creating
def add_item():   #not passing any param, how item_data getting values?
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        return {"message": "store not in database"}, 404
    
    item_id = uuid.uuid4().hex
    item = {**item_data,"item_id":item_id}
    items[item_id] = item
    return item,201





