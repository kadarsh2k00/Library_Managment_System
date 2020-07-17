from tkinter import Tk,Button,Label,Listbox,Scrollbar
from tkinter import ttk,StringVar,messagebox,N,W,E,S,END
from Database_Config import dbconfig
import pymysql

con = pymysql.connect(**dbconfig)
cursor = con.cursor()

class Bookdb:
    def __init__(self):
        self.con = pymysql.connect(**dbconfig)
        self.cursor = con.cursor()
        print('Conected to the Database')

    def __del__(self):
        self.con.close()

    def view(self):
        command = ('select * from books')
        self.cursor.execute(command)
        rows = self.cursor.fetchall()
        return rows

    def insert(self,title,author,isbn):
        command = ('INSERT INTO books(TITLE,AUTHOR,ISBN) VALUES (%s,%s,%s)')
        self.cursor.execute(command,[title,author,isbn])
        self.con.commit()
        messagebox.showinfo(title ='Book Database', message ='Book Added')

    def modify(self,id,title,author,isbn):
        command = ('UPDATE books SET TITLE = %s, AUTHOR = %s, ISBN = %s WHERE ID =%s')
        self.cursor.execute(command,[title,author,isbn,id])
        self.con.commit()
        messagebox.showinfo(title ='Book Database', message ='Book Modified')

    def delete(self,id):
        command = ('DELETE FROM books WHERE ID = %s')
        self.cursor.execute(command,[id])
        self.con.commit()
        messagebox.showinfo(title ='Book Database', message ='Book Deleted')

db = Bookdb()
def get_selected_row(event):
    global selected_tuple
    index = list_box.curselection()[0]
    selected_tuple = list_box.get(index)
    title_entry.delete(0, 'end')
    title_entry.insert('end',selected_tuple[1])
    author_entry.delete(0,'end')
    author_entry.insert('end',selected_tuple[2])
    isbn_entry.delete(0,'end')
    isbn_entry.insert('end',selected_tuple[3])

def view_records():
    list_box.delete(0, 'end')
    for row in db.view():
        list_box.insert('end', row)

def add_book():
    db.insert(title_text.get(), author_text.get(), isbn_text.get())
    list_box.delete(0, 'end')
    list_box.insert('end', (title_text.get(), author_text.get(), isbn_text.get()))
    title_entry.delete(0, 'end')
    author_entry.delete(0, 'end')
    isbn_entry.delete(0, 'end')
    con.commit()

def delete_records():
    db.delete(selected_tuple[0])
    con.commit()

def clear_screen():
    title_entry.delete(0, 'end')
    author_entry.delete(0, 'end')
    isbn_entry.delete(0, 'end')
    list_box.delete(0, 'end')

def modify_record():
    db.update(selected_tuple[0], title_text.get(), author_text.get(), isbn_text.get())
    title_entry.delete(0, 'end')
    author_entry.delete(0, 'end')
    isbn_entry.delete(0, 'end')
    con.commit()

def on_closing():
    temp = db
    if messagebox.askokcancel('Quit', 'Do you want to quit??'):
        root.destroy()
        del temp

root = Tk()
root.title('My Books Database')
root.configure(background = 'light pink')
root.geometry('940x580')
root.resizable(width=False,height=False)

title_label = ttk.Label(root, text = 'TITLE', background = 'light pink', font =('TkDefaultFont', 16))
title_label.grid(row = 0, column = 0, sticky = W, padx = 7)
title_text = StringVar()
title_entry = ttk.Entry(root, width = 24, textvariable = title_text)
title_entry.grid(row = 0, column = 1, sticky = W, padx = 7)

author_label = ttk.Label(root,text = 'AUTHOR', background = 'light pink', font =('TkDefaultFont', 16))
author_label.grid(row = 0, column = 2, sticky = W, padx = 7)
author_text = StringVar()
author_entry = ttk.Entry(root, width = 30, textvariable = author_text)
author_entry.grid(row = 0, column = 3, sticky = W, padx = 7)

isbn_label = ttk.Label(root,text = 'ISBN', background = 'light pink', font =('TkDefaultFont', 16))
isbn_label.grid(row = 0, column = 4, sticky = W, padx = 7)
isbn_text = StringVar()
isbn_entry = ttk.Entry(root, width = 24, textvariable = isbn_text)
isbn_entry.grid(row = 0, column = 5, sticky = W)

add_btn = Button(root, bg ='black', fg ='white', text ='ADD', font ='helvetica 14 bold', command = add_book)
add_btn.grid(row = 0, column = 6, sticky = W, padx = 7, pady = 5)

list_box = Listbox(root, height = 16, width = 40, font = 'helvetica 14 bold', bg ='light blue')
list_box.grid(row = 5, column = 1, columnspan = 16, sticky = W + E, pady = 40, padx = 15)
list_box.bind('<<ListboxSelect>>', get_selected_row)
scroll_bar = Scrollbar(root)
scroll_bar.grid(row = 1, column = 8, rowspan = 14, sticky = W)

list_box.configure(yscrollcommand = scroll_bar.set)
scroll_bar.configure(command = list_box.yview)

view_btn = Button(root, bg ='black', fg ='white', text ='VIEW', font='helvetica 12 bold', command =view_records)
view_btn.grid(row = 15, column = 1)

delete_btn = Button(root, bg ='black', fg ='white', text ='DELETE', font='helvetica 12 bold', command =delete_records)
delete_btn.grid(row = 15, column = 2)

modify_btn = Button(root, bg ='black', fg ='white', text ='MODIFY', font='helvetica 12 bold', command =modify_record)
modify_btn.grid(row = 15, column = 3)

clear_btn = Button(root, bg ='black', fg ='white', text ='CLEAR', font='helvetica 12 bold', command =clear_screen)
clear_btn.grid(row = 15, column = 4)

exit_btn = Button(root, bg ='black', fg ='white', text ='EXIT', font='helvetica 12 bold', command =on_closing)
exit_btn.grid(row = 15, column = 5)
root.mainloop()
