from threadsafe_tkinter import *


class Gui(object):
    def __init__(self):
        self.pixel = Tk()
        self.resolution = self.pixel.geometry("600x300")
        self.lable1 = Label(self.resolution, text="Query", foreground='red')
        self.entry1 = Entry(width=90, bd=3)
        self.scrollbar = Scrollbar(self.pixel)
        self.lable2 = Label(self.resolution, text="Article of Interest", foreground='red')
        self.article = Listbox(self.pixel, yscrollcommand=self.scrollbar.set, width=90, bd=3)
        for line in range(100):
            self.article.insert(END, "Content line number " + str(line))
        self.scrollbar.config(command=self.article.yview)
    pass
