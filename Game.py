import datetime
import pygame
import sqlite3
from random import randrange
from button import button
from time import sleep

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
        ans=(input("Enter your choice:"))
        if ans=='1':
          play(id)
        elif ans=='2':
           time_user(id) 
        elif ans=='3':
          print()
          print("\n Goodbye") 
          Loop = None
          Menu()
          break
        else:
           print()
           print("\n InValid Choice Try again")
           
def ManagerMenu(id):
    print()
    x=True
    while x:
        print()
        print("Welcome to Manager menu")
        print("""1.total time of users
2.Add/Remove users
3.Amount of Boys\Girl that playing the game
4.Profits from the game til now
5.Update Code
6.Total amount of players in the game
7.Get total reports
8.Logout""")
        x=(("Enter your choice:"))
        if x=='1':
            total_time_of_users()
                
        elif x=='2':
            Manager_Add_Remove()
        elif x=='3':
            print()
            check_boys_girls()
            print()
        elif x=='4':
            sum=(50.99)*count_players()
            print()
            print("Your Profits: {0} shekel til now".format(sum))
            print()
        elif x=='5':
            exit(1)
        elif x=='6':
            print("\nAmount of players in the game:",count_players())
        elif x=='7':
            get_reports(id)
        elif x=='8':
            print()
            print("GoodBye manager")
            x=None
            Menu()
            
        else:
            print()
            print("Invalid value,please enter again")
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
                
                