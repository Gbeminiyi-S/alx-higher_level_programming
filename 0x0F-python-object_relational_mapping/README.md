# 0x0F. Python - Object-relational mapping
An introductory project on:

- Why Python programming is awesome
- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table

## Requirements
- Files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Codes are checked with the pycodestyle (version 2.8.*)
- Files will be executed with MySQLdb version 2.0.x
- Files will be executed with SQLAlchemy version 1.4.x
- The first line of all files should be exactly `#!/usr/bin/python3`

## File Descriptions
### Mandatory
[0-select_states.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/0-select_states.py) - a script that lists all states from the database `hbtn_0e_0_usa`
- Must use the module `MySQLdb` `(import MySQLdb)`
- The script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `states.id`
- The code should not be executed when imported

### Advanced
