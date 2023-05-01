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

[1-writeme.js](./1-writeme.js) - a script that writes a string to a file

Requirements
- The first argument is the file path
- The second argument is the string to write
- The content of the file must be read in utf-8
- If an error occurred during the reading, print the error object
```
guillaume@ubuntu:~/0x14$ ./1-writeme.js my_file.txt "Python is cool"
guillaume@ubuntu:~/0x14$ cat my_file.txt ; echo ""
Python is cool
guillaume@ubuntu:~/0x14$ 
```

[2-statuscode.js](./2-statuscode.js) - a script that display the status code of a GET request

Requirements

- The first argument is the file path
- The status code must be printed like this: `code: <status code>`
- Must use the module `request`
```
guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://alx-intranet.hbtn.io/status
code: 200
guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://alx-intranet.hbtn.io/doesnt_exist
code: 404
guillaume@ubuntu:~/0x14$ 
```

[3-starwars_title.js](./3-starwars_title.js) - a script that prints the title of a Star Wars movie where the episode number matches a given integer

Requirements

- The first argument is the movie ID
- Use the [Star wars API](https://swapi-api.alx-tools.com/) with the endpoint `https://swapi-api.alx-tools.com/api/films/:id`
- Must use the module `request`
```
guillaume@ubuntu:~/0x14$ ./3-starwars_title.js 1
A New Hope
guillaume@ubuntu:~/0x14$ ./3-starwars_title.js 5
Attack of the Clones
guillaume@ubuntu:~/0x14$ 
```
