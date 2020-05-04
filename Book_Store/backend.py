import sqlite3

def connect():
    conn = sqlite3.connect("Book_Store/books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (ID INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit
    conn.close

connect()

def view_all():
    conn = sqlite3.connect("Book_Store/books.db")
    cur = conn.cursor()
    rows = cur.execute("SELECT * FROM book")
    row_data = rows.fetchall()
    conn.close
    return row_data

print(view_all())

def search_entry(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("Book_Store/books.db")
    cur = conn.cursor()
    rows = cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? or isbn = ?", (title, author, year, isbn))
    rows.fetchall()
    conn.close
    return rows

def add_entry(title, author, year, isbn):
    print(title, author, year, isbn)
    conn = sqlite3.connect("Book_Store/books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit
    conn.close

def update(id, title, author, year, isbn):
    conn = sqlite3.connect("Book_Store/books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE ID = ?", (title, author, year, isbn, id))
    cur.commit
    conn.close

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE ID = ?", (id,))
    cur.commit
    conn.close

def close():
    print("close")