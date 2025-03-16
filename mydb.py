import mysql.connector

dataBase=mysql.connector.connect(
  host='localhost',
  user='root',
  passwd='root',
)

cursorProject=dataBase.cursor()

cursorProject.execute("CREATE DATABASE dcrm")

print("ALL Done!!")