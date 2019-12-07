  
import sqlite3
from player import Player

conn = sqlite3.connect('Server.db')

c = conn.cursor()

c.execute("""CREATE TABLE users (
            first text,
            last text,
            age integer,
            username text,
            password text
            )""")

def login():
    while True:
        username=input("Enter UserName: ")
        password=input("Enter Password: ")
        find_user=("SELECT users WHERE username=? AND password=?")
        c.execute=(find_user,[(username),(password)])
        result=c.fetchall()
        if result:
            print("Welcome"+username)
            break
        else:
            print("user and password not recognized")
            enter_again=input("do you want enter again you login details y\n")
            if enter_again.lower()==n:
                exit(1)




login()
conn.close()
