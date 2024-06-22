# 0x0D. SQL - Introduction
To start mysql server and run scripts, you may follow the example below:

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
### Precaution
Make sure you maintain a chronological follow up of the files to have a clear understanding and a nice😀 learning frame work for the SQL code inside them, as most of the files depend on the preceding ones.

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
|10-top_score.sql			|a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server with results having both the score and the name (in this order) and ordered by score (top first). The database name will be passed as an argument of the `mysql` command |
|11-best_score.sql		|a script that lists all records with a `score >= 10` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server with results having both the score and the name (in this order) and ordered by score (top first). The database name will be passed as an argument of the `mysql` command |
|12-no_cheating.sql		|a script that updates the score of Bob to `10` in the table `second_table`. The database name will be passed as an argument of the `mysql` command	|
|13-change_class.sql		|a script that removes all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server. The database name will be passed as an argument of the `mysql` command |
|14-average.sql			|a script that computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in your MySQL server with the result column as `average`. The database name will be passed as an argument of the `mysql` command|
|15-groups.sql			|a script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in your MySQL server with the results displaying the `score` and the number of records for this `score` with the label `number` sorted by the number of records (descending). The database name will be passed as an argument to the `mysql` command |
|16-no_link.sql			|a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server but not listing rows without a `name` value, results displaying the score and the name (in this order) and records listed by descending score. The database name will be passed as an argument to the `mysql` command |
|100-move_to_utf8.sql		|a script that converts `hbtn_0c_0` database to UTF8 (`utf8mb4`, collate `utf8mb4_unicode_ci`) in your MySQL server plus the table `first_table` in `hbtn_0c_0` database and the field `name` in the table|
|101-avg_temperatures.sql, temperatures.sql| a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending). Import `temparatures.sql` into `hbtn_0c_0` database|
|102-top_city.sql	|a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending). run `cat 102-top_city.sql | mysql -hlocalhost -uroot -p hbtn_0c_0`|
|103-max_state.sql	| a script that displays the max temperature of each state (ordered by State name)|
