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

[8-json_api.py](./8-json_api.py) - a Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter

Requirements:

- The letter must be sent in the variable `q`
- If no argument is given, set `q=""`
- If the response body is properly JSON formatted and not empty, display the `id` and `name` like this: `[<id>] <name>`
- Otherwise:
    - Display `Not a valid JSON` if the JSON is invalid
    - Display `No result` if the JSON is empty
- Must use the packages `requests` and `sys`
- Not allowed to import packages other than `requests` and `sys`
```
guillaume@ubuntu:~/0x11$ ./8-json_api.py 
No result
guillaume@ubuntu:~/0x11$ ./8-json_api.py a
[8446] amnirqhtfjq
guillaume@ubuntu:~/0x11$ ./8-json_api.py 2
No result
guillaume@ubuntu:~/0x11$ ./8-json_api.py b
[7094] bmofakakhke
guillaume@ubuntu:~/0x11$ 
```

[10-my_github.py](./10-my_github.py) - a Python script that takes your GitHub credentials (username and password) and uses the `GitHub API` to display your `id`
- Must use `Basic Authentication` with a `personal access token as password` to access to your information (only `read:user` permission is needed)
- The first argument will be your `username`
- The second argument will be your `password` (in your case, `a personal access token as password`)
- Must use the packages `requests` and `sys`
- Not allowed to import packages other than `requests` and `sys`
```
guillaume@ubuntu:~/0x11$ ./10-my_github.py papamuziko cisfun
2531536
guillaume@ubuntu:~/0x11$ ./10-my_github.py papamuziko wrong_pwd
None
guillaume@ubuntu:~/0x11$ 
```

[100-github_commits.py](./100-github_commits.py) - a Python script that takes 2 arguments in order to solve the challenge below:
```
Please list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
```

Requirements:
- The first argument will be the `repository name`
- The second argument will be the `owner name`
- Must use the packages `requests` and `sys`
- Not allowed to import packages other than `requests` and `sys`

Response:
```
guillaume@ubuntu:~/0x11$ ./100-github_commits.py rails rails
3b5a6dfb18f33c373a89760c60d741f34206f23b: Jon Moss
f785ad786ae49dd6f7a2f1d77c44ea17008c6656: Jon Moss
bb13c37fefdc8b5699918b38eff84751c2899ad5: Rafael França
f5d880866917724217eae9785a3ccd3f806c5aaf: Rafael França
0da696a5e3cee87a996a020b664caa1eabd66220: Ryuta Kamizono
24eb450d7599bab1f5863e0578a21c65ca42a915: Matthew Draper
668f8691f1017042e238497d1a5b7b8bf1c43819: Matthew Draper
a76f5189f6cec4b3e6d9035e2b55dcda6050dfdb: Ryuta Kamizono
28079868d0e70bdac80c76cf806afd517edfe1e7: Rafael França
8f0d8551893789f26e5d6b82ccef00779296818f: Rafael Mendonça França
guillaume@ubuntu:~/0x11$ 
```
