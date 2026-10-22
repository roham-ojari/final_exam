from tkinter import *
from tkinter import messagebox
import data
####################################################################################################
win=Tk()
win.resizable(0,0)
win.geometry('850x600+400+150')
win.title("DATA")
win.config(bg="light blue")
db1 = data.database("D:/project_final/concact.db")
####################################################################################################
def exit():
    ans = messagebox.askquestion("are you sure","Are you sure to leave")
    if ans == "yes":
         win.destroy()

def clear():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_password.delete(0,END)
    ent_password2.delete(0,END)
    ent_cname.delete(0,END)
    ent_fname.focus()

def remove():
    global record
    index = lst_box.curselection()
    name = db1.select_record()
    record = name[index[0]]
    ask = messagebox.askquestion("SURE","ARE YOU SURE TO DELETE ?")
    if ask == "yes":
        db1.remove_item(record[0])
        show()

def show():
    names = db1.select_record()
    lst_box.delete(0,END)
    for name in names:
        lst_box.insert(END,name)

def insert():

    fname = ent_fname.get()
    lname = ent_lname.get()
    password = ent_password.get()
    cname = ent_cname.get()
    db1.insert_record(fname,lname,password,cname)
    lst_box.insert(0,f"{fname}_{lname}_{password}_{cname}")
    clear()

def select(envent):
    global record
    index = lst_box.curselection()
    index = index[0]
    names = db1.select_record()
    record = names[index]

    ent_fname.delete(0, END)
    ent_lname.delete(0, END)
    ent_password.delete(0, END)
    ent_cname.delete(0, END)

    ent_fname.insert(0, record[1])
    ent_lname.insert(0, record[2])
    ent_password.insert(0, record[3])
    ent_cname.insert(0, record[4])

def search():
    password = ent_password2.get().strip()
    lst_box.delete(0, END)
    record = db1.search(password)
    if record:
        messagebox.showinfo("vorod","KHOSH AMADID")
        clear()
    else:
        messagebox.showerror("error","ETELAT SAHIH NIST")
        clear()

####################################################################################################

lbl_fname=Label(win,text='NAME :',font=("Comic Sans MS", 12, "bold"),bg="light blue")
lbl_fname.place(x=10,y=20)

ent_fname=Entry(win,width=20,font=("Comic Sans MS", 12, "bold"))
ent_fname.place(x=130,y=20)

lbl_lname=Label(win,text='FAMILY :',font=("Comic Sans MS", 12, "bold"),bg="light blue")
lbl_lname.place(x=400,y=20)

ent_lname=Entry(win,width=20,font=("Comic Sans MS", 12, "bold"))
ent_lname.place(x=550,y=20)

lbl_password=Label(win,text='PASSWORD :',font=("Comic Sans MS", 12, "bold"),bg="light blue")
lbl_password.place(x=10,y=80)

ent_password=Entry(win,width=20,font=("Comic Sans MS", 12, "bold"),show="*")
ent_password.place(x=130,y=80)

lbl_cname=Label(win,text='COURSE NAME :',font=("Comic Sans MS", 12, "bold"),bg="light blue")
lbl_cname.place(x=400,y=80)

ent_cname=Entry(win,width=20,font=("Comic Sans MS", 12, "bold"))
ent_cname.place(x=550,y=80)

lbl_password2=Label(win,text='PASSWORD :',font=("Comic Sans MS", 12, "bold"),bg="light blue")
lbl_password2.place(x=20,y=500)

ent_password2=Entry(win,width=35,font=("Comic Sans MS", 12, "bold"),show="*")
ent_password2.place(x=150,y=500)
##########################################################################################################

btn_show=Button(win,text='SHOW ',font=("Comic Sans MS", 12, "bold"),width=15,command=show)
btn_show.place(x=600,y=160)

btn_insert=Button(win,text='INSERT',font=("Comic Sans MS", 12, "bold"),width=15,command=insert)
btn_insert.place(x=600,y=220)

btn_clear=Button(win,text='CLEAR',font=("Comic Sans MS", 12, "bold"),width=15,command=clear)
btn_clear.place(x=600,y=280)

btn_delete=Button(win,text='DELETE',font=("Comic Sans MS", 12, "bold"),width=15,command=remove)
btn_delete.place(x=600,y=340)

btn_exit=Button(win,text='EXIT',font=("Comic Sans MS", 12, "bold"),width=15,command=exit)
btn_exit.place(x=600,y=400)

btn_search=Button(win,text='LOGIN',font=("Comic Sans MS", 12, "bold"),width=15,command=search)
btn_search.place(x=600,y=460)

lst_box = Listbox(win,width=80,height=18)
lst_box.place(x=50,y=150)

lst_box.bind("<Button-1>",select)

win.mainloop()
