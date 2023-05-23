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



