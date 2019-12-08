import sqlite3
conn = sqlite3.connect('Server.db')
c = conn.cursor()
#c.execute("""CREATE TABLE users (
 #          UserType text,
  #         first text,
   #        last text,
    ##       age integer,
      #     gender text,
       #    id text,
        #   username text,
         #  password text
       
        #)""")


def Auth(result):
    if result=='M':
        ManagerMenu()
    elif result=='P':
        print("Parent_Menu()-SOON")
    else:
        Menu_User()
        
def Registerion():
    number_of_users=int(input("Enter how many Players do you want to register: "))
    for i in range (number_of_users):
        with conn:
            UserType=input("Enter user type for registration, Please Enter:U-User,P-Parent:  ")
            while UserType:
                if UserType.upper()=='P' or UserType.upper()=='U' or UserType.upper()=='M':
                    break
                else:
                    UserType=input("Valid input, Enter user type for registration, Please Enter: U-User,P-Parent:  ")
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
            conn.commit()

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
            Auth(result[0][0])
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
        conn.commit()



def Menu():
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
        else:
           print("\n Not Valid Choice Try again")
def Menu_User():
    ans=True
    while ans:
        print("""
        1.Play
        2.Total play time
        3.Exit/Quit
        """)
        ans=int(input("Enter your choice:"))
        if ans==1:
          Play()
        elif ans==3:
          print("\n Goodbye") 
          ans = None
        else:
           print("\n Not Valid Choice Try again")
    
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
8.exit""")
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
conn.close()
