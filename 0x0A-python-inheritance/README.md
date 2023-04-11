# 0x0A. Python - Inheritance

## Resources
### Read or watch:

[* Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)

[* Multiple inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)

[* Inheritance in Python](https://www.w3schools.com/python/python_inheritance.asp)

[* Learn to Program 10 : Inheritance Magic Methods](https://www.youtube.com/watch?v=d8kCdLCi6Lk)

## General
Why Python programming is awesome

What is a superclass, baseclass or parentclass

What is a subclass

How to list all attributes and methods of a class or instance

When can an instance have new attributes

How to inherit class from another

How to define a class with multiple base classes

What is the default class every class inherit from

How to override a method or attribute inherited from the base class

Which attributes or methods are available by heritage to subclasses

What is the purpose of inheritance

What are, when and how to use isinstance, issubclass, type and super built-in functions

## Requirements
### Python Scripts
Allowed editors: vi, vim, emacs

All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)

All your files should end with a new line

The first line of all your files should be exactly #!/usr/bin/python3

A README.md file, at the root of the folder of the project, is mandatory

Your code should use the pycodestyle (version 2.8.*)

All your files must be executable

The length of your files will be tested using wc

### Python Test Cases
Allowed editors: vi, vim, emacs

All your files should end with a new line

All your test files should be inside a folder tests

All your test files should be text files (extension: .txt)

All your tests should be executed by using this command: python3 -m doctest ./tests/*

All your modules should have a documentation (python3 -c 'print(import("my_module").doc)')

All your classes should have a documentation (python3 -c 'print(import("my_module").MyClass.doc)')

All your functions (inside and outside a class) should have a documentation (python3 -c 'print(import("my_module").my_function.doc)' and python3 -c 'print(import("my_module").MyClass.my_function.doc)')

A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Documentation
Do not use the words import or from inside your comments, the checker will think you try to import some modules

## Tasks
### Lookup - mandatory
Write a function that returns the list of available attributes and methods of an object:

* Prototype: def lookup(obj):
* Returns a list object
* You are not allowed to import any module

----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0A-python-inheritance# ./0-main.py

['class', 'delattr', 'dict', 'dir', 'doc', 'eq', 'format', 'ge', 'getattribute', 'gt', 'hash', 'init', 'init_subclass', 'le', 'lt', 'module', 'ne', 'new', 'reduce', 'reduce_ex', 'repr', 'setattr', 'sizeof', 'str', 'subclasshook', 'weakref'] ['class', 'delattr', 'dict', 'dir', 'doc', 'eq', 'format', 'ge', 'getattribute', 'gt', 'hash', 'init', 'init_subclass', 'le', 'lt', 'module', 'ne', 'new', 'reduce', 'reduce_ex', 'repr', 'setattr', 'sizeof', 'str', 'subclasshook', 'weakref', 'my_attr1', 'my_meth'] ['abs', 'add', 'and', 'bool', 'ceil', 'class', 'delattr', 'dir', 'divmod', 'doc', 'eq', 'float', 'floor', 'floordiv', 'format', 'ge', 'getattribute', 'getnewargs', 'gt', 'hash', 'index', 'init', 'init_subclass', 'int', 'invert', 'le', 'lshift', 'lt', 'mod', 'mul', 'ne', 'neg', 'new', 'or', 'pos', 'pow', 'radd', 'rand', 'rdivmod', 'reduce', 'reduce_ex', 'repr', 'rfloordiv', 'rlshift', 'rmod', 'rmul', 'ror', 'round', 'rpow', 'rrshift', 'rshift', 'rsub', 'rtruediv', 'rxor', 'setattr', 'sizeof', 'str', 'sub', 'subclasshook', 'truediv', 'trunc', 'xor', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

----

### 1.My list
Write a class MyList that inherits from list:

* Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)
* You can assume that all the elements of the list will be of type int
* You are not allowed to import any module

----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0A-python-inheritance# ./1-main.py 

[1, 4, 2, 3, 5]

[1, 2, 3, 4, 5]

[1, 4, 2, 3, 5]

----

### 2. Exact same object - mandatory
Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

* Prototype: def is_same_class(obj, a_class):
* You are not allowed to import any module

-----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0A-python-inheritance# ./2-main.py 
1 is an instance of the class int

-----

### 3. Same class or inherit from - mandatory
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

* Prototype: def is_kind_of_class(obj, a_class):
* You are not allowed to import any module

----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0A-python-inheritance# ./3-main.py 

1 comes from int

1 comes from object

-----

### 4. Only sub class of - mandatory
Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

* Prototype: def inherits_from(obj, a_class):
* You are not allowed to import any module

----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0A-python-inheritance# ./4-main.py 

True inherited from class int

True inherited from class object

----

### 5. Geometry module - mandatory
Write an empty class BaseGeometry.

* You are not allowed to import any module

----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0A-python-inheritance# ./5-main.py

<5-base_geometry.BaseGeometry object at 0x7f14a4a81880>

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

----

### 6. Improve Geometry - mandatory
Write a class BaseGeometry (based on 5-base_geometry.py).

* Public instance method: def area(self): that raises an Exception with the message area() is not implemented
* You are not allowed to import any module

----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0A-python-inheritance# ./6-main.py

[Exception] area() is not implemented

----

### 7. Integer validator - mandatory
Write a class BaseGeometry (based on 6-base_geometry.py).

* Public instance method: def area(self): that raises an Exception with the message area() is not implemented
* Public instance method: def integer_validator(self, name, value): that validates value:
  * you can assume name is always a string
  * if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
  * if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
* You are not allowed to import any module

----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0A-python-inheritance# ./7-main.py

[TypeError] name must be an integer

[ValueError] age must be greater than 0

[ValueError] distance must be greater than 0

-----

### 8. Rectangle - mandatory
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

* Instantiation with width and height: def __init__(self, width, height):
  * width and height must be private. No getter or setter
  * width and height must be positive integers, validated by integer_validator

----

root@e000a5a9f6d4:~/alx-higher_level_programming/0x0A-python-inheritance# ./8-main.py

<8-rectangle.Rectangle object at 0x7f1c0bd32880>

['_Rectangle__height', '_Rectangle__width', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator']

[AttributeError] 'Rectangle' object has no attribute 'width'

[TypeError] height must be an integer

----
### 9. Full rectangle - mandatory
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)

* Instantiation with width and height: def __init__(self, width, height)::
  * width and height must be private. No getter or setter
  * width and height must be positive integers validated by integer_validator
* the area() method must be implemented
* print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>

----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0A-python-inheritance# ./9-main.py 
[Rectangle] 3/5
15

----

### 10. Square #1 - mandatory
Write a class Square that inherits from Rectangle (9-rectangle.py):

* Instantiation with size: def __init__(self, size)::
  * size must be private. No getter or setter
  * size must be a positive integer, validated by integer_validator
* the area() method must be implemented

----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0A-python-inheritance# ./10-main.py

[Rectangle] 13/13

169

----