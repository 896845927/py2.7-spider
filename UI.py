#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
import ttk
import tkMessageBox
import tkFileDialog
import re
import craw_thread


class Select(Frame):
    def __init__(self, list, master=None):
        Frame.__init__(self, master)
        self.keywords = None
        self.file = ttk.Button(self, text='choose-keywords-file', command=self.openFile)
        self.Combobox = ttk.Combobox(self, text="", values=list, width=30)
        self.button = ttk.Button(self, text='craw', command=self.craw)
        self.file.grid(row=0, column=0, sticky=N)
        self.Combobox.grid(row=0, column=1, sticky=N)
        self.button.grid(row=0, column=2, sticky=N)
        self.grid()

    def craw(self):
        if self.keywords is None or len(self.keywords)==0:
            tkMessageBox.showinfo('Error', 'Need input search file!')
            return
        if self.Combobox.get() is None or len(self.Combobox.get())==0:
            tkMessageBox.showinfo('Error', 'Need select one website!')
            return
        domain = self.Combobox.get()
        threads = []
        for keyword in self.keywords:
            print(keyword)
            t = craw_thread.CrawThread(domain, keyword)
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        tkMessageBox.showinfo('Message', 'done')

    def openFile(self):
        file_path = tkFileDialog.askopenfilename()
        try:
            with open(file_path, "r") as f:
                self.keywords = map(lambda item: re.sub('\n', '', item), f.readlines())
        except:
                print('can not read search keyword')
# spider = Spider()
app = Select(["http://www.metacritic.com"])
app.mainloop()