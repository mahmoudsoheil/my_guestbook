import mysql.connector
from mysql.connector import Error

def connect():
    #connect to database
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='my_guestbook',
                                             user='root',
                                             password='')
        if connection.is_connected():
            print("You're connected to database")
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        cursor = connection.cursor()
        cursor.execute("create table if not exists users (" + 
                                                          "username varchar(20),"+ 
                                                          "password varchar(20));")
        cursor.close()
        return connection

def check_exist(values):
    #check if user already exists
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("select * from users where username = \"" + values[0] +"\"" +
                                         "and password = \"" + values[1] +"\";")
    if (cursor.fetchone() is None):
        return connection, cursor, False

def create(values):
    connection, cursor, exist = check_exist(values)
    if (not exist):
        cursor.execute("insert into users values ( \"" + values[0] +"\" , " +
                                                  "\"" + values[1] +"\");")
        print("created")
    cursor.close()
    connection.close()
    
def login(values):
    connection, cursor, exist = check_exist(values)
    if (exist):
        print("login successfully")
    cursor.close()
    connection.close()