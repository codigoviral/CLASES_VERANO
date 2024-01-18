import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    port= 3306,
    user="root",
    password="",
    database="bdtest1"
)

mycursor = mydb.cursor()
sql = "INSERT INTO SEGMENTO (ID, NOMBRE) VALUES (%s, %s)"
val = (2, 'TOP 2')
mycursor.execute(sql, val)
mydb.commit()
mycursor.close()
mydb.close()