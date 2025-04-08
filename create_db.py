import sqlite3

# Create a database connection
conn = sqlite3.connect('books.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table to store books
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT NOT NULL,
    year INTEGER NOT NULL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database created and table 'books' is set up!")
