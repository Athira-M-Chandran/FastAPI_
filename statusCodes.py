from fastapi import FastAPI, status

app = FastAPI()

def get_item_from_database(item_id: int):
    # Logic to retrieve the item from the database
    # Example implementation:
    database = {
        1: {"name": "Item 1"},
        2: {"name": "Item 2"},
        # ...
    }
    if item_id in database:
        return database[item_id]
    else:
        return None

@app.get("/items/{item_id}")
def get_item(item_id : int):
    item = get_item_from_database(item_id)
    if item is None:
        # Item not found, return 404 Not Found
        return {"message":"Item not found"}, status.HTTP_404_NOT_FOUND
    
    # Item found, return 200 OK
    return {"item" : item},status.HTTP_200_OK