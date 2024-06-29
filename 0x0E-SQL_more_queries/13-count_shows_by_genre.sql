-- Create the hbtn_0d_tvshows database: echo "CREATE DATABASE hbtn_0d_tvshows" | mysql -hlocalhost -uroot -p
-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download as follows;
-- curl https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
-- Alternatively you may: cat hbtn_0d_tvshows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows

-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

SELECT tv_genres.name AS genre, COUNT(*) AS 'number_of_shows'
      FROM tv_genres
INNER JOIN tv_show_genres
        ON tv_genres.id = tv_show_genres.genre_id
  GROUP BY genre
  ORDER BY number_of_shows DESC;
