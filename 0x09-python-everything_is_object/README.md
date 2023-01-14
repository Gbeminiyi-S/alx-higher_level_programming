# 0x09. Python - Everything is object
## Requirements
### Python Scripts
- Files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Codes are checked with the pycodestyle (version 2.8.*)
- All files are executable
### .txt
- Only one line
- No Shebang
## File Descriptions
### Mandatory
[0-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/0-answer.txt) - What function would you use to print the type of an object? Name of function without `()`

[1-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/1-answer.txt) - How do you get the variable identifier (which is the memory address in the CPython implementation)? Name of function without `()`

[2-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/2-answer.txt) - In the following code, do `a` and `b` point to the same object?
```
>>> a = 89
>>> b = 100
```

[3-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/3-answer.txt) - In the following code, do `a` and `b` point to the same object?
```
>>> a = 89
>>> b = 89
```
[4-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/4-answer.txt) - In the following code, do `a` and `b` point to the same object?
```
>>> a = 89
>>> b = a
```

[5-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/5-answer.txt) - In the following code, do `a` and `b` point to the same object?
```
>>> a = 89
>>> b = a + 1
```

[6-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/6-answer.txt) - What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```

[7-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/7-answer.txt) - What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 is s2)
```

[8-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/8-answer.txt) - What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```

[9-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/9-answer.txt) - What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```

[10-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/10-answer.txt) - What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```

[11-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/11-answer.txt) - What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```

[12-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/12-answer.txt) - What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

[13-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/13-answer.txt) - What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

[14-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/14-answer.txt) - What does this script print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l1.append(4)
>>> print(l2)
```

[15-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/15-answer.txt) - What does this script print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l1 = l1 + [4]
>>> print(l2)
```

[16-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/16-answer.txt) - What does this script print?
```
>>> def increment(n):
...     n += 1
>>> a = 1
>>> increment(a)
>>> print(a)
```

[17-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/17-answer.txt) - What does this script print?
```
>>> def increment(n):
...     n.append(4)
>>> l = [1, 2, 3]
>>> increment(l)
>>> print(l)
```

[18-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/18-answer.txt) - What does this script print?
```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

[19-copy_list.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/19-copy_list.py) - a function `def copy_list(l):` that returns a *copy* of a list.
  - The input list can contain any type of objects
  - The file should be maximum 3-line long (no documentation needed)
  - Not allowed to import any module
  
[20-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/20-answer.txt) - Is `a` a tuple?
```
a = ()
```

[21-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/21-answer.txt) - Is `a` a tuple?
```
a = (1, 2)
```

[22-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/22-answer.txt) - Is `a` a tuple?
```
a = (1)
```

[23-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/23-answer.txt) - Is `a` a tuple?
```
a = (1, )
```

[24-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/24-answer.txt) - What does this script print?
```
a = (1)
b = (1)
a is b
```

[25-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/25-answer.txt) - What does this script print?
```
a = (1, 2)
b = (1, 2)
a is b
```

[26-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/26-answer.txt) - What does this script print?
```
a = ()
b = ()
a is b
```

[27-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/27-answer.txt) - Will the last line of this script print 139926795932424?
```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```

[28-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/28-answer.txt) - Will the last line of this script print 139926795932424?
```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```

### Advanced
[100-magic_string.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/100-magic_string.py) -  a function `magic_string()` that returns a string “BestSchool” n times the number of the iteration
  - The file should be maximum 4-line long (no documentation needed)
  - Not allowed to import any module
  
[101-locked_class.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/101-locked_class.py) - a class `LockedClass` with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called `first_name`

**int 1/3**
```
julien@ubuntu:/python3$ cat int.py 
a = 1
b = 1
julien@ubuntu:/python3$ 
```
Assuming we are using a CPython implementation of Python3 with default options/configuration:
- How many int objects are created by the execution of the first line of the script? [103-line1.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/103-line1.txt)
- How many int objects are created by the execution of the second line of the script? [103-line2.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/103-line2.txt)

**int 2/3**
```
julien@ubuntu:/python3$ cat int.py 
a = 1024
b = 1024
del a
del b
c = 1024
julien@ubuntu:/python3$ 
```
Assuming we are using a CPython implementation of Python3 with default options/configuration:
- How many int objects are created by the execution of the first line of the script? [104-line1.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/104-line1.txt)
- How many int objects are created by the execution of the second line of the script [104-line2.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/104-line2.txt)
- After the execution of line 3, is the int object pointed by `a` deleted? [104-line3.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/104-line3.txt)
- After the execution of line 4, is the int object pointed by b deleted? [104-line4.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/104-line4.txt)
- How many int objects are created by the execution of the last line of the script? [104-line5.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/104-line5.txt)

**int 3/3**
```
julien@twix:/tmp/so$ cat int.py 
print("I")
print("Love")
print("Python")
julien@ubuntu:/tmp/so$ 
```
Assuming we are using a CPython implementation of Python3 with default options/configuration:
- Before the execution of line 2 (`print("Love")`), how many int objects have been created and are still in memory? [105-line1.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/105-line1.txt)

**Clear strings**
```
guillaume@ubuntu:/python3$ cat string.py 
a = "SCHL"
b = "SCHL"
del a
del b
c = "SCHL"
guillaume@ubuntu:/python3$
```
Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word):
- How many string objects are created by the execution of the first line of the script? [106-line1.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/106-line1.txt)
- How many string objects are created by the execution of the second line of the script? [106-line2.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/106-line2.txt)
- After the execution of line 3, is the string object pointed by `a` deleted? [106-line3.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/106-line3.txt)
- After the execution of line 4, is the string object pointed by `b` deleted? [106-line4.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/106-line4.txt)
- How many string objects are created by the execution of the last line of the script? [106-line5.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/106-line5.txt)
