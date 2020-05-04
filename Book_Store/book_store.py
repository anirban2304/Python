import tkinter as tk
import backend as bk

def get_selected(event):
    index = list1.curselection()[0]
    global selected_item
    selected_item = list1.get(index)
    
window = tk.Tk()

def view_all():
    list1.delete(0, tk.END)
    for row in bk.view_all():
        list1.insert(tk.END, row)

def search_entry():
    title = title_txt.get()
    author = author_txt.get()
    year = year_txt.get()
    isbn = isbn_txt.get()

    list1.delete(0, tk.END)
    for row in bk.search_entry(title, author, year, isbn):
        list1.insert(tk.END, row)

def add_entry():
    title = title_txt.get()
    author = author_txt.get()
    year = year_txt.get()
    isbn = isbn_txt.get()
    bk.add_entry(title, author, year, isbn)
    list1.delete(0, tk.END)
    list1.insert(tk.END, (title, author, year, isbn))

l1 = tk.Label(window, text = "Title")
l2 = tk.Label(window, text = "Author")
l3 = tk.Label(window, text = "Year")
l4 = tk.Label(window, text = "ISBN")

l1.grid(row = 0, column =0)
l2.grid(row = 0, column =2)
l3.grid(row = 1, column =0)
l4.grid(row = 1, column =2)

b1 = tk.Button(window, text = "View All", width = 12, command = view_all)
b2 = tk.Button(window, text = "Search Entry", width = 12, command = search_entry)
b3 = tk.Button(window, text = "Add Entry", width = 12, command = add_entry)
b4 = tk.Button(window, text = "Update", width = 12)
b5 = tk.Button(window, text = "Delete", width = 12)
b6 = tk.Button(window, text = "Close", width = 12)

b1.grid(row = 2, column = 3)
b2.grid(row = 3, column = 3)
b3.grid(row = 4, column = 3)
b4.grid(row = 5, column = 3)
b5.grid(row = 6, column = 3)
b6.grid(row = 7, column = 3)

title_txt = tk.StringVar()
e1 = tk.Entry(window, textvariable = title_txt)
e1.grid(row = 0, column = 1)

author_txt = tk.StringVar()
e2 = tk.Entry(window, textvariable = author_txt)
e2.grid(row = 0, column = 3)

year_txt = tk.StringVar()
e3 = tk.Entry(window, textvariable = year_txt)
e3.grid(row = 1, column = 1)

isbn_txt = tk.StringVar()
e4 = tk.Entry(window, textvariable = isbn_txt)
e4.grid(row = 1, column = 3)

list1 = tk.Listbox(window, height = 6, width = 35)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

sb1 = tk.Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)
list1.bind('<<ListboxSelect>>', get_selected)

window.mainloop()