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

All your classes should have a documentation (python3 -c \'print(\__import\__("my_module").MyClass.\__doc\__)')

All your functions (inside and outside a class) should have a documentation (python3 -c \'print(\__import\__("my_module").my_function.\__doc\__)' and python3 -c \'print(\__import\__("my_module").MyClass.my_function.\__doc\__)')

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
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# ./2-main.py 

24

root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# cat file_append.txt 

This School is so cool!

root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# ./2-main.py 

24

root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# cat file_append.txt 

This School is so cool!

This School is so cool!

----
### 3. To JSON string - mandatory
Write a function that returns the JSON representation of an object (string):

* Prototype: def to_json_string(my_obj):
* You don’t need to manage exceptions if the object can’t be serialized.

----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# ./3-main.py

[1, 2, 3]

<class 'str'>

{"id": 12, "name": "John", "places": ["San Francisco", "Tokyo"], "is_active": true, "info": {"age": 36, "average": 3.14}}

<class 'str'>

[TypeError] Object of type set is not JSON serializable

----
### 4. From JSON string to Object - mandatory
Write a function that returns an object (Python data structure) represented by a JSON string:

* Prototype: def from_json_string(my_str):
* You don’t need to manage exceptions if the JSON string doesn’t represent an object.

----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# ./4-main.py

[1, 2, 3]

<class 'list'>

{'is_active': True, 'info': {'age': 36, 'average': 3.14}, 'id': 12, 'name': 'John','places': ['San Francisco', 'Tokyo']}

<class 'dict'>

[JSONDecodeError] Expecting property name enclosed in double quotes: line 2 column 25 (char 25)

----
### 5. Save Object to a file - mandatory
Write a function that writes an Object to a text file, using a JSON representation:

* Prototype: def save_to_json_file(my_obj, filename):
* You must use the with statement
* You don’t need to manage exceptions if the object can’t be serialized.
* You don’t need to manage file permission exceptions.

----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# ./5-main.py

[TypeError] Object of type set is not JSON serializable

root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# cat my_list.json ; echo ""

[1, 2, 3]

root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# cat my_dict.json ; echo ""

{"id": 12, "name": "John", "places": ["San Francisco", "Tokyo"], "is_active": true, "info": {"age": 36, "average": 3.14}}

root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# cat my_set.json ; echo ""

root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output#

----
### 6. Create object from a JSON file - mandatory
Write a function that creates an Object from a “JSON file”:

* Prototype: def load_from_json_file(filename):
* You must use the with statement
* You don’t need to manage exceptions if the JSON string doesn’t represent an object.
* You don’t need to manage file permissions / exceptions.

----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# cat my_list.json ; echo ""

[1, 2, 3]

root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# cat my_dict.json ; echo ""

{"id": 12, "name": "John", "places": ["San Francisco", "Tokyo"], "is_active": true, "info": {"age": 36, "average": 3.14}}

root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# cat my_fake.json ; echo ""

{"is_active": true, 12 }

root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# ./6-main.py 

[1, 2, 3]

<class 'list'>

{'id': 12, 'name': 'John', 'places': ['San Francisco', 'Tokyo'], 'is_active': True, 'info': {'age': 36, 'average': 3.14}}

<class 'dict'>

[FileNotFoundError] [Errno 2] No such file or directory: 'my_set_doesnt_exist.json'

[JSONDecodeError] Expecting property name enclosed in double quotes: line 1 column 21 (char 20)

----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# cat add_item.json

cat: add_item.json: No such file or directory

root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# ./7-add_item.py

root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# cat add_item.json ; echo ""

[]

root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# ./7-add_item.py Best School

root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# cat add_item.json ; echo ""

["Best", "School"]

root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# ./7-add_item.py 89 Python C

root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# cat add_item.json ; echo ""

["Best", "School", "89", "Python", "C"]

----
### 8. Class to JSON - mandatory
Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

* Prototype: def class_to_json(obj):
* obj is an instance of a Class
* All attributes of the obj Class are serializable: list, dictionary, string, integer and boolean
* You are not allowed to import any module

-----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# ./8-main.py 

<class '8-my_class.MyClass'>

[MyClass] John - 89

<class 'dict'>

{'name': 'John', 'number': 89}

root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# ./8-main_2.py 

<class '8-my_class_2.MyClass'>

[MyClass] John - 4 => 1

<class 'dict'>

{'_MyClass__name': 'John', 'number': 4, 'is_team_red': True, 'score': 1}

----
### 9. Student to JSON - mandatory
Write a class Student that defines a student by:

* Public instance attributes:
  * first_name
  * last_name
  * age
* Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):

* Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)

* You are not allowed to import any module

----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# ./9-main.py

<class 'dict'>

John

<class 'str'>

23

<class 'int'>

<class 'dict'>

Bob

<class 'str'>

27

<class 'int'>

----
### 10. Student to JSON with filter - mandatory
Write a class Student that defines a student by: (based on 9-student.py)

* Public instance attributes:
  * first_name
  * last_name
  * age
* Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):

* Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
  * If attrs is a list of strings, only attribute names contained in this list must be retrieved.
  * Otherwise, all attributes must be retrieved
* You are not allowed to import any module

-----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0B-python-input_output# ./10-main.py

{'first_name': 'John', 'last_name': 'Doe', 'age': 23}

{'first_name': 'Bob', 'age': 27}

{'age': 27}

----
### 11. Student to disk and reload - mandatory
Write a class Student that defines a student by: (based on 10-student.py)

* Public instance attributes:
  * first_name
  * last_name
  * age
* Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
* Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
  * If attrs is a list of strings, only attributes name contain in this list must be retrieved.
  * Otherwise, all attributes must be retrieved
* Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:
  * You can assume json will always be a dictionary
  * A dictionary key will be the public attribute name
  * A dictionary value will be the value of the public attribute
* You are not allowed to import any module
Now, you have a simple implementation of a serialization and deserialization mechanism (concept of representation of an object to another format, without losing any information and allow us to rebuild an object based on this representation)

----