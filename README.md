## Section 1: Introduction - Course Project
 
 ### API 

 > An API, or **Application Programming Interface** , is like a messenger that allows different software applications to communicate and interact with each other. It defines a set of rules and protocols that determine how software components should interact, what data can be exchanged, and how it should be structured.  

 APIs are widely used in various contexts, such as web development, mobile app development, and integration between different software systems. They enable developers to leverage existing functionality or data provided by other applications, saving time and effort by reusing code and resources.

### FastAPI

>FastAPI is a **modern**, **high-performance** web framework for building APIs with Python. It is designed to be **easy to use**, **efficient**, and **highly scalable**. FastAPI leverages the latest features of Python 3.7+ and benefits from type annotations and asynchronous programming to provide fast and reliable APIs.

1. **High performance**: FastAPI is built on top of Starlette, an asynchronous web framework, which makes it incredibly fast. It is capable of handling thousands of requests per second with low latency.

2. **Easy to use**: FastAPI is designed to be developer-friendly. It offers a clean and intuitive syntax that is similar to writing regular Python functions. It supports automatic data validation, serialization, and documentation generation based on type annotations, which helps in reducing boilerplate code.

3. **Type annotations and automatic validation**: FastAPI leverages the Python type hints feature to enforce data validation. By adding type annotations to function parameters, FastAPI can automatically validate incoming requests, handle parameter conversion, and provide meaningful error messages.

4. **Asynchronous support** : FastAPI fully supports asynchronous programming, allowing you to write highly scalable and efficient code. It can handle asynchronous requests, database operations, and external API calls seamlessly, making it suitable for building real-time applications.

5. **Integrated documentation** : FastAPI generates interactive and detailed API documentation automatically based on your code's type annotations. You can access the documentation in your browser, explore available endpoints, test them, and even see example requests and responses.

6. **Security and authentication** : FastAPI provides built-in security features, including OAuth2 authentication, API key handling, and request validation. It also supports integration with popular authentication systems, such as ***JWT (JSON Web Tokens)***.

7. **WebSocket support** : FastAPI includes WebSocket support, allowing you to build ***real-time bidirectional communication*** between clients and the server using the WebSocket protocol.

8. **Scalability** : FastAPI is built to handle high loads and can be deployed in various production environments, including single-threaded and multi-worker servers. It also integrates well with other tools and frameworks, such as Docker and Kubernetes.

> Overall, FastAPI offers a powerful and efficient way to build APIs with Python, combining the speed and performance of asynchronous programming with the simplicity and ease of use of the Python language.

## Section 2: Setup & installation -  Python Installation

