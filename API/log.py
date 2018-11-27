import os
import sqlite3
import datetime
import csv

DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'log.db')
sqlite3.connect(DATABASE_PATH)


def connect_db():
    return sqlite3.connect(DATABASE_PATH)




def create_tables():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
            CREATE TABLE IF NOT EXISTS logs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(32),

            time VARCHAR(32)

            )''')

    conn.commit()
    conn.close()




def add(names):
    conn = connect_db()
    cur = conn.cursor()
    dt = datetime.datetime.now()

    cur.execute("""
                 INSERT INTO logs (name , time)  VALUES ('{}' , '{}'  )"""
                 .format(names , dt.strftime("%H, %M , %S") )
            )




    conn.commit()
    conn.close()

def selectAll():
    conn = connect_db()
    cur = conn.cursor()
    result = cur.execute("""
                SELECT * FROM logs """
                )
    result = result.fetchall()
    conn.commit()
    return str(result)

def writeAsCsv():
    conn = connect_db()
    cur = conn.cursor()
    result = cur.execute("""
                SELECT * FROM logs """
                )
    with open("log.csv", "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cur.description]) # write headers
        csv_writer.writerows(cur)






create_tables()

#create_tables()
#result  =selectAll()
#add("sai")

#writeAsCsv()


#print(result)
