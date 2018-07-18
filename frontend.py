from backend import *
from tkinter import *

class Window:
	entries_data = {}
	listboxes_data = {}
	db = None
	selected_tuple = None

	def __init__(self):
		self.app = Tk()
		self.app.wm_title("BookStore")
		self.db = Database()

	def add_label(self, text, row, column):
		label = Label(self.app, text=text)
		label.grid(row=row, column=column)

	def add_entry(self, name, row, column):
		entry_text = StringVar()
		entry = Entry(self.app, textvariable=entry_text)
		entry.grid(row=row, column=column)
		self.entries_data[name] = {'element': entry, 'text': entry_text}

	def add_listbox(self, name):
		listElem = Listbox(self.app, height=10, width=35)
		listElem.grid(row=2, column=0, rowspan=6, columnspan=2)

		scrollbar = Scrollbar(self.app)
		scrollbar.grid(row=2, column=2, rowspan=6)

		listElem.bind("<<ListboxSelect>>", self.get_selected_row)

		listElem.configure(yscrollcommand=scrollbar.set)
		scrollbar.configure(command=listElem.yview)

		self.listboxes_data[name] = listElem

	def add_button(self, text, row, column, command):
		button = Button(self.app, text=text, command=command)
		button.grid(row=row, column=column)

	def get_selected_row(self, event):
		listbox = self.listboxes_data['books']
		title = self.entries_data['title']['element']
		author = self.entries_data['author']['element']
		year = self.entries_data['year']['element']
		isbn = self.entries_data['isbn']['element']

		title.delete(0, END)
		author.delete(0, END)
		year.delete(0, END)
		isbn.delete(0, END)

		if (listbox.curselection()):
			index = listbox.curselection()[0]
			self.selected_tuple = listbox.get(index) 

			title.insert(END, self.selected_tuple[1])
			author.insert(END, self.selected_tuple[2])
			year.insert(END, self.selected_tuple[3])
			isbn.insert(END, self.selected_tuple[4])

	def view_command(self):
		listbox = self.listboxes_data['books']
		listbox.delete(0, END)
		for row in self.db.view():
			listbox.insert(END, row)	

	def search_command(self):
		listbox = self.listboxes_data['books']
		title = self.entries_data['title']['text'].get()
		author = self.entries_data['author']['text'].get()
		year = self.entries_data['year']['text'].get()
		isbn = self.entries_data['isbn']['text'].get()

		listbox.delete(0, END)
		for row in self.db.search(title, author, year, isbn):
			listbox.insert(END, row)	

	def add_command(self):
		listbox = self.listboxes_data['books']
		title = self.entries_data['title']['text'].get()
		author = self.entries_data['author']['text'].get()
		year = self.entries_data['year']['text'].get()
		isbn = self.entries_data['isbn']['text'].get()

		self.db.insert(title, author, year, isbn)
		listbox.delete(0, END)
		listbox.insert(END, (title, author, year, isbn))

	def update_command(self):
		listbox = self.listboxes_data['books']
		title = self.entries_data['title']['text'].get()
		author = self.entries_data['author']['text'].get()
		year = self.entries_data['year']['text'].get()
		isbn = self.entries_data['isbn']['text'].get()

		self.db.update(self.selected_tuple[0], title, author, year, isbn)
		listbox.delete(0, END)
		listbox.insert(END, (title, author, year, isbn))			

	def delete_command(self):
		self.db.delete(self.selected_tuple[0])
		self.view_command()

		title = self.entries_data['title']['element']
		author = self.entries_data['author']['element']
		year = self.entries_data['year']['element']
		isbn = self.entries_data['isbn']['element']

		title.delete(0, END)
		author.delete(0, END)
		year.delete(0, END)
		isbn.delete(0, END)