1. [Download Python Installer](https://www.python.org)
2. Run the Installer - 

    Make sure to check the box that says "Add Python to PATH" during the installation process. This will enable you to use Python from the Command Prompt.
3. Complete the Installation
4. Verify the Installation
    In the Command Prompt, type the following command:

    ```python --version```

    ```pip --version ```
5. Update pip (optional):

    ```pip install --upgrade pip```

## Section 3: FastAPI - Install dependencies w/ pip

- Step 1: Create a virtual environment (optional but recommended)
    Creating a virtual environment is a good practice to isolate your project dependencies. It allows you to have separate Python environments for different projects. You can create a virtual environment by running the following command in the Command Prompt or Terminal:

    ```python -m venv myenv```

- Step 2: Activate the virtual environment
    Activate the virtual environment by running the appropriate command based on your operating system:

    ```myenv\Scripts\activate```

    Once activated, your command prompt or terminal will indicate the active virtual environment.

- Step 3: Install FastAPI and dependencies

    ```pip install fastapi uvicorn```

    This command will install FastAPI and uvicorn, a recommended ASGI server for running FastAPI applications.

- Step 4: Additional dependencies (optional):

    ```pip install sqlalchemy```
## Section 3: FastAPI - Starting Fast API

* Step 1: Create a new Python file:

    Open your preferred text editor and create a new Python file. You can name it whatever you like, for example, main.py.
* Step 2: Import FastAPI:

    In your Python file, import the FastAPI module by adding the following line at the top:

    ```from fastapi import FastAPI```

* Step 3: Create an instance of the FastAPI application:

    Create an instance of the FastAPI application by initializing a FastAPI object. Add the following code after the import statement:

    ```app = FastAPI()```

* Step 4: Define a route and handler function:

    Create a route by defining a function that will handle the incoming requests. This function will be called when a request is made to a specific URL path. For example, let's create a simple "Hello, World!" route. Add the following code after the app = FastAPI() line:

    ```
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    ```

    In this example, the @app.get("/") decorator specifies that this function will handle HTTP GET requests to the root path ("/") of your application. The function itself returns a dictionary that will be converted into a JSON response.

* Step 5: Run the FastAPI application:

    To run the FastAPI application, you need to start the server. Open your terminal or command prompt, navigate to the directory where your Python file is located, and run the following command:

    ```uvicorn main:app --reload```

    The uvicorn command starts the server using the provided Python file (main) and the FastAPI application instance (app). The --reload option enables automatic reloading of the server whenever code changes are detected, which is helpful during development.

* Step 6: Access the FastAPI application:

    Once the server is running, you can access your FastAPI application by opening a web browser and navigating to http://localhost:8000 or http://127.0.0.1:8000. You should see the "Hello, World!" response.

## Section 3: FastAPI - Path operations

 Path operations are used to define routes that handle specific URL paths and HTTP methods. These routes define the behavior of your API endpoints.

 - Define a path operation:

    To define a path operation, you can use the decorator syntax. For example, let's create a GET endpoint at the path "/items/{item_id}" that returns the item ID:

    ```
    @app.get("/items/{item_id}")
    def read_item(item_id: int):
        return {"item_id": item_id}
    ```
     The value of item_id will be extracted from the URL path and passed as an argument to the function.

- Path parameters and query parameters:

    FastAPI supports both path parameters and query parameters. Path parameters are defined within the URL path itself, whereas query parameters are appended to the URL after a question mark (?).

    ```

    @app.get('/get_items/{item_id}')
    def read_item(item_id: int, q: str = None):
        if(q):
            result = {'item_id':item_id, 'q':q}
            return(result)
        return{'item_id':item_id}
    ```
- Request body:
    You can also define path operations that accept request bodies using models. 
    ```
    from pydantic import BaseModel

    class Item(BaseModel):
        name: str
        price: float
    ```
    save it as model.py

- Handle different HTTP methods:

    You can define path operations for different HTTP methods like GET, POST, PUT, DELETE, etc. For example:
    ```
    @app.post("/items")
    def create_item(item: Item):
        # Handle creating a new item
        return {"item": item}
    ```

    now send a POST request to the /items/ endpoint using a tool like cURL or an API testing tool like Postman. For example:

    ```
    {
        "name": "Example Item",
        "price": 9.99
    }
    ```
    For multiple values use list by importing typing package

    ```
    from typing import List
    @app.post('/multiple_items/')
    def create_items(items: List[Item]):
        return {"items" : items}
    ```

### Path Operation Order

1. Path operations with literal paths:

    These paths are defined explicitly and do not contain any path parameters. For example:
    ```
    @app.get("/items")
    def get_items():
        # Handle GET request for /items
        pass
    ```
2. Path operations with path parameters:

    These paths contain placeholders enclosed in curly braces ({}) to capture dynamic values from the URL. For example:
    ```
    @app.get("/items/{item_id}")
    def get_item(item_id: int):
        # Handle GET request for /items/{item_id}
        pass
    ```
3. Path operations with catch-all route:

    The catch-all route uses a path parameter with a default value of `Path(...)`, indicating that it can match any path. For example:
    ```
    from fastapi import Path

    @app.get("/items/{item_path:path}")
    def get_item_by_path(item_path: str = Path(...)):
        # Handle GET request for /items/{item_path}
        pass
    ```
    In this example, we have defined a path operation with a catch-all route using the `{item_path:path}` syntax. This route will match any path that starts with `"/items/"` and capture the remaining path as the item_path parameter.








