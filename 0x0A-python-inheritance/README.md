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