# 0x13. JavaScript - Objects, Scopes and Closures
## Requirements
- Files are interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
- First line of all your files should be exactly `#!/usr/bin/node`
- Code should be semistandard compliant (version 16.x.x)
- Files must be executable
## File Descriptions
### Mandatory
[0-rectangle.js](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/0-rectangle.js) - an empty class `Rectangle` that defines a rectangle

[1-rectangle.js](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/1-rectangle.js) - defines a rectangle
- Use the `class` notation for defining your class
- The constructor must take 2 arguments `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`

[2-rectangle.js](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/2-rectangle.js) - defines a rectangle (Based on [1-rectangle.js](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/1-rectangle.js))
- If w or h is equal to 0 or not a positive integer, create an empty object

[3-rectangle.js](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/3-rectangle.js) - defines a rectangle (Based on [2-rectangle.js](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/2-rectangle.js)
- Create an instance method called `print()` that prints the rectangle using the character `X`

[4-rectangle.js](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/4-rectangle.js) - defines a rectangle (Based on [3-rectangle.js](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/3-rectangle.js)
- Create an instance method called `rotate()` that exchanges the `width` and the `height` of the rectangle
- Create an instance method called `double()` that multiples the `width` and the `height` of the rectangle by 2

[5-square.js](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/5-square.js) - defines a square and inherits from Rectangle of [4-rectangle.js](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/4-rectangle.js)
- The constructor must take 1 argument: `size`
- The constructor of `Rectangle` must be called (by using `super()`)

[6-square.js](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/6-square.js) - defines a square and inherits from `Square` of [5-square.js](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/5-square.js)
- Create an instance method called `charPrint(c)` that prints the rectangle using the character `c`
  - If `c` is undefined, use the character `X`
  
 [7-occurrences.js](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/7-occurrences.js) - a function that returns the number of occurrences in a list
- Prototype: `exports.nbOccurences = function (list, searchElement)`

[8-esrever.js](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/8-esrever.js) - a function that returns the reversed version of a list
- Prototype: `exports.esrever = function (list)`
- Not allow to use the built-in method `reverse`

[9-logme.js](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/9-logme.js) - a function that prints the number of arguments already printed and the new argument value
- Prototype: `exports.logMe = function (item)`
- Output format: `<number arguments already printed>: <current argument value>`

[10-converter.js](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/10-converter.js) - a function that converts a number from base 10 to another base passed as argument
- Prototype: `exports.converter = function (base)`
- Not allowed to import any file
- Not allowed to declare any new variable (`var`, `let`, etc..)

### Advanced
[100-map.js](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/100-map.js) - a script that imports an array and computes a new array
- The script must import `list` from the file [100-data.js](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/test_cases/100-data.js)
- Use a `map`
- A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
- Print both the initial list and the new list

[101-sorted.js](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/101-sorted.js) - a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
- The script must import `dict` from the file [101-data.js](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/test_cases/101-data.js)
- In the new dictionary:
  - A key is a number of occurrences
  - A value is the list of user ids
- Print the new dictionary at the end

[102-concat.js](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/102-concat.js) - a script that concats 2 files.
- The first argument is the file path of the [first source file](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/test_cases/fileA)
- The second argument is the file path of the [second source file](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/test_cases/fileB)
- The third argument is the [file path of the destination](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/test_cases/fileC)
```
guillaume@ubuntu:~/0x13$ cat fileA
C is fun!
guillaume@ubuntu:~/0x13$ cat fileB
Python is Cool!!!
guillaume@ubuntu:~/0x13$ ./102-concat.js fileA fileB fileC
guillaume@ubuntu:~/0x13$ cat fileC
C is fun!
Python is Cool!!!
guillaume@ubuntu:~/0x13$ 
```
