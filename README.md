Book Management System
This project is a Book Management System built using Flask, Python, and SQLite. The system allows you to manage a collection of books with functionalities to add, edit, delete, search, and track the status of books (check-in and check-out).

Features
Add a new book to the system.

Edit the details of an existing book.

Delete a book from the system.

Search for books by title or author.

Check-in and Check-out functionality to track the status of books (whether they're borrowed or returned).

Technologies Used
Flask: A lightweight web framework for building web applications.

Python: The programming language used to build the application.

SQLite: A lightweight database to store book data.

Requirements
Before running the project, make sure you have the following installed:

Python 3.x

Flask (pip install flask)

SQLite (SQLite is typically included with Python, but you can install it manually if needed)

How to Run the Application
Clone the repository to your local machine:

bash
Copy
git clone https://github.com/your-username/bookmanagmentsystem.git
Navigate to the project directory:

bash
Copy
cd bookmanagmentsystem
Install the required dependencies (if any):

bash
Copy
pip install flask
Run the application: In the project directory, run the following command to start the Flask server:

bash
Copy
python app.py
Access the application: Open your browser and go to http://127.0.0.1:5000/ to use the Book Management System.

Functionality
Manage Books: You can view, edit, and delete books in your collection.

Add Books: You can add new books with details like title, author, genre, and year.

Search: You can search books by title or author.

Check-in / Check-out: You can mark a book as checked-in or checked-out, to track if the book is borrowed or returned.

Folder Structure
bash
Copy
bookmanagmentsystem/
│
├── app.py                  # Main Python file containing the app logic
├── templates/              # HTML templates for rendering the web pages
│   ├── home.html
│   ├── manage_books.html
│   ├── add_book.html
│   └── edit_book.html
├── static/                 # Static files (e.g., CSS, JS, images)
│   └── style.css
└── books.db                # SQLite database file (stores book information)
Database Setup
The application uses SQLite as the database. The books.db file is automatically created when you first run the application. The database stores the following information for each book:

id: The unique identifier for each book (auto-incremented).

title: The title of the book.

author: The author of the book.

genre: The genre of the book.

year: The publication year of the book.

status: Tracks whether the book is available (checked-in) or borrowed (checked-out).
