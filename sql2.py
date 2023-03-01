import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1:3306",
    user="Local Instance",
    password="268220bk.K"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
