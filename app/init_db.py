import mysql.connector
import time

trise = 15
intreval = 5

for _ in range(trise):
    try:
        time.sleep(intreval)
        connection = mysql.connector.connect(
            user="root",
            password="root",
            host="db",
            port="3306",
            database="aura_essence",
        )
    except mysql.connector.errors.DatabaseError:
        print("Database Error")
        intreval = intreval + 2
    finally:
        print("DB connected")

cursor = connection.cursor()
cursor.execute("Select * FROM candle")
students = cursor.fetchall()
connection.close()

print(students)
