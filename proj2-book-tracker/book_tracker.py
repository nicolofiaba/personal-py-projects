import streamlit as st

st.set_page_config(
    page_title="Book Tracker", 
    page_icon=":bar_chart:", 
    layout="centered"
)

class BookTracker:
    def __init__(self):
        self.books = []