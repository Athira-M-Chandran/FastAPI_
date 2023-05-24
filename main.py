

from fastapi import FastAPI
from typing import List
from model import Item

# initializing a FastAPI object
app = FastAPI()

# Section 3: FastAPI - Starting Fast API

@app.get("/")  # decorator specifies that this function will handle HTTP GET requests to the root path ("/") of your application
def read_root():
    return{"Hello": "world"} # The function itself returns a dictionary that will be converted into a JSON response.

# To run the FastAPI application, you need to start the server
# In terminal run : uvicorn main:app --reload
# The --reload option enables automatic reloading of the server whenever code changes are detected, which is helpful during development.
# Check in postman ; Enter http://127.0.0.1:8000/ in  request url with GET method

# Section 3: FastAPI - Path operations

@app.get('/items/{item_id}')
def read_item(item_id:int):
    return{"item_id":item_id}

# Path parameters and query parameters
@app.get('/get_items/{item_id}')
def read_item(item_id: int, q: str = None):
    
    if(q):
        result = {'item_id':item_id, 'q':q}
        return(result)
    return{'item_id':item_id}


# Handle post

@app.post('/post_items/')
def create_item(item: Item):
    return {"item": item}

# for multiple items
@app.post('/multiple_items/')
def create_items(items: List[Item]):
    return {"items" : items}


item_data = {
    "name": "Example Item",
    "price": 9.99
}

item = Item(**item_data)
print(item.name)    # Output: Example Item
print(item.price)   # Output: 9.99