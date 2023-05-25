# 0x10-python-network_0
## Requirements
### Python Scripts
- Files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Codes are checked with the pycodestyle (version 2.8.\*)
- All files are executable

## File Descriptions
### Mandatory
[0-body_size.sh](./0-body_size.sh) - a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

Requirements:

- The size must be displayed in bytes
- You have to use `curl`

```
guillaume@ubuntu:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
10
guillaume@ubuntu:~/0x10$ 
```

[1-body.sh](./1-body.sh) - a Bash script that takes in a URL, sends a `GET` request to the URL, and displays the body of the response

Requirements:

- Display only body of a `200` status code response
- Have to use `curl`
```
guillaume@ubuntu:~/0x10$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
guillaume@ubuntu:~/0x10$ 
```

[2-delete.sh](./2-delete.sh) - a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

Requirements:

- Have to use curl
```
guillaume@ubuntu:~/0x10$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
guillaume@ubuntu:~/0x10$ 
```

[3-methods.sh](./3-methods.sh) - a Bash script that takes in a URL and displays all HTTP methods the server will accept

Requirements:

- You have to use `curl`
```
guillaume@ubuntu:~/0x10$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
guillaume@ubuntu:~/0x10$ 
```

[4-header.sh](./4-header.sh) - a Bash script that takes in a URL as an argument, sends a `GET` request to the URL, and displays the body of the response

Requirements:

- A header variable `X-School-User-Id` must be sent with the value `98`
- Have to use `curl`
```
guillaume@ubuntu:~/0x10$ ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello School!
guillaume@ubuntu:~/0x10$ 
```

[5-post_params.sh](./5-post_params.sh) - a Bash script that takes in a URL, sends a `POST` request to the passed URL, and displays the body of the response

Requirements:

- A variable `email` must be sent with the value `test@gmail.com`
- A variable `subject` must be sent with the value `I will always be here for PLD`
- You have to use `curl`
```
guillaume@ubuntu:~/0x10$ ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
    email: test@gmail.com
    subject: I will always be here for PLD
guillaume@ubuntu:~/0x10$ 
```

[6-peak.py](./6-peak.py)[6-peak.txt](./6-peak.txt) - a function that finds __a peak__ in a list of unsorted integers.

Requirements:

- Prototype: `def find_peak(list_of_integers):`
- Not allowed to import any module
- The algorithm must have the lowest complexity (hint: you don’t need to go through all numbers to find a peak)
- `6-peak.py` must contain the function
- `6-peak.txt` must contain the complexity of your algorithm: `O(log(n))`, `O(n)`, `O(nlog(n))` or `O(n2)`
- __Note__: there may be more than one peak in the list
```
guillaume@ubuntu:~/0x10$ cat 6-main.py
#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))

guillaume@ubuntu:~/0x10$ ./6-main.py
6
3
2
None
2
4
guillaume@ubuntu:~/0x10$ wc -l 6-peak.txt 
2 6-peak.txt
guillaume@ubuntu:~/0x10$ 
```

[100-status_code.sh](./100-status_code.sh) - a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.

Requirements:

- Not allowed to use any `pipe`, `redirection`, etc.
- Not allowed to use `;` and `&&`
- Have to use `curl`
```
guillaume@ubuntu:~/0x10$ ./100-status_code.sh 0.0.0.0:5000 ; echo ""
200
guillaume@ubuntu:~/0x10$ 
guillaume@ubuntu:~/0x10$ ./100-status_code.sh 0.0.0.0:5000/nop ; echo ""
404
guillaume@ubuntu:~/0x10$ 
```

[101-post_json.sh](./101-post_json.sh) - a Bash script that sends a JSON `POST` request to a URL passed as the first argument, and displays the body of the response.

Requirements:

- The script must send a `POST` request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request
- Have to use `curl`
```
guillaume@ubuntu:~/0x10$ cat my_json_0
{
    "name": "John Doe",
    "age": 33
}
guillaume@ubuntu:~/0x10$ ./101-post_json.sh 0.0.0.0:5000/route_json my_json_0 ; echo ""
Valid JSON
guillaume@ubuntu:~/0x10$ 
guillaume@ubuntu:~/0x10$ cat my_json_1
I'm a JSON! really!
guillaume@ubuntu:~/0x10$ ./101-post_json.sh 0.0.0.0:5000/route_json my_json_1 ; echo ""
Not a valid JSON
guillaume@ubuntu:~/0x10$ 
guillaume@ubuntu:~/0x10$ cat my_json_2
{
    "name": "John Doe",
    "age": 33,
}
guillaume@ubuntu:~/0x10$ ./101-post_json.sh 0.0.0.0:5000/route_json my_json_2 ; echo ""
Not a valid JSON
guillaume@ubuntu:~/0x10$ 
```

[102-catch_me.sh](./102-catch_me.sh) - a Bash script that makes a request to `0.0.0.0:5000/catch_me` that causes the server to respond with a message containing `You got me!`, in the body of the response.

Requirements:

- Have to use `curl`
- Not allowed to use `echo`, `cat`, etc. to display the final result
```
guillaume@ubuntu:~/0x10$ ./102-catch_me.sh ; echo ""
You got me!
guillaume@ubuntu:~/0x10$ 
```
