
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