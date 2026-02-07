# Common Error Types

## SyntaxError
- ccurs when the parser encounters a syntax error.
- usually due to typos or incorrect code structure.

```python
def syntax_error_example():
    eval('x === x')  # Invalid syntax in Python
```

## NameError
- occurs when a local or global name is not found (or is not defined).

```python
def name_error_example():
    print(undefined_variable)  # 'undefined_variable' is not defined
```

## TypeError
- occurs when an operation or function is applied to an object of inappropriate type.
- for example, trying to add a string and an integer.

```python
def type_error_example():
    result = 'string' + 5  # Cannot concatenate str and int
```

## IndexError
- occurs when trying to access an index that is out of range for a list or tuple

```python
def index_error_example():
    my_list = [1, 2, 3]
    print(my_list[5])  # Index 5 is out of range for the list
```

## ValueError
- occurs when a function receives an argument of the right type but inappropriate value.
- for example, converting a non-numeric string to an integer.

```python
def value_error_example():
    number = int('not_a_number')  # Cannot convert string to int
```

## KeyError
- occurs when trying to access a dictionary with a key that does not exist.

```python
def key_error_example():
    my_dict = {'a': 1, 'b': 2}
    print(my_dict['c'])  # Key 'c' does not exist in the dictionary
```

## AttributeError
- occurs when an attribute reference or assignment fails.
- for example, trying to access a method that does not exist on an object.

```python
def attribute_error_example():
    my_list = [1, 2, 3]
    my_list.non_existent_method()  # 'list' object has no attribute 'non_existent_method'
```
