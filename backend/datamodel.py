import datetime
from distutils.log import error
from fileinput import filename
import sqlite3
import uuid


from matplotlib.pyplot import connect

#def create_db():
# try:
#    connection = sqlite3.connect('./backend/db/database.db')
#    cursor = connection.cursor()
#    cursor.execute(''' CREATE TABLE custom_voice (ID INTEGER PRIMARY KEY NOT NULL,CREATED_ON TEXT NOT NULL, LAST_MODIFIED_ON TEXT NOT NULL, TEXT_DATA TEXT NOT NULL, LANGUAGE TEXT NOT NULL, FILE_NAME TEXT NOT NULL, BASE_LOCATION TEXT NOT NULL);''')
#    cursor.close()

# except sqlite3.Error as error:
#    print(error)

# finally:
#    if connection:
#        connection.close()
#        print("Connection closed")

def insert_data(text, lang, filename, base_location):
    try:
        insert_query = """INSERT INTO custom_voice (CREATED_ON, LAST_MODIFIED_ON, TEXT_DATA, LANGUAGE, FILE_NAME, BASE_LOCATION) values(?,?,?,?,?,?)"""
        current_date = datetime.datetime.now()
        connection = sqlite3.connect('./backend/db/database.db')
        cursor = connection.cursor()
        cursor.execute(insert_query,(current_date, current_date, text, lang, filename, base_location))
        cursor.close()
        connection.commit()
        print("Data inserted")
    except sqlite3.Error as error:
        print("my error: " + str(error))
    finally:
        if connection:
            connection.close()
            print("Connection closed")

def delete_data(text, lang):
    try:
        select_query = """SELECT * FROM custom_voice WHERE TEXT_DATA=? AND LANGUAGE=?"""
        delete_query = """DELETE FROM custom_voice WHERE TEXT_DATA=? AND LANGUAGE=?"""
        connection = sqlite3.connect('./backend/db/database.db')
        flag = False
        filename, base_location = ""
        cursor = connection.cursor()
        cursor.execute(select_query,(text, lang))
        temp = cursor.fetchone()
        if temp is None:
            flag = False
            print("No such data found")
        else:
            cursor.execute(delete_query,(text, lang)) 
            flag = True
            filename = temp[5]
            base_location = temp[6]
            print("Data removed")
        cursor.close()
        connection.commit()
    except sqlite3.Error as error:
        print("my error: " + str(error))
    finally:
        if connection:
            connection.close()
            print("Connection closed")
        return [flag, filename, base_location]



def update_data(text, lang, filename, base_location):
    try:
        select_query = """SELECT * FROM custom_voice WHERE TEXT_DATA=? AND LANGUAGE=?"""
        update_query = """UPDATE custom_voice SET LAST_MODIFIED_ON=? , FILE_NAME= ? , BASE_LOCATION = ? WHERE TEXT_DATA=? AND LANGUAGE=?"""
        connection = sqlite3.connect('./backend/db/database.db')
        current_date = datetime.datetime.now()
        flag = False
        cursor = connection.cursor()
        cursor.execute(select_query,(text, lang))
        temp = cursor.fetchone()
        if temp is None:
            flag = False
            print("No such data found to update")
        else:
            flag = True
            cursor.execute(update_query,(current_date, filename, base_location, text, lang)) 
            print("Data Updated")
        cursor.close()
        connection.commit()
    except sqlite3.Error as error:
        print("my error: " + str(error))
    finally:
        if connection:
            connection.close()
            print("Connection closed")
        return flag