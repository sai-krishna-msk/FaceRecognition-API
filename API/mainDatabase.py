import os
import sqlite3
import datetime

DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'users.db')
sqlite3.connect(DATABASE_PATH)



def connect_db():
    return sqlite3.connect(DATABASE_PATH)




def create_tables():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(32),
            intruder INTEGER,
            timelimit INTEGER,
            initialHour INTEGER,
            initialMinute INTEGER,
            finalHOUR INTEGER,
            finalMinute INTEGER,
            email VARCHAR(32)
            )''')

    conn.commit()
    conn.close()






def selectAll():
    conn = connect_db()
    cur = conn.cursor()
    result = cur.execute("""
                SELECT * FROM users """
                )
    result = result.fetchall()
    conn.commit()
    return result


def gettingSpesefics(name):
    conn = connect_db()
    cur = conn.cursor()
    result = cur.execute("""
                         SELECT * FROM users WHERE name='{}'   """
                         .format(name))
    result = result.fetchall()
    conn.commit()
    return result


def makingIntruder(name):
    conn = connect_db()
    curr = conn.cursor()
    curr.execute("""
                 UPDATE users SET intruder=1, timelimit =0 ,initialHour = 0 , initialMinute = 0 , finalHOUR = 0, finalMinute = 0 WHERE name ='{}' """
                 .format(name)
            )
    conn.commit()



def settingTimeLimit(initialHour, initialMinute , finalHOUR, finalMinute, name):
    conn = connect_db()
    curr = conn.cursor()
    curr.execute("""
                 UPDATE users SET intruder=1, timelimit =1,initialHour = '{}' , initialMinute = '{}' , finalHOUR = '{}', finalMinute = '{}' WHERE name ='{}' """
                 .format(initialHour ,initialMinute ,finalHOUR, finalMinute, name)
            )
    conn.commit()

def makingPersonValid(name):
    conn = connect_db()
    curr = conn.cursor()
    curr.execute("""
                 UPDATE users SET intruder=0, timelimit =0 ,initialHour = 0 , initialMinute = 0 , finalHOUR = 0, finalMinute = 0 WHERE name ='{}' """
                 .format(name)
            )
    conn.commit()



def checkingIntruder(lists):
    lists=lists[0]

    if(lists[2]==0):

        return True


    if(lists[3]==0):

        return False


    else:


        h =datetime.datetime.now().hour
        m = datetime.datetime.now().minute
        if(datetime.time(lists[4] , lists[5])<=datetime.time(h , m) <= datetime.time(lists[6] , lists[7])):
            return True
        else:
            return False

def addPerson(name):
    boo = 0
    id =0
    try:
        conn = connect_db()
        cur = conn.cursor()
        result = cur.execute("""
                    SELECT MAX(id) FROM users """
                    )
        maxId = result.fetchall()
        conn.commit()
        id = maxId[0][0]+1
    except:
        id =0

    conn = connect_db()
    cur = conn.cursor()


    val = [
        (id , name, 0, 0, 0, 0, 0, 0,"no email id provided !"),

    ]

    cur.executemany("""
                    INSERT INTO users ('id' , 'name' , 'intruder' , 'timelimit',initialHour, initialMinute, finalHOUR, finalMinute, email )
                    VALUES (?, ? , ? , ?, ?, ?  ,?, ?, ?)""", val)

    conn.commit()







    return "Sucess"

def deletePerson(name):
    conn = connect_db()
    curr = conn.cursor()
    curr.execute("""
                 DELETE FROM users WHERE name='{}' """.format(name)
                 .format(name)
            )
    conn.commit()
    return "Sucess "






create_tables()


#connect_db()
#create_tables()
#initialize()
#result = selectAll()
#print(result)
#print(result[0][1]) # since we get the data in the form of list of tuples , first we select the fitst element in the list and then the second elemnt of the first tuple
##print(result) # getting the value of
#makingIntruder("sai")
#settingTimeLimit(17, 00, 18, 30 , "sai")
#makingPersonValid("sai")
#result = selectAll()
#print(result)
#result = checkingIntruder(gettingSpesefics(0)) # checking if the person identifed is intruder if yes return flase
#print(result)
#list = ["sai" , "Yes", "gmail.com"]
#results = addPerson(list)
#print(results)
#result = selectAll()
#print(result)
#results = deletePerson("k")
#print(results)
