# 0x0E. SQL - More queries
An introductory project on:

- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a `PRIMARY KEY`
- What’s a `FOREIGN KEY`
- How to use `NOT NULL` and `UNIQUE` constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
- What are `JOIN` and `UNION`

# Projects
## Mandatory
[0-privileges.sql](https://github.com/Gbeminiyi-S/alx-higher_level_programming/edit/main/0x0E-SQL_more_queries/0-privileges.sql) -  a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`)
```
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
ERROR 1141 (42000) at line 3: There is no such grant defined for user 'user_0d_1' on host 'localhost'
guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ echo "CREATE USER 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost                                                                                                
GRANT SELECT, INSERT, UPDA..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`                                                                                                                             
GRANT APPLICATION_PASSWORD_ADMIN,AUDIT...,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`                                        
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'              
guillaume@ubuntu:~/$ 
```

[1-create_user.sql](https://github.com/Gbeminiyi-S/alx-higher_level_programming/edit/main/0x0E-SQL_more_queries/1-create_user.sql) -  a script that creates the MySQL server user `user_0d_1`
- `user_0d_1` should have all privileges on your MySQL server
- The `user_0d_1` password should be set to `user_0d_1_pwd`
- If the user `user_0d_1` already exists, your script should not fail

```
guillaume@ubuntu:~/$ cat 1-create_user.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost                                                                                                
GRANT SELECT, INSERT..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`                                                                                                                             
GRANT APPLICATION_PASSWORD_ADMIN,...,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`                                        
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'
guillaume@ubuntu:~/$ 
```

[2-create_read_user.sql](https://github.com/Gbeminiyi-S/alx-higher_level_programming/edit/main/0x0E-SQL_more_queries/2-create_read_user.sql) - a script that creates the database `hbtn_0d_2` and the user `user_0d_2`
- `user_0d_2` should have only SELECT privilege in the database `hbtn_0d_2`
- The `user_0d_2` password should be set to `user_0d_2_pwd`
- If the database `hbtn_0d_2` already exists, your script should not fail
- If the user `user_0d_2` already exists, your script should not fail
```
guillaume@ubuntu:~/$ cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost                                                                                                
GRANT SELECT, ..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`                                                                                                                             
GRANT APPLICATION_PASSWORD_ADMIN,...,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`                                        
Grants for user_0d_2@localhost                                                                                                
GRANT USAGE ON *.* TO `user_0d_2`@`localhost`                                                                                 
GRANT SELECT ON `hbtn_0d_2`.* TO `user_0d_2`@`localhost`  
guillaume@ubuntu:~/$ 
```

[3-force_name.sql](https://github.com/Gbeminiyi-S/alx-higher_level_programming/edit/main/0x0E-SQL_more_queries/3-force_name.sql) - a script that creates the table `force_name` on your MySQL server
- `force_name` description:
  - `id` INT
  - `name` VARCHAR(256) can’t be null
- The database name will be passed as an argument of the `mysql` command
- If the table `force_name` already exists, your script should not fail
```
guillaume@ubuntu:~/$ cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO force_name (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ echo 'INSERT INTO force_name (id) VALUES (333);' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
ERROR 1364 (HY000) at line 1: Field 'name' doesn't have a default value
guillaume@ubuntu:~/$ echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ 
```

[4-never_empty.sql](https://github.com/Gbeminiyi-S/alx-higher_level_programming/edit/main/0x0E-SQL_more_queries/4-never_empty.sql) - a script that creates the table `id_not_null` on your MySQL server
- `id_not_null` description:
  - `id` INT with the default value 1
  - `name` VARCHAR(256)
- The database name will be passed as an argument of the `mysql` command
- If the table `id_not_null` already exists, your script should not fail
```
guillaume@ubuntu:~/$ cat 4-never_empty.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO id_not_null (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ echo 'INSERT INTO id_not_null (name) VALUES ("Best");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Best School
1   Best
guillaume@ubuntu:~/$ 
```

[5-unique_id.sql](https://github.com/Gbeminiyi-S/alx-higher_level_programming/edit/main/0x0E-SQL_more_queries/5-unique_id.sql) - a script that creates the table  `unique_id` on your MySQL server
- `unique_id` description:
  - `id` INT with the default value 1 and must be unique
  - `name` VARCHAR(256)
- The database name will be passed as an argument of the `mysql` command
- If the table `unique_id` already exists, your script should not fail
```
guillaume@ubuntu:~/$ cat 5-unique_id.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO unique_id (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ echo 'INSERT INTO unique_id (id, name) VALUES (89, "Best");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
ERROR 1062 (23000) at line 1: Duplicate entry '89' for key 'unique_id.id'
guillaume@ubuntu:~/$ echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ 
```

[6-states.sql](https://github.com/Gbeminiyi-S/alx-higher_level_programming/edit/main/0x0E-SQL_more_queries/6-states.sql) - a script that creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) on your MySQL server
- `states` description:
  - `id` INT unique, auto generated, can’t be null and is a primary key
  - `name` VARCHAR(256) can’t be null
- If the database `hbtn_0d_usa` already exists, your script should not fail
- If the table `states` already exists, your script should not fail
```
guillaume@ubuntu:~/$ cat 6-states.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  name
1   California
2   Arizona
3   Texas
guillaume@ubuntu:~/$ 
```

[7-model_state_fetch_all.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/edit/main/0x0E-SQL_more_queries/7-model_state_fetch_all.py) -  a script that lists all `State` objects from the database `hbtn_0e_6_usa`
- The script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- Import `State` and `Base` from `model_state` - `from model_state import Base, State`
- The script should connect to a MySQL server running on `localhost` at port `3306`
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

[8-model_state_fetch_first.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/edit/main/0x0E-SQL_more_queries/8-model_state_fetch_first.py) - a script that prints the first `State` object from the database `hbtn_0e_6_usa`
- The script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- Import `State` and `Base` from `model_state` - `from model_state import Base, State`
- The script should connect to a MySQL server running on `localhost` at port `3306`
- The state you display must be the first in `states.id`
- Not allowed to fetch all states from the database before displaying the result
- If the table `states` is empty, print `Nothing` followed by a new line
- The code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
1: California
guillaume@ubuntu:~/0x0F$ 
```

[9-model_state_filter_a.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/edit/main/0x0E-SQL_more_queries/9-model_state_filter_a.py) - a script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`
- The script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- Import `State` and `Base` from `model_state` - `from model_state import Base, State`
- The script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `states.id`
- The code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ ./9-model_state_filter_a.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
5: Nevada
guillaume@ubuntu:~/0x0F$ 
```

[10-model_state_my_get.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/edit/main/0x0E-SQL_more_queries/10-model_state_my_get.py) - a script that prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`
- The script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name to search`(SQL injection free)
- Import `State` and `Base` from `model_state` - `from model_state import Base, State`
- The script should connect to a MySQL server running on `localhost` at port `3306`
- Assume you have one record with the state name to search
- Results must display the `states.id`
- If no state has the name you searched for, display `Not found`
- The code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
3
guillaume@ubuntu:~/0x0F$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Illinois
Not found
guillaume@ubuntu:~/0x0F$ 
```

[11-model_state_insert.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/edit/main/0x0E-SQL_more_queries/11-model_state_insert.py) - a script that adds the `State` object "Louisiana" to the database `hbtn_0e_6_usa`
- The script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- Import `State` and `Base` from `model_state` - `from model_state import Base, State`
- The script should connect to a MySQL server running on `localhost` at port `3306`
- Prints the new `states.id` after creation
- The code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ ./11-model_state_insert.py root root hbtn_0e_6_usa 
6
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
6: Louisiana
guillaume@ubuntu:~/0x0F$ 
```

[12-model_state_update_id_2.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/edit/main/0x0E-SQL_more_queries/12-model_state_update_id_2.py) - a script that changes the name of a `State` object from the database `hbtn_0e_6_usa`
- The script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- Import `State` and `Base` from `model_state` - `from model_state import Base, State`
- The script should connect to a MySQL server running on `localhost` at port `3306`
- Change the name of the `State` where `id = 2` to `New Mexico`
- The code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ ./12-model_state_update_id_2.py root root hbtn_0e_6_usa 
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
1: California
2: New Mexico
3: Texas
4: New York
5: Nevada
6: Louisiana
guillaume@ubuntu:~/0x0F$ 
```

[13-model_state_delete_a.py](https://github.com/Gbeminiyi-S/alx-higher_level_programming/edit/main/0x0E-SQL_more_queries/13-model_state_delete_a.py) - a script that deletes all `State` objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`
- The script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- Import `State` and `Base` from `model_state` - `from model_state import Base, State`
- The script should connect to a MySQL server running on `localhost` at port `3306`
- The code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ ./13-model_state_delete_a.py root root hbtn_0e_6_usa 
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
2: New Mexico
4: New York
guillaume@ubuntu:~/0x0F$
```
