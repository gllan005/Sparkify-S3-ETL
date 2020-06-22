<h1> Sparkify S3 ETL Project <h1>

<h2>Fact Table</h2>
songplays - records in log data associated with song plays i.e. records with page NextSong

songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

<h2>Dimension Tables</h2>
users - users in the app Fields - user_id, first_name, last_name, gender, level

songs - songs in music database Fields - song_id, title, artist_id, year, duration

artists - artists in music database Fields - artist_id, name, location, lattitude, longitude

time - timestamps of records in songplays broken down into specific units Fields - start_time, hour, day, week, month, year, weekday