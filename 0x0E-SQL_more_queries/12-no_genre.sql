-- Create the hbtn_0d_tvshows database: echo "CREATE DATABASE hbtn_0d_tvshows" | mysql -hlocalhost -uroot -p
-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download as follows;
-- curl https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
-- Alternatively you may: cat hbtn_0d_tvshows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows

-- lists all shows contained in hbtn_0d_tvshows without a genre linked

SELECT tv_shows.title, tv_show_genres.genre_id
     FROM tv_shows
LEFT JOIN tv_show_genres
       ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_show_genres.genre_id IS NULL
 ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
