import datetime
import pygame
import sqlite3
from random import randrange
from button import button

def Create_Table():
    conn = sqlite3.connect('Data.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
           UserType text,
           first text,
           last text,
           age integer,
           gender text,
           id text,
           id_parent text, 
           username text,
           password text,
           time_limit text
        )""")

    c.execute("""CREATE TABLE IF NOT EXISTS Time (
           id text,
           total_time text
        )""")

    c.execute("""CREATE TABLE IF NOT EXISTS feelings (
       feel text,
       info text,
       question1 text,
       Answer1_of_question1 text,
       Answer2_of_question1 text,
       Answer3_of_question1 text,
       CurrectAnswer_of_question1 integar,
       question2 text,
       Answer1_of_question2 text,
       Answer2_of_question2 text,
       Answer3_of_question2 text,
       CurrectAnswer_of_question2 integar,
       question3 text,
       Answer1_of_question3 text,
       Answer2_of_question3 text,
       Answer3_of_question3 text,
       CurrectAnswer_of_question3 integar
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS exposure_and_understanding (
       id text,
       level_happy text,
       exposure_happy integar,
       level_sad text,
       exposure_sad integar,
       level_angry text,
       exposure_angry integar,
       level_fear text,
       exposure_fear integar,
       level_disappointment text,
       exposure_disappointment integar,
       level_suprised text,
       exposure_suprised integar,
       level_tired text,
       exposure_tired integar,
       level_affection text,
       exposure_affection integar,
       level_proud text,
       exposure_proud integar,
       level_concern text,
       exposure_concern integar
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS reports (
       id text,
       review text,
       first text,
       last text,
       date text
    )""")
def Menu():
    print()
    conn = sqlite3.connect('Data.db')
    c = conn.cursor()
    Create_Table()
    print("Welcome to Moment Of Emotion Game")
    ans = True
    while ans:
        print("""
        1.Login
        2.Register
        3.Exit/Quit
        """)
        ans = (input("Enter your choice:"))
        if ans == '1':
            login()
            ans = None
        elif ans == '2':
            Registerion()
        elif ans == '3':
            print("\n Goodbye")
            ans = None
            conn.close()
        else:
            print("\n Not Valid Choice Try again")

def isUserType(UserType):
    if UserType.upper()=='P' or UserType.upper()=='U' or UserType.upper()=='M':
        return True
    return False

def isGender(gender):
    if gender=='B' or gender=='G' or gender=='b' or gender=='g':
        return True
    return False

def Proper_ID(id):
    if len(id)==9:
        return True
    return False

def Proper_First_Or_Last_Name(str):
    if str.isalpha():
        return True
    return False

def Proper_Age(age):
    if age>0 and age<120:
        return True
    return False

def Check_User_Type_From_DB(type,id):
    if type=='M' or type=='m':
        ManagerMenu(id)
        return True
    elif type=='P' or type=='p':
       menu_parent(id)
       return True
    elif type=='U' or type=='u':
        Menu_User(id)
        return True
    else:
        return False


def Registerion():
        UserType=input("Enter user type for registration, Please Enter:U-User,P-Parent:  ")
        while isUserType(UserType)!=True:
                UserType=input("Invalid input, Enter user type for registration, Please Enter: U-User,P-Parent:  ")
        first=input("Enter first name: ")
        while Proper_First_Or_Last_Name(first)!=True:
            first=input("Invalid input,Enter first name only letters: ")
        last=input("Enter last name: ")
        while Proper_First_Or_Last_Name(last)!=True:
            last=input("Invalid input,Enter last name only letters: ")
        gender=input("Enter your gender [Boy or Girl]: ")
        while isGender(gender)!=True:
                gender=input("Invalid input, Enter your gender [Boy or Girl]: ")
        age=int(input("Enter your age: "))
        while Proper_Age(age)!=True:
                age=int(input("Invalid Enter your age: "))
        id=input("Enter your personal ID: ")
        while Proper_ID(id)!=True:
             id=input("Enter your personal ID properly [9 digits]: ")
        if UserType.upper()=='U':
            id_parent=input("Enter parent ID: ")
            while Proper_ID(id_parent)!=True:
                 id=input("Enter your parent properly [9 digits]: ")
        else:
            id_parent='none'
        username=input("Enter username: ")
        password=input("Enter password: ")
        insert_into_database_user(UserType.upper(),first,last,gender.upper(),age,id,id_parent,username,password)      
        
def login():
    while True:
        username=input("Enter UserName: ")
        password=input("Enter Password: ")
        with sqlite3.connect("Data.db") as db:
            cursor=db.cursor()
        find_user=("SELECT * FROM users WHERE username=? AND password=?")
        cursor.execute(find_user,[(username),(password)])
        result=cursor.fetchall()
        
        if result:
            print("Welcome "+username)
            type=result[0][0]
            id=result[0][5]
            Check_User_Type_From_DB(type,id)
            return True
        else:
            print("user and password not recognized")
            enter_again=input("do you want enter again you login details [y/n]: ")
            if enter_again.lower()== 'n':
                print("GoodBye")
                return False  
            
def insert_into_database_user(UserType,first,last,gender,age,id,id_parent,username,password):
    conn = sqlite3.connect('Data.db')
    c = conn.cursor()
    with conn:
        c.execute("INSERT INTO users VALUES (:UserType,:first, :last,:age,:gender,:id,:id_parent,:username,:password,:time_limit)", {'UserType':UserType,'first':first, 'last':last,'age':age,'gender':gender,'id':id,'id_parent':id_parent,'username':username,'password':password,'time_limit':'23:59'})
        if UserType.upper()=='U':
            c.execute("INSERT INTO Time VALUES (:id,:total_time)", {'id':id,'total_time':'0'})
            c.execute("INSERT INTO exposure_and_understanding VALUES (:id,:level_happy,:exposure_happy,:level_sad,:exposure_sad,:level_angry,:exposure_angry,:level_fear,:exposure_fear,:level_disappointment,:exposure_disappointment,:level_suprised,:exposure_suprised,:level_tired,:exposure_tired,:level_affection,:exposure_affection,:level_proud ,:exposure_proud,:level_concern,:exposure_concern)", {'id':id,'level_happy':'0','exposure_happy':0,'level_sad':'0','exposure_sad':0,'level_angry':'0','exposure_angry':0,'level_fear':'0','exposure_fear':0,'level_disappointment':'0','exposure_disappointment':0,'level_suprised':'0','exposure_suprised':0,'level_tired':'0','exposure_tired':0,'level_affection':'0','exposure_affection':0 ,'level_proud':'0' ,'exposure_proud':0,'level_concern':'0','exposure_concern':0})

        else:
            c.execute("INSERT INTO reports VALUES (:id,:review,:first,:last,:date)", {'id':id,'review':'None','first':first,'last':last,'date':'00:00:0000'})
        conn.commit()
    

def Delete(id):
    conn = sqlite3.connect('Data.db')
    c = conn.cursor()
    with conn:
        c.execute("DELETE  FROM users WHERE id = :id",
                  {'id': id})
        result=c.fetchall()
        c.execute("DELETE  FROM Time WHERE id = :id",
                  {'id': id})
        result=c.fetchall()
        c.execute("DELETE  FROM exposure_and_understanding WHERE id = :id",
                  {'id': id})
        result=c.fetchall()
        if len(result)==0:
            return False
        else:
            conn.commit()
            return True
        
def time_user(id):
    total=get_totaltime(id)
    SecToTime(total)
    
def total_time_of_users():
    sum=0
    conn = sqlite3.connect('Data.db')    
    cursor = conn.cursor()    
    data = cursor.execute('''SELECT * From Time''')
    data = data.fetchall()
    for x in data:
        sum+=int(x[1])
    print("\ntotal time of all users: {0}".format(sum))
    return

def  totaltimeson(id_parent):
     id=input("Enter you child id")
     while not Proper_ID(id):
         id=input("Incorrect id,enter you child id")
     
     if not is_parent_of_user(id_parent, id):
         print("Vaild ID")
         return 
     total=get_totaltime(id)
     SecToTime(total) 
     return
 
def Manager_Add_Remove():
   print()
   x=True
   while x:
       print("""1.Add player
2.Remove player
3.return to menu""")
       x=int(input("Enter your choice:"))
       if x==1:
           print()
           Registerion()
           break
           
       elif x==2:
           print()
           id=input("Enter ID of the player that you want to remove: ")
           Delete(id)
           break
           
      
       elif x==3:
           print()
           #ManagerMenu()
           break
           
       else:
           print()
           print("Invalid Value, you returned to Manager menu")
           
def is_parent_of_user(id_parent,id):
    with sqlite3.connect("Data.db") as db:
            cursor=db.cursor()
    find_parent=("SELECT * FROM users WHERE id=? AND id_parent=?")
    cursor.execute(find_parent,[(id),(id_parent)])
    result=cursor.fetchall()
    if result:
        return True
    return False


def menu_parent(id_parent):
    Loop = True
    while Loop:
        print("""
        1.Time limitetion
        2.Total play time of the son
        3.Enter feedback
        4.level of your son
        5.exposure to feelings of your son
        6.Logout
        """)
        ans = (input("Enter your choice:"))
        if ans == '1':
            Limit_Your_Kid(id_parent)
        elif ans == '2':
            totaltimeson(id_parent)
        elif ans == '3':
            review(id_parent)
        elif ans == '4':
            level_feelings(id_parent)
        elif ans == '5':
            exposure_to_feelings(id_parent)
        elif ans == '6':
            print("goodbye")
            Loop = None
            Menu()
            break

        else:
            print("\n InValid Choice Try again")
            