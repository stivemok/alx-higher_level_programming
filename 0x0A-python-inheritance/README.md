# 0x0A. Python - Inheritance

## Resources

### Read or watch:

* Inheritance

* Multiple inheritance

* Inheritance in Python

* Learn to Program 10 : Inheritance Magic Methods

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

All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')

All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')

All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

We strongly encourage you to work together on test cases, so that you don’t miss any edge case

### Documentation

Do not use the words import or from inside your comments, the checker will think you try to import some modules

## Tasks

0. Lookup - mandatory

Write a function that returns the list of available attributes and methods of an object:

* Prototype: def lookup(obj):

* Returns a list object

* You are not allowed to import any module

----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0A-python-inheritance# ./0-main.py 

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'my_attr1', 'my_meth']
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

----

1. My list

Write a class MyList that inherits from list:

* Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)

* You can assume that all the elements of the list will be of type int

* You are not allowed to import any module