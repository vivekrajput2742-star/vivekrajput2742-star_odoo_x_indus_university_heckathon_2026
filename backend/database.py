import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vivek@2006",
    database="coreinventory"
)

cursor = db.cursor(dictionary=True)