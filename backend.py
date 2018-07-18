import sqlite3


class Database:
	DB_FILE = 'app.db'

	def __init__(self):
		self.connect()
		self.cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
		self.commit_close()

	def connect(self):
		self.conn = sqlite3.connect(self.DB_FILE)
		self.cur = self.conn.cursor()

	def commit_close(self):
		self.conn.commit()
		self.conn.close()		

	def close(self):
		self.conn.commit()
		
	def insert(self, title, author, year, isbn):
		self.connect()
		self.cur.execute("INSERT INTO books VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
		self.commit_close()	

	def view(self):
		self.connect()
		self.cur.execute("SELECT * FROM books")
		rows = self.cur.fetchall()
		self.close()
		return rows

	def search(self, title="", author="", year="", isbn=""):
		self.connect()
		self.cur.execute("SELECT * FROM books WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
		rows = self.cur.fetchall()
		self.close()
		return rows	

	def delete(self, id):
		self.connect()
		self.cur.execute("DELETE FROM books WHERE id=?", (id,))
		self.commit_close()	

	def update(self, id, title, author, year, isbn):
		self.connect()
		self.cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
		self.commit_close()	