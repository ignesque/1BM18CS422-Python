import tkinter as tk
from tkinter import messagebox
from tkinter import font

p1,p2,p3=30,20,25

def order():
    s=0
    s=p1*int(i1.get())+p2*int(i2.get())+p3*int(i3.get())
    messagebox.showinfo( "Bill", "Total = Rs."+str(s))
        

root = tk.Tk()
root.geometry("500x500")
root.title("Menu")



Hel=font.Font(family='Helvetica', size=12, weight='bold')
HelTitle=font.Font(family='Helvetica', size=32, weight='bold')

title=tk.Label(root, text="Order Up")
title.config(font=HelTitle)
title.place(relx=0.01,rely=0.0)


tk.Label(root, text="Kerala Parotta\t\t\t30",font=Hel).place(relx=0.02,rely=0.12)
tk.Label(root, text="Malabar Parotta\t\t\t20",font=Hel).place(relx=0.02,rely=0.17)
tk.Label(root, text="Ceylon Parotta\t\t\t25",font=Hel).place(relx=0.02,rely=0.22)


i1 = tk.IntVar()
i2 = tk.IntVar()
i3 = tk.IntVar()


i1=tk.Spinbox(root, from_= 0, to = 10,width=3,font=Hel)
i1.place(relx=0.7,rely=0.12)
i2=tk.Spinbox(root, from_= 0, to = 10,width=3,font=Hel)
i2.place(relx=0.7,rely=0.17)
i3=tk.Spinbox(root, from_= 0, to = 10,width=3,font=Hel)
i3.place(relx=0.7,rely=0.22)


btn= tk.Button(root, text ="Order", font= Hel, command = order)
btn.place(relx=0.01,rely=0.3)

root.mainloop()
