# 0x14. JavaScript - Web scraping

An introductory project on:
- Why JavaScript programming is amazing
- How to manipulate JSON data
- How to use `request` and fetch API
- How to read and write a file using `fs` module

## Requirements
- Files are interpreted on Ubuntu 14.04 LTS using `node` (version 14.x)
- First line of all your files should be exactly `#!/usr/bin/node`
- Code should be semistandard compliant (version 16.x.x)
- Files must be executable
- Not allowed to use `var`

## File Descriptions
### Mandatory
[0-readme.js](./0-readme.js) - a script that reads and prints the content of a file

Requirements
	- The first argument is the file path
	- The content of the file must be read in utf-8
	- If an error occurred during the reading, print the error object
```
guillaume@ubuntu:~/0x14$ cat cisfun
C is super fun!
guillaume@ubuntu:~/0x14$ ./0-readme.js cisfun
C is super fun!

guillaume@ubuntu:~/0x14$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
guillaume@ubuntu:~/0x14$
```
