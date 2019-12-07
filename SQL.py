  
import sqlite3
from player import Player

conn = sqlite3.connect('Server.db')

c = conn.cursor()

#c.execute("""CREATE TABLE Game (
 #           first text,
  #          last text,
   #         age integer
    #        )""")
def insert_player(p):
    with conn:
        c.execute("INSERT INTO Server VALUES (:first, :last, :age)", {'first': p.first, 'last': p.last, 'age': p.age})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM Server WHERE last=:last", {'last': lastname})
    return c.fetchall()


def update_age(p, age):
    with conn:
        c.execute("""UPDATE Server SET age = :age
                    WHERE first = :first AND last = :last""",
                  {'first': p.first, 'last': p.last, 'age': age})


def remove_emp(p):
    with conn:
        c.execute("DELETE from Server WHERE first = :first AND last = :last",
                  {'first': p.first, 'last': p.last})


p1 = Player('ilia', 'elir', 23)
p2 = Player('tal', 'itah', 23)
find = get_emps_by_name('elir')
print(find)
insert_player(p1)
insert_player(p2)
print(c.fetchall())
conn.close()
