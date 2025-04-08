from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Manage books route
@app.route('/manage_books', methods=['GET', 'POST'])
def manage_books():
    search_query = request.args.get('query', '')
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()

    if search_query:
        cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", ('%' + search_query + '%', '%' + search_query + '%'))
    else:
        cursor.execute("SELECT * FROM books")
    
    books = cursor.fetchall()
    conn.close()
    return render_template('manage_books.html', books=books, search_query=search_query)

# Edit book route
@app.route('/edit_book/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()

    # Fetch the book details by ID
    cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
    book = cursor.fetchone()

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        year = request.form['year']

        # Update the book details in the database
        cursor.execute("""
            UPDATE books
            SET title = ?, author = ?, genre = ?, year = ?
            WHERE id = ?
        """, (title, author, genre, year, book_id))
        conn.commit()
        conn.close()

        return redirect(url_for('manage_books'))

    conn.close()
    return render_template('edit_book.html', book=book)

# Delete book route
@app.route('/delete_book/<int:book_id>', methods=['GET'])
def delete_book(book_id):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()

    # Delete the book from the database
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()

    return redirect(url_for('manage_books'))

# Add book route (form to add a book)
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        year = request.form['year']

        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, genre, year) VALUES (?, ?, ?, ?)",
                       (title, author, genre, year))
        conn.commit()
        conn.close()

        return redirect(url_for('manage_books'))

    return render_template('add_book.html')

if __name__ == '__main__':
    app.run(debug=True)
