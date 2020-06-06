#!/usr/bin/python -u
#-*- coding:utf8 -*-
# Developed in Python 3.8.3, 2020-06-06 start of works.

# Insert/format data to SQLite via:
import sqlite3

def createDbWithTable(pathToNewDb, tableName, schemaDefinition):
    """ For the schemaDefinition see sqlite3.cursor.execute parameter's docs """  
    try:
        sqliteConnection = sqlite3.connect(pathToNewDb)
        sqlite_create_table_query = "CREATE TABLE "+tableName+" ("+schemaDefinition+");"

        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
        print("SQLite table created")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")

# def tryCreateDb():
#     createDbWithTable(..)

def tryOutCreatingDb():
    dbName = "SQL_new_PoC.db"
    createDbWithTable(dbName, "ehm_table", '''
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    email text NOT NULL UNIQUE,
                                    joining_date datetime,
                                    salary REAL NOT NULL''')

if __name__ == "__main__":
    tryOutCreatingDb()
    #view the db to check all ok..
                                    