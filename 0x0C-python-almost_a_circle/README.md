# 0x0C. Python - Almost a circle
## Background Context
The AirBnB project is a big part of the Higher level curriculum. This project will help you be ready for it.

In this project, you will review everything about Python:

* Import
* Exceptions
* Class
* Private attribute
* Getter/Setter
* Class method
* Static method
* Inheritance
* Unittest
* Read/Write file

You will also learn about:

* args and kwargs
* Serialization/Deserialization
* JSON
## Resources
### Read or watch:

[* args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
[* JSON encoder and decoder](https://docs.python.org/3/library/json.html)
[* unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
[* Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

## General
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function
## Requirements
### Python Scripts
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.8.*)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should be documented: python3 -c \'print(\_\_import\_\_("my_module").\_\_doc\_\_)'
All your classes should be documented: python3 -c \'print(\_\_import\_\_("my_module").MyClass.\_\_doc\_\_)'
All your functions (inside and outside a class) should be documented: python3 -c \'print(\_\_import\_\_("my_module").my_function.\_\_doc\_\_)' and python3 -c \'print(\_\_import\_\_("my_module").MyClass.my_function.\_\_doc\_\_)'
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
### Python Unit Tests
* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* You have to use the unittest module
* All your test files should be python files (extension: .py)
* All your test files and folders should start with test_
* Your file organization in the tests folder should be the same as your project: ex: for models/base.py, unit tests must be in: tests/test_models/test_base.py
* All your tests should be executed by using this command: python3 -m unittest discover tests
* You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base.py
* We strongly encourage you to work together on test cases so that you don’t miss any edge case

## Tasks
### 0. If it's not tested it doesn't work - mandatory
----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0C-python-almost_a_circle# python3 -m unittest discover tests

----------------------------------------------------------------------

Ran 0 tests in 0.000s

OK

----
### 1. Base class - mandatory
-----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0C-python-almost_a_circle# ./0-main.py


1

2

3

12

4

----
### 2. First Rectangle - mandatory
----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0C-python-almost_a_circle# ./1-main.py 

1

2

12

----
### 3. Validate attributes - mandatory
----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0C-python-almost_a_circle# ./2-main.py

[TypeError] height must be an integer

[ValueError] width must be > 0

[TypeError] x must be an integer

[ValueError] y must be >= 0

-----
### 4. Area first - mandatory
----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0C-python-almost_a_circle# ./3-main.py 

6

20

56

----
### 5. Display #0 - mandatory
----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0C-python-almost_a_circle# ./4-main.py 

####

####

####

####

####

####

----

##

##

----
### 6. __str__ - mandatory
----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0C-python-almost_a_circle# ./6-main.py | cat -e

$

$

  ##$

  ##$

  ##$

---$

 ###$

 ###$

----
### 8. Update #0 - mandatory
----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0C-python-almost_a_circle# ./7-main.py 
[Rectangle] (1) 10/10 - 10/10
[Rectangle] (89) 10/10 - 10/10
[Rectangle] (89) 10/10 - 2/10
[Rectangle] (89) 10/10 - 2/10
[Rectangle] (89) 10/10 - 2/10
[Rectangle] (89) 10/10 - 2/10

----
### 9. Update #1 - mandatory
----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0C-python-almost_a_circle# ./8-main.py 
[Rectangle] (1) 10/10 - 10/10
[Rectangle] (1) 10/10 - 10/1
[Rectangle] (1) 2/10 - 1/1
[Rectangle] (89) 3/1 - 2/1
[Rectangle] (89) 1/3 - 4/2

----
### 10. And now, the Square!
----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0C-python-almost_a_circle# ./9-main.py 
[Square] (1) 0/0 - 5
25
#####
#####
#####
#####
#####
---
[Square] (2) 2/0 - 2
4
  ##
  ##
---
[Square] (3) 1/3 - 3
9



 ###
 ###
 ###

------
### 11. Square size - mandatory
-----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0C-python-almost_a_circle# ./10-main.py

[Square] (1) 0/0 - 5

5

[Square] (1) 0/0 - 10

[TypeError] width must be an integer

-----
### 12. Square update - mandatory
-----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0C-python-almost_a_circle# ./11-main.py

[Square] (1) 0/0 - 5

[Square] (10) 0/0 - 5

[Square] (1) 0/0 - 2

[Square] (1) 3/0 - 2

[Square] (1) 3/4 - 2

[Square] (1) 12/4 - 2

[Square] (1) 12/1 - 7

[Square] (89) 12/1 - 7

------
### 13. Rectangle instance to dictionary representation - mandatory
-----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0C-python-almost_a_circle# ./12-main.py 

[Rectangle] (1) 1/9 - 10/2

{'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}

<class 'dict'>

[Rectangle] (2) 0/0 - 1/1

[Rectangle] (1) 1/9 - 10/2

False
-----
### 14. Square instance to dictionary representation - mandatory
----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0C-python-almost_a_circle# ./13-main.py 

[Square] (1) 2/1 - 10

{'id': 1, 'size': 10, 'x': 2, 'y': 1}

<class 'dict'>

[Square] (2) 1/0 - 1

[Square] (1) 2/1 - 10

False
----
### 15. Dictionary to JSON string
----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0C-python-almost_a_circle# ./14-main.py


{'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}

<class 'dict'>

[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]

<class 'str'>

----
### 16. JSON string to file
----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0C-python-almost_a_circle# ./15-main.py

[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]

----
### 17. JSON string to dictionary - mandatory
----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0C-python-almost_a_circle# ./16-main.py

[<class 'list'>] [{'id': 89, 'width': 10, 'height': 4}, {'id': 7, 'width': 1, 'height': 7}]

[<class 'str'>] [{"id": 89, "width": 10, "height": 4}, {"id": 7, "width": 1, "height": 7}]

[<class 'list'>] [{'id': 89, 'width': 10, 'height': 4}, {'id': 7, 'width': 1, 'height': 7}]

----
### 18. Dictionary to Instance - mandatory
----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0C-python-almost_a_circle# ./17-main.py 

[Rectangle] (1) 1/0 - 3/5

[Rectangle] (1) 1/0 - 3/5

False

False

----
### 19. File to instances - mandatory
----
root@e000a5a9f6d4:~/alx-higher_level_programming/0x0C-python-almost_a_circle# ./18-main.py

[139788060805200] [Rectangle] (1) 2/8 - 10/7

[139788060804528] [Rectangle] (2) 0/0 - 2/4

---

[139788059510384] [Rectangle] (1) 2/8 - 10/7

---

---

[139788060634944] [Square] (4) 0/0 - 5


[139788059509088] [Square] (5) 9/1 - 7

---

[139788059567248] [Square] (4) 0/0 - 5

-----