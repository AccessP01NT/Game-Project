import sqlite3

def Create_Table():
    conn = sqlite3.connect('Server.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
           UserType text,
           first text,
           last text,
           age integer,
           gender text,
           id text,
           username text,
           password text
       
        )""")

def isUserType(UserType):
    if UserType.upper()=='P' or UserType.upper()=='U' or UserType.upper()=='M':
        return True
    return False


def isGender(gender):
    if gender.upper()=='B' or gender.upper()=='G':
        return True
    return False

def Check_User_Type_From_DB(result):
    
    if result=='M':
        ManagerMenu()
        return True
    elif result=='P':
        return True
        print("Parent_Menu()-SOON")
        return True
    elif result=='U':
        Menu_User()
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
        username=input("Enter username: ")
        password=input("Enter password: ")
        insert_into_database(UserType,first,last,gender,age,id,username,password)

def insert_into_database(UserType,first,last,gender,age,id,username,password):
    conn = sqlite3.connect('Server.db')
    c = conn.cursor()
    with conn:
        c.execute("INSERT INTO users VALUES (:UserType,:first, :last,:age,:gender,:id,:username,:password)", {'UserType':UserType,'first':first, 'last':last,'age':age,'gender':gender,'id':id,'username':username,'password':password})
        conn.commit()

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
            Check_User_Type_From_DB(str(result[0][0]))
            return True
        else:
            print("user and password not recognized")
            enter_again=input("do you want enter again you login details [y/n]: ")
            if enter_again.lower()== 'n':
                print("GoodBye")
                return False


def Delete():
    conn = sqlite3.connect('Server.db')
    c = conn.cursor()
    id=input("Enter ID of the player that you want to remove: ")
    with conn:
        c.execute("DELETE  FROM users WHERE id = :id",
                  {'id': id})
        conn.commit()



def Menu():
    conn = sqlite3.connect('Server.db')
    c = conn.cursor()
    Create_Table()
    print("Welcome to Moment Of Emotion Game")
    ans=True
    while ans:
        print("""
        1.Login
        2.Register
        3.Exit/Quit
        """)
        ans=int(input("Enter your choice:"))
        if ans==1:
          login()
          ans=None
        elif ans==2:
          Registerion()
        elif ans==3:
          print("\n Goodbye") 
          ans = None
          conn.close()
        else:
           print("\n Not Valid Choice Try again")
def Menu_User():
    Loop=True
    while Loop:
        print("""
        1.Play
        2.Total play time
        3.Logout
        """)
        ans=int(input("Enter your choice:"))
        if ans==1:
          print("Play()")
        elif ans==3:
          print("\n Goodbye") 
          Loop = None
          Menu()
          break
        else:
           print("\n InValid Choice Try again")
    
def Manager_Add_Remove():
    x=True
    while x:
        print("""1.Add player
2.Remove player
3.return to menu""")
        x=int(input("Enter your choice:"))
        if x==1 or x==2:
            if x==1:
                Registerion()
                break
                
            elif x==2:
                Delete()
                break
                
           
            elif x==3:
                ManagerMenu()
                break
                
            else:
                print("Invalid Value, you returned to Manager menu")
                ManagerMenu()
                


def ManagerMenu():
    x=True
    while True:
        print("Welcome to Manager menu")
        print("""1.Feedback from parent
2.Add/Remove users
3.Total time of the players playing the game
4.Amount of Boys\Girl that playing the game
5.Profits from the game til now
6.Update Code
7.Total amount of players in the game
8.Logout""")
        x=int(input("Enter your choice:"))
        if x==1:
            print("FeedBack()-SOON")
                
        elif x==2:
            Manager_Add_Remove()
        elif x==5:
            sum=(50.99)*count_players()
            print("Your Profits: {0} shekel til now".format(sum))
                
        elif x==8:
            print()
            print("GoodBye manager")
            Menu()
            break
        else:
            print()
            print("Invalid value,please enter again")

def count_players():
    count=0
    c.execute("SELECT COUNT (*) FROM users WHERE UserType='P'")
    rowcount = c.fetchone()[0]
    return rowcount
Menu()


