import sqlite3
import datetime
import pygame
from random import randrange
from button import button
from _overlapped import NULL

def SecToTime(total_seconds):
        m=total_seconds//60
        s=total_seconds%60
        h=m//60
        m=m%60
        h=h%24
        print("Hours:{0},Minutes:{1},Seconds:{2}".format(h,m,s))
def get_totaltime(id):
    conn = sqlite3.connect('Data.db')
    with conn as db:
        cursor=db.cursor()
    find=("SELECT * FROM Time WHERE id=?")
    cursor.execute(find,[id])
    result=cursor.fetchall()
    total_time=int(result[0][3])
    return total_time

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
           password text
        )""")
    
    c.execute("""CREATE TABLE IF NOT EXISTS Time (
           id text,
           day_time text,
           week_time text,
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

def isUserType(UserType):
    if UserType.upper()=='P' or UserType.upper()=='U' or UserType.upper()=='M':
        return True
    return False


def isGender(gender):
    if gender=='B' or gender=='G' or gender=='b' or gender=='g':
        return True
    return False

def Check_User_Type_From_DB(res):
    type=str(res[0][0])
    id=str(res[0][5])
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
        if UserType=='U':
            id_parent=input("Enter parent ID: ")
            while Proper_ID(id_parent)!=True:
                 id=input("Enter your parent properly [9 digits]: ")
        else:
            id_parent='none'
        username=input("Enter username: ")
        password=input("Enter password: ")
        insert_into_database_user(UserType,first,last,gender,age,id,id_parent,username,password)



def insert_into_database_user(UserType,first,last,gender,age,id,id_parent,username,password):
    conn = sqlite3.connect('Data.db')
    c = conn.cursor()
    with conn:
        c.execute("INSERT INTO users VALUES (:UserType,:first, :last,:age,:gender,:id,:id_parent,:username,:password)", {'UserType':UserType,'first':first, 'last':last,'age':age,'gender':gender,'id':id,'id_parent':id_parent,'username':username,'password':password})
        if UserType.upper()=='U':
            c.execute("INSERT INTO Time VALUES (:id,:day_time,:week_time,:total_time)", {'id':id,'day_time':'0','week_time':'0','total_time':'0'})
            c.execute("INSERT INTO exposure_and_understanding VALUES (:id,:level_happy,:exposure_happy,:level_sad,:exposure_sad,:level_angry,:exposure_angry,:level_fear,:exposure_fear,:level_disappointment,:exposure_disappointment,:level_suprised,:exposure_suprised,:level_tired,:exposure_tired,:level_affection,:exposure_affection,:level_proud ,:exposure_proud,:level_concern,:exposure_concern)", {'id':id,'level_happy':'0','exposure_happy':0,'level_sad':'0','exposure_sad':0,'level_angry':'0','exposure_angry':0,'level_fear':'0','exposure_fear':0,'level_disappointment':'0','exposure_disappointment':0,'level_suprised':'0','exposure_suprised':0,'level_tired':'0','exposure_tired':0,'level_affection':'0','exposure_affection':0 ,'level_proud':'0' ,'exposure_proud':0,'level_concern':'0','exposure_concern':0})
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
        with sqlite3.connect("Data.db") as db:
            cursor=db.cursor()
        find_user=("SELECT * FROM users WHERE username=? AND password=?")
        cursor.execute(find_user,[(username),(password)])
        result=cursor.fetchall()
        
        if result:
            print("Welcome "+username)
            Check_User_Type_From_DB(result)
            return True
        else:
            print("user and password not recognized")
            enter_again=input("do you want enter again you login details [y/n]: ")
            if enter_again.lower()== 'n':
                print("GoodBye")
                return False


def Delete(id):
    conn = sqlite3.connect('Data.db')
    c = conn.cursor()
    with conn:
        c.execute("DELETE  FROM users WHERE id = :id",
                  {'id': id})
        result=c.fetchall()
        if len(result)==0:
            return False
        else:
            conn.commit()
            return True



def Menu():
    print()
    conn = sqlite3.connect('Data.db')
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
def Menu_User(id):
    print()
    Loop=True
    while Loop:
        print()
        print("""
        1.Play
        2.Total play time
        3.Logout
        """)
        ans=int(input("Enter your choice:"))
        if ans==1:
          play(id)
        elif ans==2:
            total=get_totaltime(id)
            SecToTime(total)
        elif ans==3:
          print()
          print("\n Goodbye") 
          Loop = None
          Menu()
          break
        else:
           print()
           print("\n InValid Choice Try again")
    
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
            ManagerMenu()
            break
            
        else:
            print()
            print("Invalid Value, you returned to Manager menu")
                

        
    

def ManagerMenu(id):
    print()
    x=True
    while x:
        print()
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
            print()
            print("Your Profits: {0} shekel til now".format(sum))
            print()
                
        elif x==8:
            print()
            print("GoodBye manager")
            x=None
            Menu()
            
        else:
            print()
            print("Invalid value,please enter again")

def count_players():
    conn = sqlite3.connect('Data.db')
    c = conn.cursor()
    count=0
    c.execute("SELECT COUNT (*) FROM users WHERE UserType='P'")
    rowcount = c.fetchone()[0]
    return rowcount

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
    Loop=True
    while Loop:
        print("""
        1.Time limitetion
        2.Total play time of the son
        3.Notification to sleep
        4.Enter feedback
        5.Logout
        """)
        ans=int(input("Enter your choice:"))
        if ans==1:
          print("Time limitetion()")
        elif ans==2:
          print("how much time()") 
        elif ans==3:
          print("Notification to sleep()")
        elif ans==4:
          print("feedback()")
        elif ans==5:
          print("goodbye")
          Loop = None
          Menu()
          break
          
        else:
           print("\n InValid Choice Try again")
    
    
def play(id):
    def calucate_time():
        startSec=0
        endSec=0
        start=datetime.datetime.now()
        def time(message):
            if message=='start_time':
                nonlocal startSec,start
                start=datetime.datetime.now()
                startSec=start.hour*3600+start.minute*60+start.second
            elif message=='end_time':
                nonlocal endSec
                end=datetime.datetime.now()
                endSec=end.hour*3600+end.minute*60+end.second
                if not(end.day - start.day == 0):
                    return 1
                return 0
            elif message=='Caluction':
                return endSec-startSec
        return time
    def Time_Caluction(t,id):
        flag=t('end_time')
        update_time=t('Caluction')
        conn = sqlite3.connect('Data.db')
        with conn as db:
            cursor=db.cursor()
        find=("SELECT * FROM Time WHERE id=?")
        cursor.execute(find,[id])
        result=cursor.fetchall()
        total_time=str(int(result[0][3])+update_time)
        if flag==0:
            cursor.execute('''UPDATE Time SET day_time = ? WHERE id = ?''', (0,id))
        cursor.execute('''UPDATE Time SET total_time = ? WHERE id = ?''', (total_time, id))
        conn.commit()
       
    def Insert():#Insert details to DB feelings table
        def insert_into_database_feelings(feel,info,question1,Answer1_of_question1,Answer2_of_question1,Answer3_of_question1,CurrectAnswer_of_question1,question2,Answer1_of_question2,Answer2_of_question2,Answer3_of_question2,CurrectAnswer_of_question2,question3,Answer1_of_question3,Answer2_of_question3,Answer3_of_question3,CurrectAnswer_of_question3):
            conn = sqlite3.connect('Data.db')
            c = conn.cursor()
            with conn:
                c.execute("INSERT INTO feelings VALUES (:feel,:info, :question1,:Answer1_of_question1,:Answer2_of_question1,:Answer3_of_question1,:CurrectAnswer_of_question1,:question2,:Answer1_of_question2,:Answer2_of_question2,:Answer3_of_question2,:CurrectAnswer_of_question2,:question3,:Answer1_of_question3,:Answer2_of_question3,:Answer3_of_question3,:CurrectAnswer_of_question3)", {'feel':feel,'info':info, 'question1':question1,'Answer1_of_question1':Answer1_of_question1,'Answer2_of_question1':Answer2_of_question1,'Answer3_of_question1':Answer3_of_question1,'CurrectAnswer_of_question1':CurrectAnswer_of_question1,'question2':question2,'Answer1_of_question2':Answer1_of_question2,'Answer2_of_question2':Answer2_of_question2,'Answer3_of_question2':Answer3_of_question2,'CurrectAnswer_of_question2':CurrectAnswer_of_question2,'question3':question3,'Answer1_of_question3':Answer1_of_question3,'Answer2_of_question3':Answer2_of_question3,'Answer3_of_question3':Answer3_of_question3,'CurrectAnswer_of_question3':CurrectAnswer_of_question3})
                conn.commit()    
    
        insert_into_database_feelings('happy','Hapiness_Complete.png','Happy1_Complete.PNG','Angry','Smile','Cry',2,'Happy2_Complete.PNG','Happy','Sad','Anger',1,'Happy3_Complete.PNG','Anger','Sad','Happy',2)
        insert_into_database_feelings('sad','Sad_info.png','Sad1_Complete.PNG','Sad','fear','Anger',1,'Sad2_Complete.png','Happy','Sad','Anger',2,'Sad3_Complete.png','Anger','Sad','fear',2)
        insert_into_database_feelings('angry','Angry_Complete.png','Angry1_Complete.PNG','Happy','Sad','Angry',3,'Angry2_Complete.png','Anger','Happy','Fear',1,'Angry3_Complete.PNG','Fear','Sad','Anger',3) 
        insert_into_database_feelings('fear','Fear_Complete.png','Fear1_Complete.PNG','Happy','Sad','Fear',3,'Fear2_Complete.PNG','Sad','Fear','Anger',2,'Fear3_Complete.PNG','Fear','Sad','Happy',1)
        insert_into_database_feelings('disappointment','Disappointment_Complete.png','Disappointment1_Complete.png','Angry','Smile','Cry',2,'Disappointment2_Complete.PNG','Happy','Sad','Anger',1,'Disappointment3_Complete.PNG','Anger','Sad','Happy',2)
        insert_into_database_feelings('surprised','Surprised_Complete.png','Surprised1_Complete.PNG','Sad','fear','Anger',1,'Surprised2_Complete.png','Happy','Sad','Anger',2,'Surprised3_Complete.png','Anger','Sad','fear',2)
        insert_into_database_feelings('tired','Tired_Complete.png','Tired1_Complete.PNG','Happy','Sad','Angry',3,'Tired2_Complete.png','Anger','Happy','Fear',1,'Tired3_Complete.PNG','Fear','Sad','Anger',3) 
        insert_into_database_feelings('affection','Affection_Complete.png','Affection1_Complete.PNG','Happy','Sad','Fear',3,'Affection2_Complete.PNG','Sad','Fear','Anger',2,'Affection3_Complete.PNG','Fear','Sad','Happy',1)
        insert_into_database_feelings('proud','Proud_Complete.png','Proud1_Complete.PNG','Happy','Sad','Angry',3,'Proud2_Complete.png','Anger','Happy','Fear',1,'Proud3_Complete.PNG','Fear','Sad','Anger',3) 
        insert_into_database_feelings('concern','Concern_Complete.png','Concern1_Complete.PNG','Happy','Sad','Fear',3,'Concern2_Complete.PNG','Sad','Fear','Anger',2,'Concern3_Complete.PNG','Fear','Sad','Happy',1)
    
    
              
        
        
    def Reset_dictionary():
        for x in level:
            if level[x]==15:
                level[x]=0
    def UpdateCard():#Updating from DB the Cards and buttons
        global x
        x=arr_feelings[indexCard]
        Reset_dictionary()
        with sqlite3.connect("Data.db") as db:
            cursor=db.cursor()
        find_feelings=("SELECT * FROM feelings WHERE feel=?")
        cursor.execute(find_feelings,[(x)])
        result=cursor.fetchall()
        global Card_info,Card_question,Button1,Button2,Button3,questionButton,color,ans
        Card_info=pygame.image.load(result[0][1])
        Card_question=pygame.image.load(result[0][2+level[x]])
        Button1=button((255,255,255),300,430,250,40,result[0][3+level[x]])
        Button2=button((255,255,255),300,530,250,40,result[0][4+level[x]])
        Button3=button((255,255,255),300,630,250,40,result[0][5+level[x]])
        questionButton=button((255,255,255),300,680,250,100,'Question')
        color=randrange(0,255)
        ans=result[0][6+level[x]]
    
    def updateTabel_exposure(id):
        conn = sqlite3.connect('Data.db')
        with conn as db:
            cursor=db.cursor()
        find=("SELECT * FROM exposure_and_understanding WHERE id=?")
        cursor.execute(find,[id])
        result=cursor.fetchall()
        now=result[0][indexCard*2+2]
        now1=result[0][indexCard*2+1]
        if(indexCard==0):
            cursor.execute('''UPDATE exposure_and_understanding SET exposure_happy = ? WHERE id = ?''', (now+1, id))
            conn.commit()
            if not now1 == 'h':
                if level[x]==5:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_happy = ? WHERE id = ?''', ('low', id))
                    conn.commit()
                    
                if level[x]==10:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_happy = ? WHERE id = ?''', ('medium', id))
                    conn.commit()
                    
                if level[x]==15:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_happy = ? WHERE id = ?''', ('high', id))
                    conn.commit()
                    
    
        elif(indexCard==1):
            cursor.execute('''UPDATE exposure_and_understanding SET exposure_sad = ? WHERE id = ?''', (now+1, id))
            conn.commit()
            if not now1 == 'h':
                if level[x]==5:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_sad = ? WHERE id = ?''', ('low', id))
                    conn.commit()
                if level[x]==10:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_sad = ? WHERE id = ?''', ('medium', id))
                    conn.commit()
                if level[x]==15:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_sad = ? WHERE id = ?''', ('high', id))
                    conn.commit()
        elif(indexCard==2):
            cursor.execute('''UPDATE exposure_and_understanding SET exposure_angry = ? WHERE id = ?''', (now+1, id))
            conn.commit()
            if not now1 == 'h':
                if level[x]==5:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_angry = ? WHERE id = ?''', ('low', id))
                    conn.commit()
                if level[x]==10:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_angry = ? WHERE id = ?''', ('medium', id))
                    conn.commit()
                if level[x]==15:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_angry = ? WHERE id = ?''', ('high', id))
                    conn.commit()
        elif(indexCard==3):
            cursor.execute('''UPDATE exposure_and_understanding SET exposure_fear = ? WHERE id = ?''', (now+1, id))
            conn.commit()
            if not now1 == 'h':
                if level[x]==5:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_fear = ? WHERE id = ?''', ('low', id))
                    conn.commit()
                if level[x]==10:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_fear = ? WHERE id = ?''', ('medium', id))
                    conn.commit()
                if level[x]==15:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_fear = ? WHERE id = ?''', ('high', id))
                    conn.commit()
        elif(indexCard==4):
            cursor.execute('''UPDATE exposure_and_understanding SET exposure_disappointment = ? WHERE id = ?''', (now+1, id))
            conn.commit()
            if not now1 == 'h':
                if level[x]==5:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_disappointment = ? WHERE id = ?''', ('low', id))
                    conn.commit()
                if level[x]==10:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_disappointment = ? WHERE id = ?''', ('medium', id))
                    conn.commit()
                if level[x]==15:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_disappointment = ? WHERE id = ?''', ('high', id))
                    conn.commit()
                    
        elif(indexCard==5):
            cursor.execute('''UPDATE exposure_and_understanding SET exposure_suprised = ? WHERE id = ?''', (now+1, id))
            conn.commit()
            if not now1 == 'h':
                if level[x]==5:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_suprised = ? WHERE id = ?''', ('low', id))
                    conn.commit()
                if level[x]==10:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_suprised = ? WHERE id = ?''', ('medium', id))
                    conn.commit()
                if level[x]==15:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_suprised = ? WHERE id = ?''', ('high', id))
                    conn.commit()
        elif(indexCard==6):
            cursor.execute('''UPDATE exposure_and_understanding SET exposure_tired = ? WHERE id = ?''', (now+1, id))
            conn.commit()
            if not now1 == 'h':
                if level[x]==5:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_tired = ? WHERE id = ?''', ('low', id))
                    conn.commit()
                if level[x]==10:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_tired = ? WHERE id = ?''', ('medium', id))
                    conn.commit()
                if level[x]==15:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_tired = ? WHERE id = ?''', ('high', id))
                    conn.commit()
        elif(indexCard==7):
            cursor.execute('''UPDATE exposure_and_understanding SET exposure_8 = ? WHERE id = ?''', (now+1, id))
            conn.commit()
            if not now1 == 'h':
                if level[x]==5:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_affection = ? WHERE id = ?''', ('low', id))
                    conn.commit()
                if level[x]==10:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_affection = ? WHERE id = ?''', ('medium', id))
                    conn.commit()
                if level[x]==15:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_affection = ? WHERE id = ?''', ('high', id))
                    conn.commit()
        elif(indexCard==8):
            cursor.execute('''UPDATE exposure_and_understanding SET exposure_proud = ? WHERE id = ?''', (now+1, id))
            conn.commit()
            if not now1 == 'h':
                if level[x]==5:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_proud = ? WHERE id = ?''', ('low', id))
                    conn.commit()
                if level[x]==10:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_proud = ? WHERE id = ?''', ('medium', id))
                    conn.commit()
                if level[x]==15:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_proud = ? WHERE id = ?''', ('high', id))
                    conn.commit()
        elif(indexCard==9):
            cursor.execute('''UPDATE exposure_and_understanding SET exposure_concern = ? WHERE id = ?''', (now+1, id))
            conn.commit()
            if not now1 == 'h':
                if level[x]==5:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_concern = ? WHERE id = ?''', ('low', id))
                    conn.commit()
                if level[x]==10:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_concern = ? WHERE id = ?''', ('medium', id))
                    conn.commit()
                if level[x]==15:
                    cursor.execute('''UPDATE exposure_and_understanding SET level_concern = ? WHERE id = ?''', ('high', id))
                    conn.commit()
        
        
    
    
    def Random():#return random number to indexCard 
        while True:
            rand=randrange(0,len(arr_feelings))
            if(rand!=indexCard):
                return rand        
            
    def RedWindow():#Building the buttons
        if(indexTypeCard==0):
            screen.fill((color,150,100))
            questionButton.draw(screen,(0,0,0))
        else:
            screen.fill((color,131,180))
            Button1.draw(screen,(0,0,0))
            Button2.draw(screen,(0,0,0))
            Button3.draw(screen,(0,0,0))
    
    
    def feel_Card():#Building the cards
        if(indexTypeCard==0):
            screen.blit(Card_info,(200,10))
        else:
            screen.blit(Card_question,(140,10))
        
    
    pygame.init()
    pygame.display.set_caption("Moment of Emotion") 
    screen=pygame.display.set_mode((800,800)) 
    arr_feelings=['happy','sad','angry','fear','disappointment','surprised','tired','affection','proud','concern']
    level={'happy':0,'sad':0,'angry':0,'fear':0,'disappointment':0,'surprised':0,'tired':0,'affection':0,'proud':0,'concern':0}
    indexCard=0
    indexTypeCard=0
    running=True
    Mistake1=True
    Mistake2=True
    Mistake3=True
    t=calucate_time()
    UpdateCard()
    k=True
    once_only=True
    while running: #Loop keep the window on
        if once_only==True:
            t('start_time')
            once_only=False
        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            if event.type==pygame.MOUSEBUTTONDOWN:#Pressing on button
                if questionButton.isOver(pos) :
                    if(indexTypeCard==0):
                        indexTypeCard+=1 
                elif Button1.isOver(pos) and indexTypeCard==1:
                        if not ans==1:
                            Mistake1=False
                        else:
                            Mistake1=True
                            Mistake2=True
                            Mistake3=True 
                            level[x]+=5
                            updateTabel_exposure(id)
                            indexCard=Random()
                            indexTypeCard=0
                            UpdateCard()
                elif Button2.isOver(pos) and indexTypeCard==1:
                        if not ans==2:
                            Mistake2=False
                        else:
                            Mistake1=True
                            Mistake2=True
                            Mistake3=True 
                            level[x]+=5
                            updateTabel_exposure(id)      
                            indexCard=Random()
                            indexTypeCard=0
                            UpdateCard()
                elif Button3.isOver(pos) and indexTypeCard==1:
                        if not ans==3:
                            Mistake3=False
                        else:
                            Mistake1=True
                            Mistake2=True
                            Mistake3=True 
                            level[x]+=5
                            updateTabel_exposure(id)      
                            indexCard=Random()
                            indexTypeCard=0
                            UpdateCard()
                        
            if event.type==pygame.MOUSEMOTION: #button change color
                
                if questionButton.isOver(pos) and indexTypeCard==0:
                    questionButton.color=(255,0,0)
                else:
                    questionButton.color=(0,255,0)
                if Mistake1:
                    
                    if Button1.isOver(pos):
                        Button1.color=(255,0,0)
                    else:
                        Button1.color=(0,255,0)
                else:
                    Button1.color=(255,0,0)
                if Mistake2:
                    if Button2.isOver(pos):
                        Button2.color=(255,0,0)
                    else:
                        Button2.color=(0,255,0)
                else:
                    Button2.color=(255,0,0)
                if Mistake3:
                    if Button3.isOver(pos):
                        Button3.color=(255,0,0)
                    else:
                        Button3.color=(0,255,0)
                else:
                    Button3.color=(255,0,0)
                
        if event.type==pygame.QUIT:
            Time_Caluction(t,id)
            running=False
            exit(1)
        
        RedWindow()
        feel_Card()
        pygame.display.flip()
Menu()
