

from fastapi import FastAPI

# initializing a FastAPI object
app = FastAPI()

@app.get("/")  # decorator specifies that this function will handle HTTP GET requests to the root path ("/") of your application
def read_root():
    return("Hello world")  # The function itself returns a dictionary that will be converted into a JSON response.



# To run the FastAPI application, you need to start the server
# In terminal run : uvicorn main:app --reload
# The --reload option enables automatic reloading of the server whenever code changes are detected, which is helpful during development.
# Check in postman ; Enter http://127.0.0.1:8000/ in  request url with GET method