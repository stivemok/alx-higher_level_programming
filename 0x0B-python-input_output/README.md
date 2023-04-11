# 0x0B. Python - Input/Output
## Resources
### Read or watch:

[* 7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

[* 8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)

[* Dive Into Python 3: Chapter 11. Files](https://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf)

[* JSON encoder and decoder](https://docs.python.org/3/library/json.html)

[* Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/watch?v=EukxMIsNeqU)

[* Automate the Boring Stuff with Python(ch.8 p 180-183 & ch.14 p 326-333)](https://automatetheboringstuff.com/)

## General
Why Python programming is awesome

How to open a file

How to write text in a file

How to read the full content of a file

How to read a file line by line

How to move the cursor in a file

How to make sure a file is closed after using it

What is and how to use the with statement

What is JSON

What is serialization

What is deserialization

How to convert a Python data structure to a JSON string

How to convert a JSON string to a Python data structure

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

All your modules should have a documentation (python3 -c \'print(\__import\__("my_module").\__doc\__)')

All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')

All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Tasks
### 0.Read file - mandatory
Write a function that reads a text file (UTF8) and prints it to stdout:

* Prototype: def read_file(filename=""):
* You must use the with statement
* You don’t need to manage file permission or file doesn't exist exceptions.
* You are not allowed to import any module

----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# ./0-main.py 

We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!

----
### 1. Write to a file - mandatory
Write a function that writes a string to a text file (UTF8) and returns the number of characters written:

* Prototype: def write_file(filename="", text=""):
* You must use the with statement
* You don’t need to manage file permission exceptions.
* Your function should create the file if doesn’t exist.
* Your function should overwrite the content of the file if it already exists.
* You are not allowed to import any module

----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# ./1-main.py 

24

root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# cat my_first_file.txt

This School is so cool!

----

### 2. Append to a file - mandatory
Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

* Prototype: def append_write(filename="", text=""):
* If the file doesn’t exist, it should be created
* You must use the with statement
* You don’t need to manage file permission or file doesn't exist exceptions.
* You are not allowed to import any module

-----