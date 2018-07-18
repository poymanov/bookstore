from frontend import *

window = Window()

window.add_label("Title", 0, 0)
window.add_label("Author", 0, 2)
window.add_label("Year", 1, 0)
window.add_label("ISBN", 1, 2)

window.add_entry('title', 0, 1)
window.add_entry('author', 0, 3)
window.add_entry('year', 1, 1)
window.add_entry('isbn', 1, 3)

window.add_listbox('books')

window.add_button('View all', 2, 3, window.view_command)
window.add_button('Search entry', 3, 3, window.search_command)
window.add_button('Add entry', 4, 3, window.add_command)
window.add_button('Update selected', 5, 3, window.update_command)
window.add_button('Delete selected', 6, 3, window.delete_command)
window.add_button('Close', 7, 3, window.app.destroy)

window.view_command()

window.app.mainloop()