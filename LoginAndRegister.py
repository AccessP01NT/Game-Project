from tkinter import *
import sqlite3


def register_user():
    
    username_info=username.get()
    password_info=password.get()
    first_info=first.get()
    last_info=last.get()
    id_info=id.get()
    age_info=age.get()
    gender_info=gender.get()
    type_info=type.get()
    with conn:
        c.execute("INSERT INTO users VALUES (:first,:last,:age,:gender,:id,:type,:username,:password)", {'first':first_info,'last':last_info,'id':id_info,'age':age_info,'gender':gender_info,'type':type_info,'username':username_info,'password':password_info})
    username_entry.delete(0,END)
    password_entry.delete(0,END)

    Label(screen1,text="Registration Success",fg="green" ,font=("calibri",11)).pack()

def register():
    global screen1
    screen1=Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x450")
    global username
    global username_entry
    global password
    global password_entry
    global first
    global first_entry
    global last
    global last_entry
    global id
    global id_entry
    global age
    global age_entry
    global gender
    global gender_entry
    global type
    global type_entry
    first=StringVar()
    last=StringVar()
    id=StringVar()
    age=StringVar()
    gender=StringVar()
    type=StringVar()
    username=StringVar()
    password=StringVar()
    
    Label(screen1,text="Please enter details below ").pack()
    Label(screen1,text="").pack()

    Label(screen1,text="First name * ").pack()
    first_entry=Entry(screen1,textvariable=first)
    first_entry.pack()
    Label(screen1,text="Last name * ").pack()
    last_entry=Entry(screen1,textvariable=last)
    last_entry.pack()
    Label(screen1,text="ID * ").pack()
    id_entry=Entry(screen1,textvariable=id)
    id_entry.pack()
    Label(screen1,text="Age * ").pack()
    age_entry=Entry(screen1,textvariable=age)
    age_entry.pack()
    Label(screen1,text="Gender(M\F) * ").pack()
    gender_entry=Entry(screen1,textvariable=gender)
    gender_entry.pack()
    Label(screen1,text="Type * ").pack()
    type_entry=Entry(screen1,textvariable=type)
    type_entry.pack()

    Label(screen1,text="Username * ").pack()
    username_entry=Entry(screen1,textvariable=username)
    username_entry.pack()
    Label(screen1,text="Password * ").pack()
    password_entry=Entry(screen1,textvariable=password)
    password_entry.pack()
    Label(screen1,text="").pack()
    Button(screen1,text="Register",width=10,height=1,command=register_user).pack()


def login():
    print("Login session started")

def main_screen():
    global screen
    screen=Tk()
    screen.geometry("300x250")
    screen.title("Noted 1.0") 
    Label(text="Moment of emotion",bg="grey",width="300",height="2",font=("Clibri",13)).pack()
    Label(text="").pack()
    Button(text="Login",height="2",width="30",command=login).pack()
    Label(text="").pack()
    Button(text="Register",height="2",width="30",command=register).pack()
       
    screen.mainloop()
    


conn = sqlite3.connect('Server.db')
c = conn.cursor()
'''
c.execute("""CREATE TABLE users (
           first text,
           last text,
           id text,
           age integer,
           gender text,
           type text,
           username text,
           password text
        )""")
'''
main_screen()
