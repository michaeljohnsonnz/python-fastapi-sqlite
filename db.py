import sqlite3

def get_genres():
  with sqlite3.connect("chinook.db") as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM genres')
    genres = cursor.fetchall()
  return genres

def get_tracks():
  with sqlite3.connect("chinook.db") as conn: 
    cursor = conn.cursor()
    cursor.execute("SELECT name, composer, milliseconds FROM tracks;")
    tracks = cursor.fetchall()
  return tracks