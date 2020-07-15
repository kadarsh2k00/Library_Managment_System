from tkinter import ttk,Tk,Button,Label,N,W,E,S,StringVar,Listbox,Scrollbar,END
from tkinter import messagebox

root = Tk()
root.title('My Books Database')
root.configure(background = 'light blue')
root.geometry('1024x720')
root.resizable(width=False,height=False)

title_label = ttk.Label(root, text = 'TITLE', background = 'light blue', font =('TkDefaultFont', 16))
title_label.grid(row = 0, column = 0, sticky = W)
title_text = StringVar()
title_entry = ttk.Entry(root, width = 24, textvariable = title_text)
title_entry.grid(row = 0, column = 1, sticky = W)

author_label = ttk.Label(root,text = 'AUTHOR', background = ' light blue', font =('TkDefaultFont', 16))
author_label.grid(row = 0, column = 3, sticky = W)
author_text = StringVar()
author_entry = ttk.Entry(root, width = 30, textvariable = author_text)
author_entry.grid(row = 0, column = 4, sticky = W)

isbn_label = ttk.Label(root,text = 'ISBN', background = ' light blue', font =('TkDefaultFont', 16))
isbn_label.grid(row = 0, column = 6, sticky = W)
isbn_text = StringVar()
isbn_entry = ttk.Entry(root, width = 24, textvariable = isbn_text)
isbn_entry.grid(row = 0, column = 7, sticky = W)
root.mainloop()
