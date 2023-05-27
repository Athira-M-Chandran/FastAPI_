
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel, Field, validator
from fastapi import HTTPException

app = FastAPI()

class Item(BaseModel):
    name : str = Field(..., min_length=1, max_length=100)
    price : float = Field(...,gt=0)

    #the `name` field is required (...) and must have a minimum length of 1 and a maximum length of 100 characters. 
    # The `price` field is required and must be a value greater than 0. 
    #These additional validation rules will be applied by FastAPI during the schema validation process.

    @validator("price")
    def validate_price(cls,value):
        if(value<0):
            raise ValueError("Price must be positive value")
        return value

class ItemList(BaseModel):
    items : List[Item] = Field(..., min_items=2, max_items=2)

    # Using field or @validator 

    @validator("items")
    def validate_items(cls, items):
        if len(items) >2:
            raise ValueError("Exceeded maximum limit of 2 items")
        return items
    


@app.post("/create_items/")
def post_items(items_list : ItemList):
    try:
        return {"message" : "Items created successfully","items" : items_list.items}
    except ValueError as e:
        raise HTTPException(status_code = 400, detail= str(e))

