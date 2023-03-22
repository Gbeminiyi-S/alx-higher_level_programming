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
```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
```

[1-filter_states.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/1-filter_states.py) - a script that lists all `states` with a `name` starting with `N` (upper N) from the database `hbtn_0e_0_usa`
- The script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
- Results must be sorted in ascending order by `states.id`
- The code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
```

[2-my_filter_states.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/2-my_filter_states.py) - a script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument
- The script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (no argument validation needed)
- Use `format` to create the SQL query with the user input
- Results must be sorted in ascending order by `states.id`
- The code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
```

[3-my_safe_filter_states.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/3-my_safe_filter_states.py) - 
a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, it is safe from MySQL injections!
- The script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (safe from MySQL injection)
- Results must be sorted in ascending order by `states.id`
- The code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
```

[4-cities_by_state.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/4-cities_by_state.py) - a script that lists all `cities` from the database `hbtn_0e_4_usa`
- The script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- Only use `execute()` once
- Results must be sorted in ascending order by `cities.id`
- The code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./4-cities_by_state.py root root hbtn_0e_4_usa
(1, 'San Francisco', 'California')
(2, 'San Jose', 'California')
(3, 'Los Angeles', 'California')
(4, 'Fremont', 'California')
(5, 'Livermore', 'California')
(6, 'Page', 'Arizona')
(7, 'Phoenix', 'Arizona')
(8, 'Dallas', 'Texas')
(9, 'Houston', 'Texas')
(10, 'Austin', 'Texas')
(11, 'New York', 'New York')
(12, 'Las Vegas', 'Nevada')
(13, 'Reno', 'Nevada')
(14, 'Henderson', 'Nevada')
(15, 'Carson City', 'Nevada')
guillaume@ubuntu:~/0x0F$ 
```

[5-filter_cities.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/5-filter_cities.py) - a script that takes in the name of a state as an argument and lists all `cities` of that state, using the database `hbtn_0e_4_usa`
- The script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (safe from MySQL injection)
- Only use `execute()` once
- Results must be sorted in ascending order by `cities.id`
- The code should not be executed when imported

[model_state.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/model_state.py) - a python file that contains the class definition of a `State` and an instance `Base = declarative_base()`
- `State` class:
    - inherits from `Base`
    - links to the MySQL table `states`
    - class attribute `id` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
    - class attribute `name` that represents a column of a string with maximum 128 characters and can’t be null
- Use the module `SQLAlchemy`
-  all classes who inherit from `Base` must be imported before calling `Base.metadata.create_all(engine)`
```
guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql
-- Create database hbtn_0e_6_usa
CREATE DATABASE IF NOT EXISTS hbtn_0e_6_usa;
USE hbtn_0e_6_usa;
SHOW CREATE TABLE states;

guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
ERROR 1146 (42S02) at line 4: Table 'hbtn_0e_6_usa.states' doesn't exist
guillaume@ubuntu:~/0x0F$ cat 6-model_state.py
#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

guillaume@ubuntu:~/0x0F$ ./6-model_state.py root root hbtn_0e_6_usa
guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
Table   Create Table
states  CREATE TABLE `states` (\n  `id` int(11) NOT NULL AUTO_INCREMENT,\n  `name` varchar(128) NOT NULL,\n  PRIMARY KEY (`id`)\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
guillaume@ubuntu:~/0x0F$ 
```
[7-model_state_fetch_all.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/7-model_state_fetch_all.py) - a script that lists all `State` objects from the database `hbtn_0e_6_usa`
- The script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- Import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Results must be sorted in ascending order by `states.id`
- The code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ cat 7-model_state_fetch_all.sql
-- Insert states
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
Enter password: 
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
guillaume@ubuntu:~/0x0F$ 
```

[8-model_state_fetch_first.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/8-model_state_fetch_first.py) - a script that prints the first `State` object from the database `hbtn_0e_6_usa`
- The script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- Import `State` and `Base` from `model_state` - `from model_state import Base, State`
- The state displayed must be the first in `states.id`
- Not allowed to fetch all states from the database before displaying the result
- If the table `states` is empty, print `Nothing` followed by a new line
- The code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
1: California
guillaume@ubuntu:~/0x0F$
```

[9-model_state_filter_a.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/9-model_state_filter_a.py) - a script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`
- The script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- Import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Results must be sorted in ascending order by `states.id`
- The code should not be executed when imported

### Advanced
