# 0x0E. SQL - More queries

## Expect to learn:
* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* What’s a PRIMARY KEY
* What’s a FOREIGN KEY
* How to use NOT NULL and UNIQUE constraints
* How to retrieve datas from multiple tables in one request
* What are subqueries
* What are JOIN and UNION

|File				|Description						|
|-----------------------|-----------------------------------------------|
|0-privileges.sql		| a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`) |
|1-create_user.sql	|a script that creates the MySQL server user `user_0d_1`	|
|2-create_read_user.sql	|a script that creates the database `hbtn_0d_2` and the user `user_0d_2`	|
|3-force_name.sql		| a script that creates the table `force_name` on your MySQL server. The database name will be passed as an argument of the mysql command ie `cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2`	|
|4-never_empty.sql	|a script that creates the table `id_not_null` on your MySQL server |
|5-unique_id.sql		|a script that creates the table `unique_id` on your MySQL server		|
|6-states.sql		| a script that creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) on your MySQL server 	|
|7-cities.sql		|a script that creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) on your MySQL server|
|8-cities_of_california_subquery.sql|a script that lists all the cities of California that can be found in the database `hbtn_0d_usa` |
|9-cities_by_state_join.sql|a script that lists all cities contained in the database `hbtn_0d_usa` |
|10-genre_id_by_show.sql|a script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked. The database name will be passed as an argument of the `mysql` command ie `cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows`	|
|11-genre_id_all_shows.sql|a script that lists all shows contained in the database `hbtn_0d_tvshows` including those with `NULL` in `tv_shows.title`. The database name will be passed as an argument of the `mysql` command|
|12-no_genre.sql		|a script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked. The database name will be passed as an argument of the `mysql` command. ie `cat 12-no_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows` |

