# Why use modules?
- **Reusability**: Modules allow you to reuse code across multiple projects without having to rewrite it.
- **Organization**: Modules help you organize your code into logical sections, making it easier to maintain and understand.
- **Namespace**: Modules provide a separate namespace for your code, preventing naming conflicts between different parts of your program.
- **Built-in functionality**: Python comes with a large standard library of modules that provide a wide range of functionality, from file handling to web development.
- **Third-party libraries**: There are many third-party libraries available that can be easily installed and imported as modules, allowing you to leverage the work of others and save time.

## Built-in modules
- built-in modules are modules that are included with the Python standard library, and you can import and use them in your code without installing anything
- some examples of built-in modules are: `math`, `random`, `datetime`, `os`, `sys`

## Custom modules
- you can create your own custom modules by creating a `.py` file and defining functions, classes, and variables in it
- you can then import the module and use its functions, classes, and variables in your code

# External modules 
- external modules are modules that are not part of the Python standard library, but can be installed and used in your code
- you can install external modules using `pip`, the Python package manager
- once you have installed an external module, you can import it and use its functions, classes, and variables in your code    

- to install an external module, you can use the following command in your terminal:

    ```bash
    $ pip install module_name

    $ python -m pip install module_name
    ```


- if you are using a virtual environment, make sure to activate it before installing the module
- for example, to install the requests module, you can use the following command:
    
    ```bash
    pip install requests
    ```

both commands install python packages, but with an important difference:

`pip install module_name`

- runs the pip executable directly from your system's `PATH`
- may use a different python version thatn the one you're currently using
- can cause issues when you have multiple python versions installed

`python -m pip install module_name`

- runs `pip` as a module using the specific python interpreter in the command
- guarantees the package is installed for that exact python version
- more explicit and reliable, especially with multiple python installations

example scenario: if you have python 3.9 and 3.12 installed:

- `pip install requests` might install to Python 3.9's site-packages
- `python3.12 -m pip install requests` explicitly installs to Python 3.12's site-packages


> Best practice: use `python -m pip` (or `python3 -m pip`) to ensure you're installing packages for the correct python interpreter, especially in virtual environments or when multiple python versions are present.

### Set up your virtual environment

1. open terminal in your project directory

    ```bash
    cd /users/user/path/to/project/directory
    ```
2. create a virtual environment (if not already done)

    ```bash
    python3 -m venv .venv
    ```
3. activate the virtual environment

    ```bash
    source .venv/bin/activate
    ```
    you should see `(.venv)` prefix in your terminal
4. upgrade pip (recommended)

    ```bash
    pip install --upgrade pip
    ```
5. install required packages

    ```bash
    pip install package1 package2
    ```
6. create `requirements.txt` file (optional but recommended)

    ```bash
    pip freeze > requirements.txt
    ```
    this saves all installed packages for future reference

7. configure vs code to use this interpreter

    - open vs code in your project folder
    - press `Cmd + Shift + P`
    - type "Python: Select Interpreter"
    - choose the one showing `.venv/bin/python`
    - vs code will remember this selection

8. deactivate the virtual environment (when done)

    ```bash
    deactivate
    ```
    the `(.venv)` prefix will disappear from your terminal prompt, returning to your system python.