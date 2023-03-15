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

### Advanced
