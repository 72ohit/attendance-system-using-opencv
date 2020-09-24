# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 21:26:32 2020

@author: Rohit
"""


from tkinter import *
import tkinter.ttk as ttk
import csv
import combine

root = Tk()
root.title("Python - Import CSV File To Tkinter Table")
width = 1000
height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)


TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Id", "Name", "Date","Time"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Id', text="Id", anchor=W)
tree.heading('Name', text="Name", anchor=W)
tree.heading('Date', text="Date", anchor=W)
tree.heading('Time', text="Time", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=300)
tree.column('#2', stretch=NO, minwidth=0, width=300)
tree.column('#3', stretch=NO, minwidth=0, width=300)
tree.column('#4', stretch=NO, minwidth=0, width=300)
tree.pack()

with open('C:/Users/Rohit/Desktop/project/combined_csv.csv', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        Id = row['Id']
        Name = row['Name']
        Date = row['Date']
        Time = row['Time']
        tree.insert("", 0, values=(Id, Name, Date, Time))
        
    

    root.mainloop()
    
    
