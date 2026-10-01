import streamlit as st
import pandas as pd
import sqlite3

def delete_book(book_id):
    conn = sqlite3.connect("book_tracker.db")
    cursor = conn.cursor()

    command = """
        DELETE FROM books 
        WHERE book_id = ?
        """
    cursor.execute(command, (book_id,))
    conn.commit()
    conn.close()

@st.dialog("Book notes")
def show_notes(title, notes):
    st.write(f"### {title}")
    st.write(notes)

def on_click_notes():
    click = st.session_state.show_notes
    book = df.iloc[click["row"]]
    show_notes(book["title"], book["notes"])

columns = ["title", "author", "year", "rating", "genre"]
            
st.title("Your books")

connection = sqlite3.connect('book_tracker.db')

df = pd.read_sql_query("SELECT * FROM books", connection)

df["notes_button"] = "📝"
df["delete"] = False

edited_df = st.data_editor(
    df.drop(columns=["notes"]),
    column_config={
        "notes_button": st.column_config.ButtonColumn(
            "Notes",
            help="Show book notes",
            width="small",
            on_click = on_click_notes,
            key="show_notes"
        ),
        "delete": st.column_config.CheckboxColumn(
            "Delete",
            width="small"
        )
    },
    hide_index=True
)

if st.button("Delete selected", key=f"delete_selected"):
    selected = edited_df[edited_df['delete']]

    for book_id in selected["book_id"]:
        delete_book(book_id)
    st.rerun()




