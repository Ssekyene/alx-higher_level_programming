# 0x0D. SQL - Introduction
To start mysql server and run scripts, you may follow the exxample below:

```
$ service mysql start
 * Starting MySQL database server mysqld
$
$ cat 0-list_databases.sql | mysql -uroot -p
Database
information_schema
mysql
performance_schema
sys
$
```

|File					|Description						|
|-----------------------------|-----------------------------------------------|
|0-list_databases.sql		| a script that lists all databases of your MySQL server|
|1-create_database_if_missing.sql|a script that creates the database `hbtn_0c_0` in your MySQL server if it does not exist|
|2-remove_database.sql		|a script that deletes the database `hbtn_0c_0` in your MySQL server if it exists|
|3-list_tables.sql		|a script that lists all the tables of a database in your MySQL server. The database name will be passed as argument of mysql command eg `cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql` |
|4-first_table.sql		|a script that creates a table called `first_table` in the current database in your MySQL server if it does not exist. The database name will be passed as an argument of the `mysql` command as in `3-list_tables.sql` |
|5-full_table.sql			|a script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server. The database name will be passed as an argument of the `mysql` command. |
|6-list_values.sql		|a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server. The database name will be passed as an argument of the `mysql` command |
|7-insert_value.sql		|a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server. The database name will be passed as an argument of the `mysql` command|
|8-count_89.sql			|a script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in your MySQL server |
|9-full_creation.sql		|a script that creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiples rows. The database name will be passed as an argument to the `mysql` command |

