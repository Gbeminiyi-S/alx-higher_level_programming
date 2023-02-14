# 0x0D. SQL - Introduction
An introductory project on:

- What’s a database
- What’s a relational database
- What does SQL stand for
- What’s MySQL
- How to create a database in MySQL
- What does `DDL` and `DML` stand for
- How to `CREATE` or `ALTER` a table
- How to `SELECT` data from a table
- How to `INSERT`, `UPDATE` or `DELETE` data
- What are `subqueries`
- How to use MySQL functions

## Requirements
- files are to be executed on Ubuntu 20.04 LTS using `MySQL 8.0` (version 8.0.25)
## File Descriptions
### Mandatory
[0-list_databases.sql](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/0-list_databases.sql) - a script that lists all databases of your MySQL server

[1-create_database_if_missing.sql](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/1-create_database_if_missing.sql) - a script that creates the database `hbtn_0c_0` in your MySQL server
- If the database `hbtn_0c_0` already exists, your script should not fail
- Not allowed to use the `SELECT` or `SHOW` statements

[2-remove_database.sql](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/2-remove_database.sql) - a script that deletes the database `hbtn_0c_0` in your MySQL server
- the database `hbtn_0c_0` doesn’t exist, your script should not fail
- Not allowed to use the `SELECT` or `SHOW` statements

[3-list_tables.sql](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/3-list_tables.sql) - a script that lists all the tables of a database in your MySQL server
- The database name will be passed as argument of `mysql` command

[4-first_table.sql](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/4-first_table.sql) - a script that creates a table called `first_table` in the current database in your MySQL server
- `first_table` description:
    - `id` INT
    - `name` VARCHAR(256)
- The database name will be passed as an argument of the `mysql` command
- If the table `first_table` already exists, your script should not fail
- Not allowed to use the `SELECT` or `SHOW` statements

[5-full_table.sql](https://github.com/Gbeminiyi-S/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/5-full_table.sql) - a script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server
- The database name will be passed as an argument of the `mysql` command
- Not allowed to use the `DESCRIBE` or `EXPLAIN` statements
