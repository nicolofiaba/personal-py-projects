import streamlit as st
import sqlite3

def insert_book(book):
    connection = sqlite3.connect("book_tracker.db")
    cursor = connection.cursor()

    command = """
            INSERT INTO books (title, author, year, rating, genre, notes)
            VALUES (?, ?, ?, ?, ?, ?)
        """
    try:
        cursor.execute(command, (
            book["title"],
            book["author"],
            book["year"],
            book["rating"],
            book["genre"],
            book["notes"]
        ))
        connection.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        connection.close()



st.title("Book Tracker")
st.markdown("Insert the last book you have read and build your personal library!")

with st.form("book_form"):

    title = st.text_input("Book title")
    author = st.text_input("Author")
    year = st.text_input("Publication year")

    rating = st.slider("Rating", 1, 10, 5)

    genre = st.selectbox(
        "Genre",
        ["Novel", "Fantasy", "Science Fiction", "History", "Other"]
    )

    notes = st.text_area("Notes")
    submitted = st.form_submit_button("Add book to the library")


if submitted:

    if not title:
        st.warning("Insert at least the book title!")

    if year and not year.isnumeric():
        st.warning("Year must be a number!")

    else:
        book = {
            "title": title,
            "author": author,
            "year": year,
            "rating": rating,
            "genre": genre,
            "notes": notes
        }
        if insert_book(book):
            st.success("New book added!")
        else:
            st.warning("Book already present!")
        
