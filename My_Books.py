from tkinter import ttk,Tk,Button,Label,N,W,E,S,StringVar,Listbox,Scrollbar,END
from tkinter import messagebox

root = Tk()
root.title('My Books Database')
root.configure(background = 'light pink')
root.geometry('1024x720')
#root.resizable(width=False,height=False)

title_label = ttk.Label(root, text = 'TITLE', background = 'light pink', font =('TkDefaultFont', 16))
title_label.grid(row = 0, column = 0, sticky = W)
title_text = StringVar()
title_entry = ttk.Entry(root, width = 24, textvariable = title_text)
title_entry.grid(row = 0, column = 1, sticky = W)

author_label = ttk.Label(root,text = 'AUTHOR', background = 'light pink', font =('TkDefaultFont', 16))
author_label.grid(row = 0, column = 2, sticky = W)
author_text = StringVar()
author_entry = ttk.Entry(root, width = 30, textvariable = author_text)
author_entry.grid(row = 0, column = 3, sticky = W)

isbn_label = ttk.Label(root,text = 'ISBN', background = 'light pink', font =('TkDefaultFont', 16))
isbn_label.grid(row = 0, column = 4, sticky = W)
isbn_text = StringVar()
isbn_entry = ttk.Entry(root, width = 24, textvariable = isbn_text)
isbn_entry.grid(row = 0, column = 5, sticky = W)

submit_btn = Button(root, bg ='black', fg ='white', text ='ADD', font ='helvetica 14 bold', command = '')
submit_btn.grid(row = 0, column = 6, sticky = W)

list_box = Listbox(root, height = 16, width = 40, font = 'helvetica 14 bold', bg ='light blue')
list_box.grid(row = 5, column = 1, columnspan = 16, sticky = W + E, pady = 40, padx = 15)

scroll_bar = Scrollbar(root)
scroll_bar.grid(row = 1, column = 8, rowspan = 14, sticky = W)

list_box.configure(yscrollcommand = scroll_bar.set)
scroll_bar.configure(command = list_box.yview)
root.mainloop()
