# 0x11. Python - Network #1

An introductory project on:

- How to fetch internet resources with the Python package `urllib`
- How to decode `urllib` body response
- How to use the Python package `requests`
- How to make HTTP `GET` request
- How to make HTTP `POST/PUT/`etc. request
- How to fetch JSON resources
- How to manipulate data from an external service

## Requirements
- All files should be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- The first line of all files should be exactly `#!/usr/bin/python3`
- The code should use the Pycodestyle (`version 2.8.*`)
- All files must be executable
- All modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
- Must use `get` to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
- The code should not be executed when imported (by using if `__name__ == "__main__":`)

## File Descriptions
### Mandatory
[0-hbtn_status.py](./0-hbtn_status.py) - a Python script that fetches https://alx-intranet.hbtn.io/status

Requirements:

- Must use the package `urllib`
- Not allowed to import any packages other than `urllib`
- The body of the response must be displayed like the following example (tabulation before `-`)
- Must use a `with` statement
```
guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
guillaume@ubuntu:~/0x11$ 
```

[1-hbtn_header.py](./1-hbtn_header.py) - a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.

Requirements:

- Must use the package `urllib` and `sys`
- Not allowed to import any packages other than `urllib` and `sys`
- The value of this variable is different for each request
- Must use a `with` statement
```
guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
ade2627e-41dd-4c34-b9d9-a0fa0f47b237
guillaume@ubuntu:~/0x11$ 
guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
6593e1f5-1b4b-4c9f-9c0e-72ab525b850f
guillaume@ubuntu:~/0x11$ 
```

[2-post_email.py](./2-post_email.py) - a Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`)

Requirements:

- The email must be sent in the `email` variable
- Must use the packages `urllib` and `sys`
- Not allowed to import packages other than `urllib` and `sys`
- Must use the `with` statement
```
guillaume@ubuntu:~/0x11$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
guillaume@ubuntu:~/0x11$ 
```

[3-error_code.py](./3-error_code.py) - a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`)

Requirements:

- Have to manage `urllib.error.HTTPError` exceptions and print: `Error code:` followed by the HTTP status code
- Must use the packages `urllib` and `sys`
- Not allowed to import packages other than `urllib` and `sys`
- Must use the `with` statement
```
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000
Index
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
guillaume@ubuntu:~/0x11$ 
```

[4-hbtn_status.py](./4-hbtn_status.py) - a Python script that fetches https://alx-intranet.hbtn.io/status

Requirements:

- Must use the package `requests`
- Not allow to import packages other than `requests`
- The body of the response must be display like the following example (tabulation before `-`)
```
guillaume@ubuntu:~/0x11$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$
guillaume@ubuntu:~/0x11$ 
```

[5-hbtn_header.py](./5-hbtn_header.py) - a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header

Requirements:

- Must use the packages `requests` and `sys`
- Not allow to import other packages than `requests` and `sys`
- The value of this variable is different for each request
```
guillaume@ubuntu:~/0x11$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
5e52e160-c822-4669-8b3a-8b3bbca7b090
guillaume@ubuntu:~/0x11$ 
guillaume@ubuntu:~/0x11$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
eaceaf35-bc0f-4f74-994a-7be0728ec654
guillaume@ubuntu:~/0x11$ 
```

[6-post_email.py](./6-post_email.py) - a Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response

Requirements:
- The email must be sent in the variable `email`
- Must use the packages `requests` and `sys`
- Not allowed to import packages other than `requests` and `sys`
```
guillaume@ubuntu:~/0x11$ ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
guillaume@ubuntu:~/0x11$ 
```

[7-error_code.py](./7-error_code.py) - a Python script that takes in a URL, sends a request to the URL and displays the body of the response

Requirements:

- If the HTTP status code is greater than or equal to 400, print: `Error code:` followed by the value of the HTTP status code
- Must use the packages `requests` and `sys`
- Not allowed to import packages other than `requests` and `sys`
```
guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000
Index
guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
guillaume@ubuntu:~/0x11$ 
```
