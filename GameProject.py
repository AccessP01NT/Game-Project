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
