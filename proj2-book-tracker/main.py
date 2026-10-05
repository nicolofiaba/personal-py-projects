import streamlit as st
import sqlite3

# Define connection and cursor 
def init_db():
    connection = sqlite3.connect("book_tracker.db")
    cursor = connection.cursor()

    create_command = """CREATE TABLE IF NOT EXISTS
    books(book_id INTEGER PRIMARY KEY, title TEXT UNIQUE COLLATE NOCASE NOT NULL, author TEXT, 
    year INTEGER, rating INTEGER, genre TEXT, notes TEXT)"""
    cursor.execute(create_command)
    connection.commit()
    connection.close()

init_db()

pg = st.navigation([
    st.Page("pages/home.py", title="Homepage"), 
    st.Page("pages/explore.py", title="Explore")
    ])

pg.run()



