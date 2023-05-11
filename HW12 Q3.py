import sqlite3
import pandas as pd

pd.options.display.max_columns = 10

connection = sqlite3.connect('books.db')

print(pd.read_sql('SELECT last FROM authors ORDER BY last DESC', connection))

print(pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection))

print(pd.read_sql("""SELECT title, copyright, author_ISBN.isbn FROM titles INNER JOIN author_ISBN ON titles.isbn = author_ISBN.isbn WHERE author_ISBN.id = '2' ORDER BY title ASC""", connection))

cursor = connection.cursor()

cursor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('Sue', 'Red')""")

cursor = cursor.execute("""INSERT INTO titles (isbn, title, edition, copyright) VALUES ('87', 'Halo: Magic Treehouse', '69', '2009')""")

cursor = cursor.execute("""INSERT INTO author_ISBN (id, isbn) VALUES ('6', '69')""")

print(pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection))

