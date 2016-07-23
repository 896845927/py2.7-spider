#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# import tkMessageBox

from spider_main import Spider


class Select(Frame):
    def __init__(self, list, spider, master=None):
        Frame.__init__(self, master)
        self.Combobox = tkinter.ttk.Combobox(self, text="", values=list, width=30)
        self.label = Label(self, text="Keyword")
        self.Entry = Entry(self)
        self.button = Button(self, text='craw', command=self.craw)
        self.Combobox.grid(row=0, column=0, sticky=N)
        self.label.grid(row=0, column=1, sticky=N)
        self.Entry.grid(row=0, column=2, sticky=N)
        self.button.grid(row=0, column=3, sticky=N)
        self.grid()

    def craw(self):
        keyword = self.Entry.get()
        domain = self.Combobox.get()
        print(keyword,domain)
        spider.craw(domain, keyword)
        tkinter.messagebox.showinfo('Message', 'done')
spider = Spider()
app = Select(["http://www.metacritic.com"], spider)
app.mainloop()