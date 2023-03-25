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

## Projects
### Mandatory
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

[7-cities.sql](./7-cities.sql): a script that creates the database `hbtn_0d_usa` with a table `cities`
- `cities` description:
    - `id`: INT (unique, auto-generated, cannot be null and is a primary key)
    - `state_id`: INT (cannot be null, foreign key that references to id of the
    `states` table)
    - `name`: VARCHAR(256) (cannot be null)


[8-cities_of_california_subquery.sql](./8-cities_of_california_subquery.sql): a script that lists all the cities of California that can be found in the database `hbtn_0d_usa`, ordered by ascending `cities.id`

[9-cities_by_state_join.sql](./9-cities_by_state_join.sql): a script that lists all cities contained in the database `hbtn_0d_usa`, ordered by ascending `cities.id`
- Each record should display: `cities.id` - `cities.name` - `states.name`
- Only one `SELECT` statement


[10-genre_id_by_show.sql](./10-genre_id_by_show.sql): a script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked, in order of ascending `tv_shows.title` and `tv_show_genres.genre_id`
- Only one `SELECT` statement

[11-genre_id_all_shows.sql](./11-genre_id_all_shows.sql): a script that lists all shows contained in the database `hbtn_0d_tvshows`, in order of ascending `tv_shows.title` and `tv_show_genres.genre_id`
- Each record should display: `tv_shows.title` - `tv_show_genres.genre_id`
- If a show does not have a genre, displays `NULL`.


[12-no_genre.sql](./12-no_genre.sql): a script that lists all shows contained in   `hbtn_0d_tvshows` without a genre linked, in order of ascending `tv_shows.title` and `tv_show_genres.genre_id`.

* **13. Number of shows by genre**
  * [13-count_shows_by_genre.sql](./13-count_shows_by_genre.sql): MySQL script that lists all genres from
  `hbtn_0d_tvshows` and displays the number of shows linked to each, in order of descending number of shows linked.
  * Does not display a genre if it has no linked shows.

* **14. My genres**
  * [14-my_genres.sql](./14-my_genres.sql): MySQL script that uses the `hbtn_0d_tvshows` database
  to list all genres of the show Dexter, in order of ascending genre name.

* **15. Only Comedy**
  * [15-comedy_only.sql](./15-comedy_only.sql): MySQL script that lists all comedy shows in the
  database `hbtn_0d_tvshows`, in order of ascending show title.

* **16. List shows and genres**
  * [16-shows_by_genre.sql](./16-shows_by_genre.sql): MySQL script that lists all shows, and all genres
  linked to that show, from the database `hbtn_0d_tvshows`, in order of ascending show title and genre name.

* **17. Not my genre**
  * [100-not_my_genres.sql](./100-not_my_genres.sql`) MySQL script that uses the `hbtn_0d_tvshows`
  database to list all genres not linked to the show Dexter, in order of ascending genre name.

* **18. No Comedy tonight!**
  * [101-not_a_comedy.sql](./101-not_a_comedy.sql): MySQL script that lists all shows without the
  genre comedy in the database `hbtn_0d_tvshows`, in order of ascending show title.

* **19. Rotten tomatoes**
  * [102-rating_shows.sql](./102-rating_shows.sql): MySQL script that lists all shows from
  `hbtn_0d_tvshows_rate` by their rating, in order of descending rating.

* **20. Best genre**
  * [103-rating_genres.sql](./103-rating_genres.sql): MySQL script that lists all genres in the
  database `hbtn_0d_tvshows_rate` by their rating, in order of descending rating.
