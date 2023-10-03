# Project Name
**0x09. Python - Everything is object**

## Author's Details
Name: *BC Rachoshi.*

Email: *bcrachoshi@gmail.com*

Username: *Infrixxx*

##  Requirements

### Python Scripts
*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using gcc, using python3 (version 3.8.5).
*   All your files should end with a new line.
*   The `main.py` files are used to test your functions, but you don’t have to push them to your repo.
*   The first line of all your files should be exactly `#!/usr/bin/python3`.
*   Your code should use the pycodestyle (version `2.8.*`).
*   All your files must be executable.
*   The length of your files will be tested using `wc`.
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
*   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`).
*   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)`' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`).
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified).

### `.txt` Answer Files
*   Only one line.
*   No Shebang.
*   All your files should end with a new line.
*   Write the name of a function without `()`.


## Project Description
What is an object.
What is the difference between a class and an object or instance.
What is the difference between immutable object and mutable object.
What is a reference.
What is an assignment.
What is an alias.
How to know if two variables are identical.
How to know if two variables are linked to the same object.
How to display the variable identifier (which is the memory address in the CPython implementation).
What is mutable and immutable.
What are the built-in mutable types.
What are the built-in immutable types.
How does Python pass variables to functions.


* **0. Who am I?** - What function would you use to print the type of an object? - `0-answer.txt`.
* **1. Where are you?** - How do you get the variable identifier (which is the memory address in the CPython implementation)? - `1-answer.txt`.
* **2. Right count** - In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`. - `2-answer.txt`.
```
>>> a = 89
>>> b = 100
```
* **3. Right count =** - In the following code, do `a` and `b` point to the same object? Answer with `Yes or No`. - `3-answer.txt`.
```
>>> a = 89
>>> b = 89
```
* **4. Right count =** - In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`. - `2-answer.txt`.
```
>>> a = 89
>>> b = a
```
* **5. Right count =+** - In the following code, do `a` and `b` point to the same object? Answer with `Yes or No`. - `3-answer.txt`.
```
>>> a = 89
>>> b = a + 1
```
* **6. Is equal** - What do these 3 lines print? - `6-answer.txt`.
```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```
* **7. Is the same** - What do these 3 lines print? - `7-answer.txt`.
```
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```
* **8. Is really equal** - What do these 3 lines print? - `8-answer.txt`.
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```
* **9. Is really the same** - What do these 3 lines print? - ` 9-answer.txt`.
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```
* **10. And with a list, is it equal** - What do these 3 lines print? - `10-answer.txt`.
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```
* **11. And with a list, is it the same** - What do these 3 lines print? - `11-answer.txt`.
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```
* **12. And with a list, is it really equal** - What do these 3 lines print? - `12-answer.txt`.
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```
* **13. And with a list, is it really the same** - What do these 3 lines print? - `13-answer.txtt`.
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```
* **14. List append** - What does this script print? - `14-answer.txt`.
```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```
* **15. List add** - What does this script print? - `15-answer.txt`.
```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```
* **16. Integer incrementation** - What does this script print? - `16-answer.txt`.
```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```
* **17. List incrementation** - What does this script print? - `17-answer.txt`.
```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```
* **18. List assignation** - What does this script print? - `18-answer.txt`.
```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
Certainly! Here is the completion for question 18:

* **18. List assignation** - What does this script print? - `18-answer.txt`.
```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

Answer in `18-answer.txt`:
```
[1, 2, 3]
```

In this script, we have a function `assign_value(n, v)` that takes two arguments and assigns the value of `v` to `n`. However, this assignment does not affect the original list `l1` outside of the function. So, when we print `l1` after calling `assign_value(l1, l2)`, it remains unchanged, and the output is `[1, 2, 3]`.