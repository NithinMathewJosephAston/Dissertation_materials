# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from threadsafe_tkinter import *
from GUI import Gui
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gui = Gui()
    gui.lable1.grid(row=1)
    gui.entry1.grid(row=1, column=1)
    gui.lable2.grid(row=2)
    gui.scrollbar.grid(row=2, column=1)
    gui.article.grid(row=2, column=1)
    mainloop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
