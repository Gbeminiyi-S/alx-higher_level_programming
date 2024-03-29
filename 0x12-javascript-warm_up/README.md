# 0x12. JavaScript - Warm up
## Requirements
- Files are interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
- First line of all your files should be exactly `#!/usr/bin/node`
- Code should be semistandard compliant (version 16.x.x)
- Files must be executable
## File Descriptions
### Mandatory
[0-javascript_is_amazing.js](./0-javascript_is_amazing.js) - a script that prints "JavaScript is amazing"
- Create a constant variable called myVar with the value “JavaScript is amazing”
- Use console.log(...) to print all output

[1-multi_languages.js](./1-multi_languages.js) - a script that prints 3 lines:
- The first line: “C is fun”
- The second line: “Python is cool”
- The third line: “JavaScript is amazing”

[2-arguments.js](./2-arguments.js) - a script that prints a message depending of the number of arguments passed:
- If no arguments are passed to the script, print “No argument”
- If only one argument is passed to the script, print “Argument found”
- Otherwise, print “Arguments found”

[3-value_argument.js](./3-value_argument.js) - a script that prints the first argument passed to it:
- If no arguments are passed to the script, print “No argument”
- Not allowed to use `var`
- Not allowed to use `length`

[4-concat.js](./4-concat.js) - a script that prints two arguments passed to it, in the following format: "is"
```
guillaume@ubuntu:~/0x12$ ./4-concat.js c cool
c is cool
guillaume@ubuntu:~/0x12$ ./4-concat.js c 
c is undefined
guillaume@ubuntu:~/0x12$ ./4-concat.js
undefined is undefined
guillaume@ubuntu:~/0x12$ 
```
[5-to_integer.js](./5-to_integer.js) - a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer:
- If the argument can’t be converted to an integer, print “Not a number”

[6-multi_languages_loop.js](./6-multi_languages_loop.js) - a script that prints 3 lines: (like [1-multi_languages.js](./1-multi_languages.js)) but by using an array of string and a loop
- The first line: “C is fun”
- The second line: “Python is cool”
- The third line: “JavaScript is amazing”

[7-multi_c.js](./7-multi_c.js) - a script that prints `x` times “C is fun”
- `x` is the first argument of the script
- If the first argument can’t be converted to an integer, print “Missing number of occurrences”

[8-square.js](./8-square.js) - a script that prints a square
- The first argument is the size of the square
- If the first argument can’t be converted to an integer, print “Missing size”
- use the character X to print the square

[9-add.js](./9-add.js) - a script that prints the addition of 2 integers
- The first argument is the first integer
- The second argument is the second integer
- Define a function with this prototype: `function add(a, b)`

[10-factorial.js](./10-factorial.js) - a script that computes and prints a factorial
- The first argument is integer (argument can be cast as integer) used for computing the factorial
- Factorial of `NaN` is `1`
- Must be done recursively
- Must use a function
- Must use console.log(...) to print all output

[11-second_biggest.js](./11-second_biggest.js) - a script that searches the second biggest integer in the list of arguments
- If no argument passed, print `0`
- If the number of arguments is `1`, print `0`
- not allowed to use `var`

[12-object.js](./12-object.js) - Update this [script](./test-cases/12-object.js) to replace the value 12 with 89
- not allowed to use `var`

[13-add.js](./13-add.js) - a function that returns the addition of 2 integers
- The function must be visible from outside
- The name of the function must be `add`
- Not allowed to use `var`

### Advanced
[100-let_me_const.js](./100-let_me_const.js) - a file that modifies the value of `myVar` to `333`

[101-call_me_moby.js](./101-call_me_moby.js) - a function that executes `x` times a function
- The function must be visible from outside
- Prototype: `function (x, theFunction)`
- not allowed to use `var`

[102-add_me_maybe.js](./102-add_me_maybe.js) - a function that increments and calls a function
- The function must be visible from outside
- Prototype: `function (number, theFunction)`
- Not allowed to use `var`

[103-object_fct.js](./103-object_fct.js) - Update this [script](./test-cases/103-object_fct.js) by adding a new function `incr` that increments the integer `value`
