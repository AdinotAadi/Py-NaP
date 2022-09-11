import mysql.connector


def dbconnect():
    connector = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="tiger",
        database="test")
    cur = connector.cursor()
