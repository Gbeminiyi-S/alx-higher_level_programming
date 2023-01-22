# 0x0B. Python - Input/Output
An introductory project on:

- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the with statement
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure
## Requirements
### Python Scripts
- Files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Codes are checked with the pycodestyle (version 2.8.*)
## File Descriptions
### Mandatory
[0-read_file.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0B-python-input_output/0-read_file.py) - reads a text file (`UTF8`) and prints it to stdout
- Prototype: `def read_file(filename=""):`
- Use the `with` statement

[1-write_file.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0B-python-input_output/1-write_file.py) - writes a string to a text file (`UTF8`) and returns the number of characters written
- Prototype: `def write_file(filename="", text=""):`
- Use the `with` statement
- function should create the file if doesn’t exist
- function should overwrite the content of the file if it already exists

[2-append_write.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0B-python-input_output/2-append_write.py) - appends a string at the end of a text file (`UTF8`) and returns the number of characters added
- Prototype: `def append_write(filename="", text=""):`
- Use the `with` statement
- function should create the file if doesn’t exist

[3-to_json_string.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0B-python-input_output/3-to_json_string.py) - returns the JSON representation of an object (string)
- Prototype: `def to_json_string(my_obj):`

[4-from_json_string.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0B-python-input_output/4-from_json_string.py) - returns an object (Python data structure) represented by a JSON string
- Prototype: `def from_json_string(my_str):`

[5-save_to_json_file.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0B-python-input_output/5-save_to_json_file.py) - writes an Object to a text file, using a JSON representation
- Prototype: `def save_to_json_file(my_obj, filename):`
- Use the `with` statement

[6-load_from_json_file.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0B-python-input_output/6-load_from_json_file.py) - creates an Object from a “JSON file”
- Prototype: `def load_from_json_file(filename):`
- Use the `with` statement

[7-add_item.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0B-python-input_output/7-add_item.py) - a script that adds all arguments to a Python list, and then save them to a file
- Use function save_to_json_file from [5-save_to_json_file.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0B-python-input_output/5-save_to_json_file.py)
- Use your function load_from_json_file from [6-load_from_json_file.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0B-python-input_output/6-load_from_json_file.py)
- The list must be saved as a JSON representation in a file named `add_item.json`
- If the file doesn’t exist, it should be created

[8-class_to_json.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0B-python-input_output/8-class_to_json.py) - returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object
- Prototype: `def class_to_json(obj):`
- `obj` is an instance of a Class
- All attributes of the `obj` Class are serializable: list, dictionary, string, integer and boolean

[9-student.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0B-python-input_output/9-student.py) - a class `Student` that defines a student by:
- Public instance attributes:
    - `first_name`
    - `last_name`
    - `age`
- Instantiation with `first_name`, `last_name`and `age`: `def __init__(self, first_name, last_name, age):`
- Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance (same as [8-class_to_json.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0B-python-input_output/8-class_to_json.py))

[10-student.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0B-python-input_output/10-student.py) - a class `Student` that defines a student by:  (based on [9-student.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0B-python-input_output/9-student.py))
- Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance (same as [8-class_to_json.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0B-python-input_output/8-class_to_json.py)):
    - If `attrs` is a list of strings, only attribute names contained in this list must be retrieved.
    - Otherwise, all attributes must be retrieved

[11-student.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0B-python-input_output/11-student.py) - a class `Student` that defines a student by:  (based on [10-student.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0B-python-input_output/10-student.py))
- Public method `def reload_from_json(self, json):` that replaces all attributes of the `Student` instance:
  - Assume `json` will always be a dictionary
  - A dictionary key will be the public attribute name
  - A dictionary value will be the value of the public attribute
  
[12-pascal_triangle.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0B-python-input_output/12-pascal_triangle.py) - a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:
   - Returns an empty list if `n <= 0`
   - You can assume `n` will be always an integer
   
[100-append_after.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0B-python-input_output/100-append_after.py) - inserts a line of text to a file, after each line containing a specific string
- Prototype: `def append_after(filename="", search_string="", new_string=""):`
- Use the `with` statement
