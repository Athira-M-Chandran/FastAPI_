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

### FastAPI - Path operations

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

### FastAPI - Intro to Postman

> Postman is a popular API development and testing tool that allows you to send HTTP requests and view the responses. It provides a user-friendly interface for interacting with APIs and simplifies the process of testing and debugging API endpoints.

1. [Install Postman](https://www.postman.com/)
2. Open Postman
3. Create a new request:
    To send a request to your FastAPI application, click on the "New" button in the top-left corner of the Postman interface. Choose the HTTP method (GET, POST, PUT, DELETE, etc.) you want to use for the request.
4. Enter the request URL:
    In the URL field, enter the endpoint URL of your FastAPI application. For example, if your FastAPI application is running on `http://localhost:8000` and you have defined a route like `@app.get("/items/{item_id}")`, you can enter `http://localhost:8000/items/123` in the URL field.
5. Set request headers (if required):
    If your FastAPI endpoint requires specific headers, you can set them in the Headers section of the Postman request. Click on the "Headers" tab and add the required headers as key-value pairs.
6. Set request body (if required):
    If your FastAPI endpoint expects a request body (e.g., for POST or PUT requests), you can set the body content in the "Body" section of the Postman request. Choose the appropriate format (e.g., JSON, form-data, etc.) and enter the required data.
7. Send the request:
    Once you have configured the request URL, headers, and body, click on the "Send" button to send the request to your FastAPI application.
8. View the response:
    Postman will display the response received from your FastAPI application. You can see the response status code, headers, and the response body. Use this information to verify that your FastAPI endpoints are functioning correctly.

> By using Postman, you can easily send different types of requests (GET, POST, PUT, DELETE) to your FastAPI application, test various scenarios, and examine the responses to ensure your API endpoints are working as expected. It is a powerful tool for API development and debugging.

### HTTP POST Requests

>HTTP POST requests are used to send data to a server and create a new resource on the server. In FastAPI, you can handle POST requests by defining a path operation decorated with @app.post() or @app.route() decorators. Here's an example:

```
from fastapi import FastAPI

app = FastAPI()

@app.post("/items")
async def create_item(item: Item):
    # Logic to create the item
    return {"message": "Item created successfully"}
```
In this example, we define a path operation using the ` @app.post()` decorator with the path `"/items"`. The `create_item()` function handles the POST request to `"/items"`. The function takes a parameter named item of type Item. The request body will be automatically parsed and validated based on the Item model or schema.

### Schema Validation with Pydantic

> Schema validation is the process of validating the structure, data types, and constraints of incoming data against a defined schema or model.

> In FastAPI, you can perform schema validation using Pydantic, a powerful data validation and serialization library. Pydantic allows you to define data models or schemas with annotated fields, which will be used to validate and parse incoming request data.

1. Define a Pydantic model: 
    Create a Pydantic model that represents the expected structure and data types of the incoming data. You can define fields with their respective data types and any additional validation rules or constraints.
    ```
    from pydantic import BaseModel

    class Item(BaseModel):
        name: str
        price: float
    ```
2. Use the model in the path operation:
     In your FastAPI path operation, specify the model as the parameter type. FastAPI will automatically validate and parse the incoming request data against the defined model.

     ```
     from fastapi import FastAPI

    app = FastAPI()

    @app.post("/items")
    def create_item(item: Item):
        # Logic to create the item
        return {"message": "Item created successfully"}
    ```
3. Handle validation errors: 
    If the incoming data does not match the defined schema, FastAPI will automatically return a validation error response with details about the validation errors. You can handle these errors and customize the response as needed.

    ```
    from fastapi import HTTPException

    try:
        # Code that can raise specific exceptions
        pass
    except ValueError as e:
        # Handle ValueError
        pass
    except ValidationError as e:
        # Handle ValidationError
        pass
    except HTTPException as e:
        # Handle HTTPException
        pass
    ```
[Refer](schema_validation.py)

## CRUD Operations

> Create, Read, Update, and Delete
1. Create (POST): To create a new resource, you can define a route with the HTTP method `POST`.
```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ItemCreate(BaseModel):
    name: str
    description: str

@app.post("/items")
async def create_item(item: ItemCreate):
    # Create a new item using the data from the request body
    # Perform any necessary operations, e.g., save to the database
    created_item = {"id": 1, "name": item.name, "description": item.description}
    return created_item
```

2. Read (GET): To retrieve existing resources, you can define routes with the HTTP method `GET`.

```
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    # Retrieve the item with the given item_id from the database
    item = {"id": item_id, "name": "Item 1", "description": "Description of Item 1"}
    return item
```

3. Update (PUT or PATCH): To update an existing resource, you can define routes with the HTTP methods `PUT` or `PATCH`
```
class ItemUpdate(BaseModel):
    name: str
    description: str

@app.put("/items/{item_id}")
async def update_item(item_id: int, item_update: ItemUpdate):
    # Update the item with the given item_id using the data from the request body
    # Perform any necessary operations, e.g., update in the database
    updated_item = {"id": item_id, "name": item_update.name, "description": item_update.description}
    return updated_item
```

4. Delete (DELETE): To delete an existing resource, you can define a route with the HTTP method `DELETE`. 
```
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    # Delete the item with the given item_id from the database
    return {"message": f"Item {item_id} deleted successfully"}
```
[Refer](crud_operations.py)

### Storing posts in Array

> To store posts in an array using FastAPI, you can define a route to handle the creation of posts and maintain a list to store the posts.

[Example](postsInArray.py)

### Creating posts

To create posts in FastAPI, you can use the HTTP POST method and define a route that handles the creation of posts.

[Example](create_post.py)

### Postman Collections & saving requests

> Postman Collections are a way to organize and store API requests for easy access and sharing. You can save your requests as collections in Postman to keep them organized and readily available for future use. 

1. Open Postman and make sure you have the request you want to save.

2. Click on the "Save" button located at the top right corner of the Postman interface.

3. In the pop-up window, select the desired collection or create a new one. Collections allow you to group related requests together.

4. Enter a name for the request and click on the "Save" button. This will save the request in the selected collection.

5. You can access your saved requests by clicking on the "Collections" tab in the left sidebar. Select the desired collection to see all the saved requests within it.

6. To make changes to a saved request, simply open the request from the collection, make the necessary modifications, and save it again.

By saving your requests as collections, you can easily organize and manage them, as well as share them with your team or others. Postman also provides features like variables, environments, and test scripts to further enhance your API testing and development workflow.

### Retrieve One Post

[Refer](retrieve.py)

### Changing response Status Codes

> In FastAPI, you can change the response status codes by using the appropriate status code constants provided by the fastapi.status module or by directly specifying the status code as an integer.

[Example](statusCodes.py)

### Deleting posts

[Refer](deletingPost.py)

### Updating posts
> To update posts in your FastAPI application, you can create a PUT or PATCH route that receives the updated post data and the post ID, and then updates the corresponding post in the list.

[Refer](updatingPost.py)

### Automatic Documentation
> You can access the documentation by visiting the `/docs` endpoint to view the Swagger UI or the `/redoc` endpoint to view the ReDoc UI.

For more Details- [click here](documentation.py)
 
 Make sure to customize the documentation routes as needed and adjust any other settings according to your application's requirements.

### FastAPI - Python packages

> FastAPI is a modern and high-performance web framework for building APIs with Python. While FastAPI itself is a powerful package, there are several additional Python packages that can complement and enhance your FastAPI development experience. 
1. **uvicorn** : A lightning-fast ASGI server that is recommended for running FastAPI applications in production. It provides excellent performance and supports asynchronous request handling.
2. **pydantic** : A data validation and parsing library that is heavily used in FastAPI for request and response validation. Pydantic allows you to define data models with type annotations and provides automatic data validation and serialization/deserialization capabilities.
3. **SQLAlchemy** : A popular SQL toolkit and Object-Relational Mapping (ORM) library for Python. SQLAlchemy makes it easy to work with databases in FastAPI applications by providing a high-level, Pythonic interface for interacting with databases.
4. **Alembic**: A database migration tool that works seamlessly with SQLAlchemy. Alembic allows you to manage and apply database schema changes over time, making it easier to evolve your database schema as your FastAPI application grows.
5. **OAuth2** : FastAPI has built-in support for OAuth2 authentication. The `oauthlib` and `python-jose` packages are commonly used to implement OAuth2 authentication flows with FastAPI.
6. **Redis**: A popular in-memory data store that can be used as a caching layer in FastAPI applications. The `aioredis` package provides an asynchronous Redis client that works well with FastAPI's async capabilities.
7. **JWT**: JSON Web Tokens (JWT) are a common authentication mechanism in web applications. The PyJWT package is widely used to handle JWT authentication in FastAPI applications.
8. **CORS** : Cross-Origin Resource Sharing (CORS) is an important aspect of web APIs. The `fastapi-cors` package provides middleware to handle CORS-related headers and configurations in FastAPI applications.
9. **FastAPI-utils** : A collection of utilities and tools that enhance FastAPI development. It includes features like dependency injection, reusable decorators, validation helpers, and more.

You can install these packages using pip, just like any other Python package, and incorporate them into your FastAPI projects as needed.

## Section 4: Databases - Database Intro

> A database is a structured collection of data that is organized, stored, and managed in a way that allows for efficient retrieval, manipulation, and analysis. Databases are used in various applications and industries to store and manage vast amounts of information.

The advantages of using databases include:
1. **Data Integrity**: Databases provide mechanisms to enforce data integrity rules, such as constraints, which ensure that the data is accurate, consistent, and reliable.

2. **Data Security**: Databases offer security features like user authentication, access control, and encryption to protect sensitive information from unauthorized access or modification.

3. **Data Consistency**: Databases support transactions, which allow multiple operations to be grouped together as a single unit. This ensures that all operations within a transaction are completed successfully or rolled back if any part fails, maintaining the consistency of the data.
 
4. **Data Scalability**: Databases can handle large amounts of data and support the scalability required to accommodate growing data volumes and user demands.

5. **Data Retrieval and Analysis**: Databases provide powerful querying capabilities, enabling users to retrieve, filter, and analyze data based on specific criteria, facilitating data-driven decision-making.

### Databases - Postgres Windows Install

[Install](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)

### Databases - Postgres Mac Install

[Install](https://www.postgresql.org/download/macosx/)

### Database Schema & Tables

1. **Database Schema**:

- A logical container or namespace for organizing database objects.
- Helps in avoiding naming conflicts and provides a logical separation.
- Can be used to group related tables, views, and other database objects together.
- Allows for better organization and management of the database.

2. **Database Table**:

- Represents a structured way to store and organize data.
- Consists of rows and columns.
- Each row represents a record or set of related data.
- Each column represents a specific attribute or field within that record.
- Tables have a defined structure, including column names, data types, and constraints.
- Tables are related to each other through keys and relationships.

When designing a database schema and creating tables, consider the following aspects:

1. Identify Entities and Relationships:
- Determine the entities or objects that need to be represented in the database.
- Define the relationships between these entities, such as one-to-one, one-to-many, or many-to-many.

2. Define Table Structure:
- Identify the attributes or properties of each entity.
- Determine the appropriate data types for each attribute (e.g., integer, text, date, etc.).
- Establish primary keys and unique constraints to ensure data integrity.
- Define foreign keys to establish relationships between tables.

3. Normalize Data:
- Apply normalization techniques to ensure data is organized efficiently and minimize redundancy.
- Normalization helps avoid data anomalies and improve database performance.

4. Establish Constraints and Indexes:
- Define constraints, such as not-null, unique, and check constraints, to enforce data integrity rules.
- Create indexes on columns that are frequently used in search or join operations for improved query performance.

5. Consider Security and Access Control:
- Implement appropriate access control mechanisms to restrict user privileges and protect sensitive data.
- Set up proper authentication and authorization measures to ensure data security.

### Managing Postgres with PgAdmin GUI

> Managing PostgreSQL with the pgAdmin GUI provides a user-friendly interface for performing various administrative tasks on your PostgreSQL database.

1. **Launch pgAdmin** : 

    Firstly, we will open the pgAdmin application. For this, we will enter `pgAdmin` into the search bar of our system
2. **Create a server** :

    After that, we will right-click on the Servers node and select the `Register` → `Server… menu` to create a server
3. **Provide the server name** :

    After selecting the `Server` option, the `Create-Server` window will be opened, where we enter the server name in the Name column, for example, `PostgreSQL1` and then we will click on the `Connection` tab,
4. **Provide the host and password** :

    After clicking on the `Connection` tab, we will provide the details of the `host` (eg. localhost) and `password` for the Postgres user, and after that, we will click on the `Save` button.
5. **Expanding the server** :

    In the next step, we will click on the `Servers` node to expand the server. And PostgreSQL has a database named `Postgres` by default
6. **Open the Query tool** :

    Now, we will open the query tool by selecting the menu item `Tool` → `Query Tool`, or we can directly click the `query tool` icon nearby Browser
7. **Enter the command in the Query editor** :

    Enter the below command in the Query Editor and click on the `Execute` button.

    ```
    Select Version();
    ```
### Databases - Your first SQL Query

1. **Launch the SQL Client**: Open your preferred SQL client or interface. This can be a command-line tool, a GUI-based application, or a web-based interface depending on your setup and preferences.

2. **Connect to the Database**: In your SQL client, establish a connection to the database where you want to execute the query. Provide the necessary details such as the server address, port number, database name, username, and password. Once connected, you should see a prompt or interface ready to accept SQL commands.

3. **Write the SQL Query**: Now it's time to write your SQL query. SQL queries are written using the SQL (Structured Query Language) syntax. Here's an example of how you can create a "customers" table:

```
CREATE TABLE customers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  phone VARCHAR(20)
);

```
To add entries to the "customers" table, you can use the INSERT INTO statement in SQL. Here's an example of how you can insert some sample data into the table:

```
INSERT INTO customers (name, email, phone)
VALUES ('John Doe', 'johndoe@example.com', '123-456-7890');

INSERT INTO customers (name, email, phone)
VALUES ('Jane Smith', 'janesmith@example.com', '987-654-3210');

INSERT INTO customers (name, email, phone)
VALUES ('Alice Johnson', 'alicejohnson@example.com', '555-123-4567');
```

 run the `SELECT * FROM customers;` query again to retrieve all the entries and verify that they have been successfully added to the table.

 ### Databases - Filter results with "where" keyword

 ```
select * 
from customers
where id=2;
```
 Here is an overview of some commonly used WHERE clauses and operators in PostgreSQL:

 
1. *Comparison Operators:*

- `=`: Equal to
- `<>` or `!=`: Not equal to
- `<`: Less than
- `>`: Greater than
- `<=`: Less than or equal to
- `>=`: Greater than or equal to
- `IS NULL`: Value is null
- `IS NOT NULL`: Value is not null

2. *Logical Operators:*

- AND: Both conditions must be true
- OR: Either condition must be true
- NOT: Negates a condition

3. *Pattern Matching Operators:*

- LIKE: Matches a pattern
- ILIKE: Matches a pattern case-insensitively
- SIMILAR TO: Matches a regular expression pattern

4. *Range Operators:*

- BETWEEN: Value is within a range
- NOT BETWEEN: Value is not within a range
- IN: Value matches any value in a list
- NOT IN: Value does not match any value in a list

5. *String Matching Operators:*

- ~ or ~*: Matches a regular expression pattern (case-sensitive or case-insensitive)
- !~ or !~*: Does not match a regular expression pattern (case-sensitive or case-insensitive)

6. *Array Operators:*

- ANY: Value matches any value in an array
- ALL: Value matches all values in an array

7. *Subqueries:*

- IN: Value is in the result of a subquery
- NOT IN: Value is not in the result of a subquery
- EXISTS: Checks if a subquery returns any rows


### Databases - SQL Operators

1. **Arithmetic Operators:** 
- `+` : Addition
- `-` : Subtraction
- `*` : Multiplication
- `%` : Modulo
- `+` (unary): positive value
- `-` (unary) :Negative value
2. **Comparison Operator**
- `=` : Equal to
- `<>` or `!=` : Not equal to
- `<` : Less than
- `>` : Greater than
- `<=` : Less than or equal to
- `>=` : Greater than or equal to
- `BETWEEN` : Value is within a range
- `LIKE` : Pattern matching(with wildcard characters)
- `IN` : Value matches any values in a list
- `IS NULL` : Value is null
- `IS NOT NULL` : value is not null
3. **Logical operators**
- `AND` - Logical AND
- `OR` - Logical OR
- `NOT` - LogicalNOT
- `ALL` - TRUE if all of the subquery values meet the condition
- `ANY` - TRUE if any of the subquery values meet the condition
- `EXISTS` - TRUE if subquery returns one or more records
- `SOME` - TRUE if any ofthe subquery values meet the condition
4. **String Operators**
- `||` - Concatenation
- `LIKE` - Pattern matching
- `ILIKE` - Case insensitive pattern matching
- `SUBSTRING` - Extracts a substring from a string
5. **Set Operations**
- `UNION` -Combines result set and removes duplicates
- `UNION ALL` - Combines results sets without removing duplicates
- `INTERSECT` -Retrieves common rows from two results sets
- `EXCEPT` or `MINUS` - Retrieves rows from the first result set that are not in the second result set.
6. **NULL- related Operators**
- `IS NULL` : Checks if a value is null
- `IS NOT NULL` : Checks if a value is not NULL
- `COALESCE` : Returns the first non-null value from a list
7. **Bitwise Operator**
-  `&` - Bitwise AND
- `|` - Bitwise OR
- `^` - Bitwise Exculsive OR

### Databases - IN Keyword

> In SQL, the `IN` keyword is used to check if a value matches any value in a list or a subquery. It is often used in the `WHERE` clause to filter rows based on a specified set of values.

Examples

- Using a list of values:

`SELECT * FROM customers WHERE country IN ('USA', 'Canada', 'UK');`

    This query retrieves all rows from the "customers" table where the "country" column has a value that matches any of the values in the list ('USA', 'Canada', 'UK').

- Using a subquery:

`SELECT * FROM orders WHERE customer_id IN (SELECT id FROM customers WHERE country = 'USA');`

    This query retrieves all rows from the "orders" table where the "customer_id" column has a value that matches any of the IDs returned by the subquery.

### Databases - Pattern matching with LIKE keyword

> In SQL, the `LIKE` keyword is used for pattern matching within character strings. It allows you to search for values that match a specific pattern using wildcard characters.

1. **Using wildcard characters** :
- `%` - Matches any sequence of characters
- `_` - Matches any single character

Examples:

`SELECT * FROM customers WHERE name LIKE 'J%';`

2. **Combining wildcard characters:**

`SELECT * FROM customers WHERE name LIKE 'S_m_';`

3. **Using character ranges:** :

`SELECT * FROM customers WHERE name LIKE '[A-C]%';`

`SELECT * FROM customers WHERE name ~ '^[A-C].*';` In PostgreSQL

### Databases - Ordering Results

> In SQL, you can order the results of a query using the `ORDER BY` clause. The `ORDER BY` clause allows you to specify one or more columns by which the result set should be sorted, either in ascending (default) or descending order.

```
SELECT column1, column2, ...
FROM table_name
ORDER BY column1 [ASC|DESC], column2 [ASC|DESC], ...
```

example:

```
SELECT * FROM customers
ORDER BY age DESC, name ASC;
```
### Databases - LIMIT & OFFSET

> In SQL, the `LIMIT` and `OFFSET` clauses are used to control the number of rows returned by a query and to skip a certain number of rows, respectively. These clauses are often used together to implement pagination or to retrieve a subset of results from a larger dataset.

1. **LIMIT**: The `LIMIT` clause is used to specify the maximum number of rows to be returned by a query. It restricts the result set to a certain number of rows. The syntax for the `LIMIT` clause is as follows:

```
SELECT column1, column2, ...
FROM table_name
LIMIT number_of_rows;
```

example 
```
SELECT * FROM customers
LIMIT 5;
```
2. `OFFSET`: The `OFFSET` clause is used to skip a specified number of rows before starting to return the rows. It is often used in combination with `LIMIT` to implement pagination. The syntax for the `OFFSET` clause is as follows:
```
SELECT column1, column2, ...
FROM table_name
OFFSET number_of_rows_to_skip;
```
Example
```
SELECT * FROM customers
OFFSET 5
LIMIT 5;
```

### Databases - Inserting Data

Create table - 
```
CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    age INT
);
```

Inserting data

>When working with databases, inserting data is a common operation that allows you to add new records to a table. In SQL, you can use the `INSERT INTO` statement to insert data into a table. Here's the basic syntax:
```
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

### Databases - Deleting Data

> When working with databases, deleting data is a common operation to remove records from a table. In SQL, you can use the `DELETE` statement to delete data from a table. Here's the basic syntax:
```
DELETE FROM table_name
WHERE condition;
```
example :
```
DELETE FROM customers
WHERE age >= 30 AND city = 'New York';
```

### Databases - Updating Data

> When working with databases, updating data is a common operation that allows you to modify existing records in a table. In SQL, you can use the `UPDATE` statement to update data in a table. Here's the basic syntax:
```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

```
UPDATE customers
SET email = 'newemail@example.com', age = 35
WHERE customer_id = 3;
RETURNING *;
```
> Use the `RETURNING` clause to return the updated rows from the UPDATE statement

## Section 5: Python + Raw SQL - Setup App Database

To set up a database for your Python application, you'll need to perform a few steps. Here's a general outline of the process:

1. *Install the required database driver*: Depending on the database you're using, you'll need to install the appropriate Python library or driver. For example, if you're using PostgreSQL, you can install the `psycopg2` library by running `pip install psycopg2`.
2. *Connect to the database* : In your Python application, you'll need to establish a connection to the database using the appropriate connection parameters. These parameters typically include the host, port, database name, username, and password. Here's an example of connecting to a PostgreSQL database:
```
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="mydatabase",
    user="myuser",
    password="mypassword"
)
```

3. *Create a cursor*: After establishing a connection, you'll need to create a cursor object. The cursor allows you to execute SQL queries and interact with the database.

```
cursor = conn.cursor()
```
4. *Execute SQL queries*: With the cursor, you can execute SQL queries to create tables, insert data, update records, and perform other operations. Here's an example of creating a table:

```
create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50),
        email VARCHAR(100),
        password VARCHAR(100)
    );
"""

cursor.execute(create_table_query)
```
5. *Commit the changes*: After executing the SQL queries, you need to commit the changes to make them persistent in the database.
```
conn.commit()
```
6. *Close the cursor and connection*: Once you're done working with the database, it's important to close the cursor and connection to release the resources.
```
cursor.close()
conn.close()
```

### Python + Raw SQL - Connecting to database w/ Python

To connect to a database using Python and execute raw SQL queries, you can use the appropriate database library or driver for the database you're working with. Here are examples of connecting to different databases using raw SQL in Python:

1. Connecting to PostgreSQL using psycopg2:

```
import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="mydatabase",
    user="myuser",
    password="mypassword"
)

# Create a cursor
cursor = conn.cursor()

# Execute SQL queries
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Commit changes and close the cursor and connection
conn.commit()
cursor.close()
conn.close()
```

2. Connecting to MySQL using mysql-connector-python:

```
import mysql.connector

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    port="3306",
    database="mydatabase",
    user="myuser",
    password="mypassword"
)

# Create a cursor
cursor = conn.cursor()

# Execute SQL queries
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Commit changes and close the cursor and connection
conn.commit()
cursor.close()
conn.close()
```

3. Connecting to SQLite using sqlite3 (built-in module in Python):

```
import sqlite3

# Establish a connection to the SQLite database
conn = sqlite3.connect("mydatabase.db")

# Create a cursor
cursor = conn.cursor()

# Execute SQL queries
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Commit changes and close the cursor and connection
conn.commit()
cursor.close()
conn.close()
```
### Python + Raw SQL - Retrieving Posts

```
import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="mydatabase",
    user="myuser",
    password="mypassword"
)

# Create a cursor
cursor = conn.cursor()

# Execute the SELECT query to retrieve posts
select_query = "SELECT * FROM posts;"
cursor.execute(select_query)

# Fetch all rows from the result
rows = cursor.fetchall()

# Process the retrieved posts
for row in rows:
    post_id = row[0]
    title = row[1]
    content = row[2]
    # Perform any required operations with the retrieved data
    print(f"Post ID: {post_id}")
    print(f"Title: {title}")
    print(f"Content: {content}")
    print()

# Commit changes and close the cursor and connection
conn.commit()
cursor.close()
conn.close()
```

### Python + Raw SQL - Creating Post

```
import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="mydatabase",
    user="myuser",
    password="mypassword"
)

# Create a cursor
cursor = conn.cursor()

# Define the SQL statement for inserting a new post
insert_query = """
    INSERT INTO posts (title, content)
    VALUES (%s, %s)
"""

# Define the data for the new post
post_title = "My First Post"
post_content = "This is the content of my first post."

# Execute the INSERT statement with the data
cursor.execute(insert_query, (post_title, post_content))

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
```

[Refer](db1.py)

### Python + Raw SQL - Get One Post
```
import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="mydatabase",
    user="myuser",
    password="mypassword"
)

# Create a cursor
cursor = conn.cursor()

# Define the SQL statement for retrieving a single post
select_query = """
    SELECT * FROM posts
    WHERE post_id = %s
"""

# Define the ID of the post you want to retrieve
post_id = 1

# Execute the SELECT statement with the post ID
cursor.execute(select_query, (post_id,))

# Fetch the first row from the result
row = cursor.fetchone()

# Process the retrieved post
if row:
    post_id = row[0]
    title = row[1]
    content = row[2]
    # Perform any required operations with the retrieved data
    print(f"Post ID: {post_id}")
    print(f"Title: {title}")
    print(f"Content: {content}")
else:
    print("Post not found.")

# Close the cursor and connection
cursor.close()
conn.close()
```
[Refer](db2_getonepost.py)

### Python + Raw SQL - Delete Post
```
import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="mydatabase",
    user="myuser",
    password="mypassword"
)

# Create a cursor
cursor = conn.cursor()

# Define the SQL statement for deleting a post by its ID
delete_query = """
    DELETE FROM posts
    WHERE post_id = %s
"""

# Define the ID of the post to be deleted
post_id = 1

# Execute the DELETE statement with the post ID
cursor.execute(delete_query, (post_id,))

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
```
[Refer](db3_delete.py)

### Python + Raw SQL - Update Post

```
import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="mydatabase",
    user="myuser",
    password="mypassword"
)

# Create a cursor
cursor = conn.cursor()

# Define the SQL statement for updating a post by its ID
update_query = """
    UPDATE posts
    SET title = %s, content = %s
    WHERE post_id = %s
"""

# Define the new values for the post
new_title = "Updated Title"
new_content = "Updated content of the post"
post_id = 1

# Execute the UPDATE statement with the new values and post ID
cursor.execute(update_query, (new_title, new_content, post_id))

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
```
[Refer](db4_update.py)

[Refer(using api)](database_api.py)

## Section 6: ORMs - ORM intro

> ORM stands for **Object-Relational Mapping**. It is a programming technique used to map objects in an object-oriented programming language (like Python) to database tables in a relational database management system (such as MySQL, PostgreSQL, or SQLite). ORM provides a higher-level abstraction that allows developers to interact with databases using objects and their relationships, rather than writing raw SQL queries.

With an ORM, you can define your database schema and relationships using classes and objects, and the ORM library handles the mapping and translation of these objects to the corresponding database tables and queries. The ORM takes care of generating the SQL queries, executing them, and retrieving the results, making database operations more intuitive and easier to work with.

Here are some benefits of using an ORM:

1. *Simplified database interactions*: With ORM, you can perform database operations using familiar programming language constructs, such as classes, objects, and methods. This abstraction simplifies the code and makes it more readable and maintainable.

2. *Cross-database compatibility*: ORM frameworks often support multiple database systems, allowing you to switch between different databases without changing your code significantly.

3. *Data modeling* : ORM frameworks provide tools and techniques to define the structure of your data in the form of models or classes. These models represent database tables and their relationships, making it easier to manage and maintain the data schema.

4. *Query abstraction*: ORM frameworks typically offer a high-level query language or API that abstracts away the underlying SQL syntax. This allows you to write database queries using object-oriented syntax, making them more concise and less error-prone.

5. *Automatic data mapping*: ORM frameworks handle the mapping between database tables and objects automatically. They map the columns of a table to the attributes of an object, enabling seamless data retrieval and manipulation.

Popular ORM frameworks in Python include **SQLAlchemy**, **Django ORM** (part of the Django web framework), and **Peewee**. Each ORM has its own features, syntax, and usage patterns, so it's important to choose the one that best fits your project requirements.

With ORM, you can focus more on your application's business logic and less on the low-level details of database operations. It simplifies database interactions, improves code organization, and enhances developer productivity.

### ORMs - SQLALCHEMY setup

1. *Install SQLAlchemy*: You can install SQLAlchemy using pip, the Python package manager. Open your terminal or command prompt and run the following command:
```
pip install SQLAlchemy
```

2. *Import SQLAlchemy*: In your Python script or application, import the SQLAlchemy module to use its functionalities. Typically, you'll import it as follows:
```
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
```

3. *Establish a Database Connection*: Create an engine object that represents the database connection. The engine object defines the database URL and other configuration details. For example, to connect to a PostgreSQL database locally, you can use the following code:
```
engine = create_engine('postgresql://username:password@localhost/mydatabase')
```

4. *Define a Base Model*: In SQLAlchemy, you typically define a base model class that other models will inherit from. This base model class will provide common functionality and configuration. For example:
```
Base = declarative_base()
```

5. *Define Models*: Define your database models by creating Python classes that inherit from the base model class. Each class represents a table in the database, and each attribute represents a column. For example:
```
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100))
```

6. *Create Tables*: Once you have defined your models, you need to create the corresponding tables in the database. SQLAlchemy provides a feature called "schema generation" that can automatically create the tables based on your model definitions. To create the tables, use the following code:
```
Base.metadata.create_all(engine)

```

7. *Create a Session*: To interact with the database, you need to create a session object. The session object acts as a middleman between your code and the database. Use the following code to create a session:
```
Session = sessionmaker(bind=engine)
session = Session()
```

[Refer](sqlalchemy_setup.py)

### ORMs - Adding CreatedAt Column

> If the table already exists and you want to add the created_at column to the existing table, you can use a database migration tool like Alembic to apply the changes.

1. Install Alembic:
```
pip install alembic
```
2. Set up Alembic: 

Initialize Alembic by running the following command in your project directory:
```
alembic init alembic
```

This will create an `alembic` directory with configuration files and folders.
3. Create a migration script:

Inside the `alembic/versions` directory, create a new migration script. The name of the script should reflect the purpose of the migration. For example, you can name it something like `add_created_at_column.py`. Open the script file and define the migration operations.

Here's an example migration script that adds the created_at column to an existing table:
```
from alembic import op
import sqlalchemy as sa

from sqlalchemy import create_engine
import urllib.parse
from datetime import datetime

revision_id = datetime.now().strftime("%Y%m%d%H%M%S")
create_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Set the revision ID and create date
revision = 'your_revision_id'
down_revision = None
create_date = 'your_create_date'

password = urllib.parse.quote_plus('a@bcd')
# Create the connection string with the encoded password
connection_string = f'postgresql://user:{password}@localhost/dbname'

# Create the engine
engine = create_engine(connection_string)

# The table name and column name need to be adjusted according to your existing table structure
table_name = 'your_table'
column_name = 'created_at'


def upgrade():
    op.add_column(table_name, sa.Column(column_name, sa.DateTime))


def downgrade():
    op.drop_column(table_name, column_name)
```

4. Edit the alembic.ini file in the alembic directory. Update the sqlalchemy.url setting with your database connection string. For example:

```
sqlalchemy.url = postgresql://your_user:your-password@localhost/your-databasename
```

5. Run the migration:
```
alembic upgrade head
```
[refer](alembic/versions/add_created_at_column.py)

### ORMs - Create Posts

1. *Import the necessary modules and classes:*
```
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Post  # Assuming you have defined a Post model class
```

2. *Create an engine to connect to your database:*
```
engine = create_engine('postgresql://user:password@localhost/database_name')
```
3. *Create a session factory:*
```
Session = sessionmaker(bind=engine)
```

4. *Create a session:*
```
session = Session()
```
5. *Create new posts:*
```
post1 = Post(title='First Post', content='This is the content of the first post.')
post2 = Post(title='Second Post', content='This is the content of the second post.')

```
6. *Add the new posts to the session:*
```
session.add(post1)
session.add(post2)
```
7. *Commit the changes to the database:*
```
session.commit()
```
8. *Close the session:*
```
session.close()
```
[Refer](sqlalchemy_post.py)

### ORMs - Get All Posts

To retrieve all posts from a database table using an ORM like SQLAlchemy, you can follow these steps:

1. *Import the necessary modules and classes:*
```
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Post  # Assuming you have defined a Post model class

```
2. *Create an engine to connect to your database:*
```
engine = create_engine('postgresql://user:password@localhost/database_name')
```
3. *Create a session factory:*
```
Session = sessionmaker(bind=engine)
```
4. *Create a session:*
```
session = Session()
```
5. *Retrieve all posts from the database:*
```
posts = session.query(Post).all()
```
This query retrieves all rows from the `Post` table and returns them as a list of `Post` objects.
6. *Access the retrieved posts:*
```
for post in posts:
    print(post.title)
    print(post.content)
    print("---")
```
7. *Close the session:*
```
session.close()
```
[refer](sqlalchemy_get.py)

### ORMs - Get Post by ID

1. *Import the necessary modules and classes:*
```
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Post  # Assuming you have defined a Post model class

```
2. *Create an engine to connect to your database:*
```
engine = create_engine('postgresql://user:password@localhost/database_name')
```
3. *Create a session factory:*
```
Session = sessionmaker(bind=engine)
```
4. *Create a session:*
```
session = Session()
```
5. *Retrieve a post by its ID:*
```
post_id = 1  # Replace 1 with the desired ID
post = session.query(Post).get(post_id)
```
6. *Access the retrieved post:*
```
if post is not None:
    print(post.title)
    print(post.content)
else:
    print("Post not found.")
```
7. *Close the session:*
```
session.close()
```
[Refer](sqlalchemy_getbyID.py)

### ORMs - Delete Post

1. *Import the necessary modules and classes:*
```
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Post  # Assuming you have defined a Post model class

```
2. *Create an engine to connect to your database:*
```
engine = create_engine('postgresql://user:password@localhost/database_name')
```
3. *Create a session factory:*
```
Session = sessionmaker(bind=engine)
```
4. *Create a session:*
```
session = Session()
```
5. *Retrieve a post by its ID:*
```
post_id = 1  # Replace 1 with the desired ID
post = session.query(Post).get(post_id)
```
6. *Query and delete the post by its ID*
```
if post is not None:
    session.delete(post)
    print("Post deleted successfully)
else:
    print("Post not found.")
```
7. *Close the session:*
```
session.close()
```
[Refer](sqlalchemy_delete.py)

### ORMs - Update Post
1. *Import the necessary modules and classes:*
```
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Post  # Assuming you have defined a Post model class

```
2. *Create an engine to connect to your database:*
```
engine = create_engine('postgresql://user:password@localhost/database_name')
```
3. *Create a session factory:*
```
Session = sessionmaker(bind=engine)
```
4. *Create a session:*
```
session = Session()
```
5. *Retrieve a post by its ID:*
```
post_id = 1  # Replace 1 with the desired ID
post = session.query(Post).get(post_id)
```
6. *Update the post by its ID:*
```
if post is not None:
    post.title = "New Title"
    post.content = "New Content"
    session.commit()
    print("Post updated successfully.")
else:
    print("Post not found.")
```
7. *Close the session:*
```
session.close()
```
[Refer](sqlalchemy_delete.py)

#### Query with join
query = session.query(User, Post).join(Post)

#### Query with condition
query = session.query(User).filter(User.username.like('A%'))

#### Perform the aggregation and grouping
query = session.query(User.username, func.avg(User.age)).group_by(User.username)

## Section 7: Pydantic Models - Pydantic vs ORM Models

#### Pydantic Models:
- Pydantic is a **data validation** and **serialization library** that helps you define data schemas and perform input validation.

- Pydantic models are primarily used for **input validation**, **data parsing**, and **serialization/deserialization** of data in APIs or other data processing tasks.

- Pydantic models **define the structure and constraints of the data**, including data types, required fields, default values, and validation rules.

- Pydantic models provide powerful validation features such as **type validation**, **field validation**, and **custom validation** functions.

- Pydantic models are **not directly connected to a database**. They focus on input/output operations and data transformation rather than persisting data in a database.

- Pydantic models are typically **used in API frameworks** like FastAPI, where they help validate incoming requests and automatically parse and serialize data.

#### ORM Models:

- ORM (Object-Relational Mapping) models are **used for mapping database tables to Python objects**.
- ORM models represent the **structure of database tables** and provide an abstraction layer that allows you to interact with the database using Python objects and methods.
- ORM models define the **schema of the database tables**, including fields, relationships, constraints, and indexes.
- ORM models provide features for **querying, creating, updating, and deleting data in the database** using object-oriented syntax.
- ORM models are tightly coupled to the underlying database and provide a way to **perform complex database operations** using Python code.
- ORM models are commonly used in frameworks like SQLAlchemy, Django ORM, or Peewee for interacting with relational databases.

> In summary, Pydantic models focus on data validation and serialization/deserialization tasks, while ORM models focus on mapping database tables to Python objects and providing database operations. Both Pydantic and ORM models have their own use cases and can be used together in an application to handle different aspects of data validation, serialization, and database interaction.

### Pydantic Models - Pydantic Models Deep Dive

1. **Defining Pydantic Models:**

> To create a Pydantic model, you need to define a Python class that inherits from the pydantic.BaseModel class. Inside the class, you define attributes with their types, optionally specifying additional validation rules using Pydantic's field types and validators.
```
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
    email: str
```

2. **Field Types:**

Pydantic provides various field types that can be used to define the attributes of a model. Some commonly used field types include:

- str: Represents a string.
- int: Represents an integer.
- float: Represents a floating-point number.
- bool: Represents a boolean value.
- List[Type]: Represents a list of elements of a specified type.
- Dict[str, Type]: Represents a dictionary with string keys and values of a specified type.
- datetime.datetime: Represents a date and time.

These field types ensure that the provided input data matches the expected type during validation.

3. **Field Validation:**

Pydantic allows you to apply validation rules to the fields in your models. You can use decorators like `@validator` and `@root_validator` to define custom validation functions. Pydantic also provides built-in validators such as `EmailStr`, `UrlStr`, `Length`, and more.

```
from pydantic import BaseModel, EmailStr

class Person(BaseModel):
    name: str
    age: int
    email: EmailStr

    @validator('age')
    def check_age(cls, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        return age
```
4. **Model Validation:**

To validate input data against a Pydantic model, you can create an instance of the model and pass the input data as a dictionary. Pydantic will validate the data, perform type conversions, and raise validation errors if the data does not conform to the model's schema.
```
person_data = {
    "name": "John Doe",
    "age": 25,
    "email": "john.doe@example.com"
}

person = Person(**person_data)
```
If the input data is invalid, a `ValidationError` will be raised, providing details about the validation errors.
5. **Data Serialization:**

Pydantic models support automatic serialization to and deserialization from various formats, including JSON, dictionaries, and more. You can use the model's `dict()` method to serialize the model instance to a dictionary, or the `json()` method to serialize it to a JSON string.
```
person_dict = person.dict()
person_json = person.json()
```
Pydantic also provides the `parse_obj()` and `parse_raw()` methods to create model instances from dictionaries or raw input data, respectively.

6. **Data Conversion and Coercion:**
- Pydantic models can automatically convert and coerce data to the specified types.
```
person_data = {
    "name": "John Doe",
    "age": "25",  # str value
    "price": 99  # Coerced from int to float
}

person = Person(**person_data)
print(person.age)  # Output: 25 (converted to int)
print(person.price)  # Output: 99.0 (coerced to float)
```
- Built-in type conversion includes parsing strings to integers, floats, booleans, dates, and times.
- Strict Data Validation.
```
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str
    price: float

    class Config:
        strict = True

product_data = {
    "name": "Product 1",
    "price": "99"  # Not directly assignable to float
}

product = Product(**product_data)  # Raises a ValidationError
```
- You can define custom conversion functions using the `@root_validator` decorator.

7. **Nested Models and Relationships:**

- Pydantic models can have nested models to represent complex data structures and relationships.
- Use the nested model's class name as the attribute type to define a relationship between models.
```
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class Person(BaseModel):
    name: str
    age: int
    address: Address
```
In this example, the `Person` model has a nested `Address` model as a field. When creating a `Person` instance, you can provide the address details as a nested dictionary.
- Pydantic supports one-to-one, one-to-many, and many-to-many relationships between models.

a. *One-to-One Relationship*: each instance of one model is associated with exactly one instance of another model.
```
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

class Profile(BaseModel):
    user: User
    bio: str
```
In this example, the `Profile` model has a one-to-one relationship with the `User` model, where each profile is associated with a single user.

b. *One-to-Many Relationship*: each instance of one model can be associated with multiple instances of another model.
```
from pydantic import BaseModel

class Author(BaseModel):
    name: str

class Book(BaseModel):
    title: str
    authors: List[Author]
```
c. *Many-to-Many Relationship:* instances of one model can be associated with multiple instances of another model, and vice versa.

```
from pydantic import BaseModel

class Category(BaseModel):
    name: str

class Product(BaseModel):
    name: str
    categories: List[Category]
```
In this example, the `Product` model has a many-to-many relationship with the `Category` model, where each product can be associated with multiple categories, and each category can be associated with multiple products.

Accessing Nested Models and Relationships:

When working with nested models and relationships, you can access the nested fields and relationships using dot notation.
```
person = Person(name="John", age=30, address={"street": "123 Main St", "city": "New York", "postal_code": "12345"})
print(person.name)  # Output: John
print(person.address.city)  # Output: New York
```
using dot notation.
```
book = Book(title="My Book", authors=[{"name": "Author 1"}, {"name": "Author 2"}])
print(book.title)  # Output: My Book
print(book.authors[0].name)  # Output: Author 1
```
8. **Customizing Pydantic Models:**

- You can customize Pydantic models by overriding built-in methods or adding custom methods and properties.

### Pydantic Models - Response Model

To define a Pydantic model as a response model, follow these steps:

1. Import the necessary modules:
```
from fastapi import FastAPI
from pydantic import BaseModel
```
2. Define the Pydantic model for the response:
```
class Item(BaseModel):
    name: str
    price: float
```
3. Create a FastAPI application instance:
```
app = FastAPI()
```
4. Define an endpoint that returns the response model:
```
@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = fetch_item_from_database(item_id)
    return item
```
In this example, the `read_item` endpoint returns an `Item` object, which is a Pydantic model. The response data will be automatically serialized to JSON based on the structure of the `Item` model.

If you want to explicitly specify the response model in the endpoint function signature, you can use the `response_model` parameter:
```
from fastapi import Response

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    item = fetch_item_from_database(item_id)
    return item
```
Note that when using `response_model`, FastAPI will automatically validate the returned data against the specified response model and raise an error if the data does not match the model's structure or validation rules.

> By using Pydantic models as response models in FastAPI, you can ensure consistent and well-structured responses from your API endpoints. The response data will be automatically serialized, and you can take advantage of Pydantic's powerful validation capabilities to ensure the correctness and integrity of the returned data.

## Section 8: Authentication & Users - Creating Users Table

```
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

[Refer](auth_create_users.py)

### Authentication & Users - User Registration Path Operation

[Refer](auth_user_reg.py)

### Authentication & Users - Hashing User Passwords

> When it comes to user authentication, it is crucial to securely store user passwords to protect them from unauthorized access. One common practice is to hash passwords using a strong **cryptographic hashing algorithm** combined with a random salt.

1. Generate a random salt for each user:
- When a user creates an account or changes their password, generate a random string of sufficient length (e.g., 16 bytes) to serve as the salt.
- The salt should be unique for each user and stored alongside their hashed password.
2. Concatenate the user's password with the salt:
- Append the salt to the user's password, forming a new string.
3. Apply a secure cryptographic hash function:
- Use a strong hashing algorithm like `bcrypt`, `Argon2`, or `scrypt` to hash the concatenated string.
- Ensure that the algorithm is well-suited for password hashing, designed to be computationally expensive to `thwart brute-force attacks`.
4. Store the salt and hashed password in the database:
- Save both the salt and the resulting hashed password in the user's record in the database.
- The salt and hashed password should be stored in separate columns.

When authenticating a user, follow these steps:
1. Retrieve the user's salt and hashed password from the database based on their username or email.
2. Concatenate the provided password with the stored salt.
3. Apply the same cryptographic hash function to the concatenated string.
4. Compare the resulting hash with the stored hashed password.
5. If the hashes match, the provided password is correct, and the user is authenticated.


Here's an example using the bcrypt library to hash passwords in your authentication system:

1. Install the `bcrypt` library: ```pip install bcrypt```
2. Import the `bcrypt` module in your code: ```import bcrypt```
3. Modify your `User` model to include a hashed password field:
```
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    # ...

    password_hash = Column(String(100), nullable=False)
```
4. Update the registration path operation to hash the user password before storing it:
```
@app.post("/register")
def register_users(user_data_list: List[UserRegistrationRequest]):
    with Session() as session:
        for user_data in user_data_list:
            username = user_data.username
            password = user_data.password
            email = user_data.email

            # Hash the password
            password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

            user = User(username=username, email=email, password_hash=password_hash)

            session.add(user)

        session.commit()
```
### Authentication & Users - Refractor Hashing Logic
```
import bcrypt

class User(Base):
    # ... other column definitions ...

    def set_password(self, password):
        password_bytes = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        self.password = hashed_password.decode('utf-8')
```
In this updated implementation, the `password` provided is encoded to bytes using the `UTF-8` encoding. The `bcrypt.hashpw()` function is then used to generate the hashed password using the password bytes and a randomly generated salt. The resulting hashed password, which is in bytes, is decoded back to a UTF-8 encoded string and assigned to the `self.password` attribute of the User instance.

[Refer](auth_model_users.py)

### Authentication & Users - Get User by ID

[Refer](auth_user_get.py)

### Authentication & Users - FastAPI Routers

> In FastAPI, you can use routers to **organize** your API routes into separate modules or files. Routers allow you to group related endpoints together and **encapsulate** their functionality. Here's an example of how to create a router for user-related operations:

1. Create a new file named `user_router.py`.
2. Inside `user_router.py`, import the necessary dependencies:
```
from fastapi import APIRouter
from fastapi import HTTPException

from auth_model_users import User
from auth_user_connection import Session
```
3. Create an instance of `APIRouter`:
```
router = APIRouter()
```
4. Define your user-related endpoints using the router. For example, you can define a route to get a user by ID:
```
@router.get("/users/{user_id}")
def get_user(user_id: int):
    with Session() as session:
        user = session.query(User).get(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
```
You can add more endpoints for user registration, authentication, update, delete, etc.

5. Save the file.

To use the router in your main FastAPI application, import it and include it in the `app` instance:
```
from fastapi import FastAPI
from user_router import router

app = FastAPI()

app.include_router(router)
```

The main benefit of using routers in FastAPI is organization and modularity. Here are some advantages of using routers:

- **Modularity**: Routers allow you to organize your API routes into separate modules or files. This can improve code maintainability and make it easier to understand and navigate the codebase. Each router can encapsulate a specific set of endpoints related to a particular functionality or resource.

- **Separation of Concerns**: Routers help you separate different parts of your API into logical units. For example, you can have separate routers for user-related endpoints, authentication endpoints, admin endpoints, etc. This separation makes it easier to manage and maintain different parts of your API independently.

- **Code Reusability**: Routers can be reused across multiple FastAPI applications or even in different projects. You can create a reusable router module and import it into multiple applications. This promotes code reuse and avoids duplication of endpoint definitions.

- **Route Prefixing**: Routers allow you to specify a prefix for all the routes defined within the router. This can be useful when you want to group related endpoints under a common URL prefix. It provides a clean and structured URL hierarchy for your API.

### Authentication & Users - Router Prefix

[Refer](auth_user_routerPrefix.py)

### Authentication & Users - Router Tags

> FastAPI provides a feature called "tags" that allows you to group and categorize your API endpoints. Tags help with organizing and documenting your API, especially when you have a large number of endpoints.

To add tags to your authentication and user routers, you can use the `tags` parameter when defining your endpoints within the routers.
```
from fastapi import FastAPI, APIRouter
from auth_user_connection import Session
from auth_model_users import User

app = FastAPI()

auth_router = APIRouter(tags=["Authentication"])
user_router = APIRouter(tags=["Users"])

@auth_router.post("/login")
def login():
    # Authentication logic goes here
    pass

@user_router.get("/")
def get_users():
    with Session() as session:
        users = session.query(User).all()
        if not users:
            raise HTTPException(status_code=404, detail="Users not found")
        return users

@user_router.get("/{user_id}")
def get_user(user_id: int):
    with Session() as session:
        user = session.query(User).get(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

app.include_router(auth_router)
app.include_router(user_router)
```
By default, FastAPI generates an interactive API documentation (Swagger UI) that includes tags to organize the endpoints. You can see the tags in the documentation and use them for navigation.(`http://127.0.0.1:8000/docs` or `http://127.0.0.1:8000/redoc`)

Including tags in your routers can improve the readability and organization of your API, making it easier to understand and navigate through the various endpoints.

[Refer](auth_user_routerTags.py)

### Authentication & Users - JWT Token Basics

JWT (JSON Web Token) is an open standard (RFC 7519) for **securely transmitting information between parties** as a JSON object. It is commonly used for **authentication and authorization purposes** in web applications.

Here are the basic components and concepts of JWT:

1. **Header**: The JWT header contains **metadata about the token** and specifies the algorithm used to sign and encode the token. It typically consists of two parts: **the token type (JWT)** and **the signing algorithm** (e.g., HMAC, RSA, or others).

2. **Payload**: The JWT payload contains the **claims or statements about the user or entity**. Claims can include information such as user ID, username, role, and other relevant data. There are three types of claims: *reserved claims*, *public claims*, and *private claims*. Reserved claims have predefined meanings, while public and private claims are custom claims defined by the application.

3. **Signature**: The JWT signature is used to **verify the authenticity of the token**. It is created by combining the *encoded header, encoded payload, and a secret key* (or a public/private key pair) using the specified signing algorithm. The signature ensures that the token has not been tampered with during transmission.

4. **Encoding**: The header and payload are Base64Url encoded to form the first two parts of the JWT. The encoded parts are concatenated with a period ('.') separator. The resulting string represents the JWT token.

When using JWT for authentication and authorization, the general flow is as follows:

1. **User Authentication**: The user provides their credentials (e.g., username and password) to the server for authentication.

2. **Token Generation**: Upon successful authentication, the server generates a JWT token. The token typically includes the user's ID or other relevant information as part of the payload.

3. **Token Issuance**: The server sends the JWT token back to the client as a response.

4. **Token Usage**: The client includes the JWT token in subsequent requests by adding it to the Authorization header or as a parameter in the request.

5. **Token Verification**: On each request, the server validates the JWT token's signature, verifies the token's claims, and ensures its validity and integrity.

6. **Authorization**: The server checks the user's permissions and roles based on the information in the token's payload to determine whether the user is authorized to access the requested resources.

> JWT tokens are self-contained and can be decoded and verified by the server without the need for database lookups or session management. They provide a stateless mechanism for authentication and can be used in various scenarios, including APIs, single sign-on (SSO), and microservices architectures.

It's important to note that JWT tokens should be used securely, and sensitive information should not be included in the payload to prevent potential security risks. Proper measures should be taken to secure the transmission and storage of JWT tokens, such as using HTTPS for communication and securely storing the secret keys or using asymmetric key pairs.

### Authentication & Users - Login Process

The login process in the context of authentication and user management involves verifying the user's credentials and granting access to protected resources. Here's a basic outline of the login process using JWT authentication:

1. **User Authentication**: The user provides their credentials (e.g., username and password) through a login form or API endpoint.
2. **Validate Credentials**: The server validates the user's credentials by checking if they match the stored user data in the database. This can involve querying the database to retrieve the user record based on the provided username or email.
3. **Generate JWT Token**: If the credentials are valid, the server generates a JWT token with the necessary claims (e.g., user ID, username, role) and signs it using a secret key. The token is typically set with an expiration time to enhance security.
4. **Token Issuance**: The server sends the JWT token back to the client as a response, usually within the response body or a specific header (e.g., Authorization header).
5. **Client Storage**: The client application stores the received JWT token securely. Common storage options include browser cookies, local storage, or session storage. The token should be stored securely and protected from unauthorized access.
6. **Token Usage**: On subsequent requests to access protected resources or perform authorized actions, the client includes the JWT token in the Authorization header or as a parameter. This allows the server to identify and authenticate the user.
7. **Token Verification**: Upon receiving a request, the server verifies the JWT token's signature and decodes the token to retrieve the user's claims. The server then checks if the user has the necessary permissions to access the requested resource.
8. **Grant Access**: If the JWT token is valid and the user has the required permissions, the server grants access to the requested resource or performs the authorized action. Otherwise, the server returns an appropriate error response (e.g., 401 Unauthorized).

Additionally, it's recommended to use secure communication protocols (e.g., HTTPS) to transmit sensitive data and enforce secure password policies (e.g., password complexity requirements, password expiration) to enhance overall security.

### Authentication & Users - Creating a Token

To create a token for user authentication, you can use a JWT (JSON Web Token) library that supports token generation and signing. Here's an example of how to create a JWT token in Python using the PyJWT library:

1. Install PyJWT library:
```
pip install PyJWT
```

2. Import necessary modules:
```
import jwt
import datetime
```
3. Define a function to generate a JWT token:
```
def create_token(user_id, secret_key, expires_in_minutes=60):
    # Define the payload with user-specific claims
    payload = {
        'user_id': user_id,  # unique identifier 
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=expires_in_minutes)
    }

    # Generate the JWT token
    token = jwt.encode(payload, secret_key, algorithm='HS256')

    return token
```
4. Generate a token for a specific user:
```
user_id = 123
secret_key = 'your_secret_key'

token = create_token(user_id, secret_key)
```
[Refer](auth_user_token.py)

### Authentication & Users - OAuth2 PasswordRequestForm

[Refer](auth_user_token_api.py)

### Authentication & Users - Verify user is Logged In

[Refer](auth_user_token_outh.py)

### Authentication & Users - Fixing Bugs

1. **Reproduce the bug**: Begin by reproducing the bug in a controlled environment. This will allow you to understand the specific steps or conditions that trigger the issue. Document the steps involved and gather any relevant error messages or logs.
2. **Understand the expected behavior**: Review the system's documentation, specifications, or user requirements to ensure a clear understanding of the expected behavior for authentication and user-related features. Compare the expected behavior with the observed behavior to identify any discrepancies.
3. **Isolate the bug**: Narrow down the scope of the problem by isolating the bug to specific modules, functions, or components. By doing so, you can focus your debugging efforts on the relevant areas, reducing complexity.
4. **Review the code**: Examine the code related to authentication and user-related functionality. Look for logical errors, incorrect assumptions, or missing validations that could lead to unexpected behavior. Pay close attention to input validation, authentication methods, session management, and access control mechanisms.
5. **Check dependencies**: Ensure that any external libraries, frameworks, or APIs used for authentication and user management are up to date and properly integrated. Verify that you are using the recommended versions and configurations and that there are no known issues or security vulnerabilities associated with them.
6. **Debugging tools**: Utilize debugging tools and techniques to trace the code execution, inspect variables, and step through the relevant sections of the code. This can help identify the point at which the bug occurs and provide insights into the root cause.
7. **Test cases**: Develop or review existing test cases specifically designed to cover authentication and user-related scenarios. Verify that these test cases cover both expected and edge cases, including different user roles, input variations, and error conditions.
8. **Logging and error handling**: Ensure that appropriate logging and error handling mechanisms are in place. Review the logs and error messages to identify any relevant information or patterns that could help pinpoint the issue.
9. **Fix the bug**: Based on the analysis and understanding gained from the previous steps, implement the necessary changes to fix the bug. This might involve modifying the code, updating configuration settings, or addressing any issues related to dependencies.
10. **Test the fix**: After making the code changes, thoroughly test the affected authentication and user-related functionality to ensure that the bug is resolved and that it does not introduce any new issues. Revisit the test cases identified earlier and validate that the expected behavior is now being exhibited.
11. **Deployment and monitoring**: Once the bug fix has been tested and validated, deploy the updated code to the production environment. Monitor the system closely after deployment to verify that the fix is effective and that there are no regressions or other unforeseen issues.

### Authentication & Users - Protecting Routes

To protect routes in FastAPI, you can use the `Depends` function from `fastapi.security` module along with an authentication function. Here's an example of how to protect routes using token-based authentication:

1. Import the necessary modules and define the authentication function:

```
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def authenticate_user(token: str = Depends(oauth2_scheme)):
    # Implement your logic to authenticate the user based on the token
    # Check the token validity, decode it, and verify if it belongs to a valid user
    # Return the user if authenticated, or raise an HTTPException with 401 Unauthorized status code
    # Example implementation:
    if token != "valid_token":
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return True
```
1. Protect the route by adding the `Depends(authenticate_user)` parameter to the route function:
```
@app.get("/protected")
async def protected_route(user: bool = Depends(authenticate_user)):
    # Only executed if the user is authenticated
    # Implement your logic for the protected route here
    return {"message": "You are accessing a protected route"}
```

### Authentication & Users - Test Expired Token

To test an expired token, you can manually create a token with a very short expiration time, such as a few seconds, and then attempt to access a protected route with that token after it has expired. Here's an example of how you can simulate an expired token:

1. Set a very short expiration time for the token in the `create_access_token` function. For example, you can set `expires_delta` to `5` (5 minutes) instead of `30`.
```
access_token = create_access_token(data={'sub': user.username}, secret_key='your_secret_key', expires_delta=5)
```
1. Start the FastAPI application and obtain a token by making a request to the `/token` endpoint.
2. Copy the token and wait for more than 5 minutes (or whatever expiration time you set in step 1) to ensure it has expired.
3. Make a request to a protected route, such as `/protected`, and include the expired token in the `Authorization` header as a bearer token.
```
GET /protected HTTP/1.1
Host: localhost:8000
Authorization: Bearer <expired_token>
```
4. The server should respond with an HTTP 401 Unauthorized status code and the message "Invalid authentication token" because the token has expired.

This test will simulate the behavior of an expired token and allow you to verify that the authentication middleware correctly handles expired tokens.