import mysql.connector


def dbConnect():
    connector = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="tiger",
        database="test")
    cur = connector.cursor()


def main():
    dbConnect()


if __name__ == "__main__":  
    main()
