from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app= FastAPI()

class Items(BaseModel):
    
    name : str
    description : str

class ItemList(BaseModel):
    items :List[Items]

created_items = []

@app.post("/create_items/")
def create_item(item_list: ItemList):

    for i in range(len(item_list.items)):
        created_item = {"id": i+1,"name": item_list.items[i].name, "description" : item_list.items[i].description}
        created_items.append(created_item)
    return {'items': created_items}

@app.get("/items/{item_id}")
def get_items(item_id : int):
    for item in created_items:
        if item['id'] ==  item_id:
            return item
     
    return {"Message" : "Item not found"}

@app.put("/items/{item_id}")
def update_item(item_id :int, updated_item : Items):
    for item in created_items:
        if item['id']== item_id:
            item['name'] = updated_item.name
            item['description'] = updated_item.description
            return {"message" : "Item updated Successfully"}
    return {"message" : "Not found"}


@app.delete("/items/{item_id}")
def delete_item(item_id : int):
    global created_items
    created_items = [item for item in created_items if item['id']!= item_id]
    return{"message" : "Item deleted successfully", "created-list" :created_items}