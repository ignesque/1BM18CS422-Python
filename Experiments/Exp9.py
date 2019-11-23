import tkinter as tk
from tkinter import messagebox

def submit():
    if(v.get()==0 or var1.get()==var2.get()==var3.get()==0 or var.get()=="Select"):
        messagebox.showinfo( "Error", "Insufficient Data")
    else:
        messagebox.showinfo( "Submitted", "Booking Successful")
        

root = tk.Tk()
root.geometry("500x500")

v = tk.IntVar()

tk.Label(root, text="Choose Language:").place(relx=0.0,rely=0.0)
tk.Radiobutton(root, text="English",variable=v,value=1).place(relx=0.0,rely=0.05)
tk.Radiobutton(root,text="Kannada",variable=v,value=2).place(relx=0.0,rely=0.1)
tk.Radiobutton(root,text="Hindi",variable=v,value=3).place(relx=0.0,rely=0.15)


tk.Label(root, text="Choose Movie:").place(relx=0.0,rely=0.2)
var1 = tk.IntVar()
tk.Checkbutton(root, text="The Prestige", variable=var1).place(relx=0.0,rely=0.25)
var2 = tk.IntVar()
tk.Checkbutton(root, text="Inception", variable=var2).place(relx=0.25,rely=0.25)
var3 = tk.IntVar()
tk.Checkbutton(root, text="Memento", variable=var3).place(relx=0.5,rely=0.25)



tk.Label(root, text="Choose No. of Tickets:").place(relx=0.0,rely=0.31)
OptionList = ["Select",1,2,3,4,5]
var = tk.StringVar()
var.set(OptionList[0])
opt = tk.OptionMenu(root, var, *OptionList)
opt.place(relx=0.3,rely=0.3)

btn= tk.Button(root, text ="Book Movie", command = submit)
btn.place(relx=0.01,rely=0.38)

root.mainloop()