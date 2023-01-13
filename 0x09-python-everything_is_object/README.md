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

[14-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/14-answer.txt) - What do this script print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l1.append(4)
>>> print(l2)
```

[15-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/15-answer.txt) - What do this script print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l1 = l1 + [4]
>>> print(l2)
```

[16-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/16-answer.txt) - What do this script print?
```
>>> def increment(n):
...     n += 1
>>> a = 1
>>> increment(a)
>>> print(a)
```

[17-answer.txt](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x09-python-everything_is_object/17-answer.txt) - What do this script print?
```
>>> def increment(n):
...     n.append(4)
>>> l = [1, 2, 3]
>>> increment(l)
>>> print(l)
```
