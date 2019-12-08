
import sqlite3

conn = sqlite3.connect('Server.db')
c = conn.cursor()
count_num_of_players=0

#c.execute("""CREATE TABLE users (
 #          UserType text,
  #         first text,
   #        last text,
    #       age integer,
     #      gender text,
      #     id text,
       #    username text,
        #   password text
       
        #)""")

def Registerion():
    number_of_users=int(input("Enter how many Players do you want to register: "))
    for i in range (number_of_users):
        with conn:
            UserType=input("Enter user type for registration, Please Enter:M-Managment,U-User,P-Parent:  ")
            while UserType:
                if UserType.upper()=='P' or UserType.upper()=='U' or UserType.upper()=='M':
                    break
                else:
                    UserType=input("Valid input, Enter user type for registration, Please Enter:M-Managment,U-User,P-Parent:  ")
            if UserType.upper()=='P':
                global count_num_of_players
                count_num_of_players+=1
            first=input("Enter first name: ")
            last=input("Enter last name: ")
            gender=input("Enter your gender [Boy or Girl]: ")
            while gender:
                if gender.upper()=='B' or gender.upper()=='G':
                    break
                else:
                    gender=input("Valid input, Enter your gender [Boy or Girl]: ")
            age=input("Enter your age: ")
            id=input("Enter your personal ID: ")
            username=input("Enter username: ")
            password=input("Enter password: ")
            c.execute("INSERT INTO users VALUES (:UserType,:first, :last,:age,:gender,:id,:username,:password)", {'UserType':UserType,'first':first, 'last':last,'age':age,'gender':gender,'id':id,'username':username,'password':password})


def login():
    while True:
        username=input("Enter UserName: ")
        password=input("Enter Password: ")
        with sqlite3.connect("Server.db") as db:
            cursor=db.cursor()
        find_user=("SELECT * FROM users WHERE username=? AND password=?")
        cursor.execute(find_user,[(username),(password)])
        result=cursor.fetchall()
        if result:
            print("Welcome "+username)
            break
        else:
            print("user and password not recognized")
            enter_again=input("do you want enter again you login details [y/n]: ")
            if enter_again.lower()== 'n':
                print("GoodBye")
                break

def Delete():
    id=input("Enter ID of the player that you want to remove: ")
    with conn:
        c.execute("DELETE  FROM users WHERE id = :id",
                  {'id': id})

Registerion()
conn.close()
