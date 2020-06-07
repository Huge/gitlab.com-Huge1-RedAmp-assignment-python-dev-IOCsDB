#!/usr/bin/python -u
#-*- coding:utf8 -*-
# Developed in Python 3.8.3, 2020-06-06 start of works.

# Insert/format data to SQLite via:
import sqlite3

def createDbWithTable(pathToNewDb, tableName, schemaDefinition):
    """ For the schemaDefinition see sqlite3.cursor.execute parameter's docs """  
    try:
        sqliteConnection = sqlite3.connect(pathToNewDb)
        queryToCreateTheTable = "CREATE TABLE "+tableName+" ("+schemaDefinition+");"
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")#including the func name 'd make it more worthy
        cursor.execute(queryToCreateTheTable)
        sqliteConnection.commit()
        # print("SQLite table created")
        cursor.close()

    except sqlite3.Error as error:
        import sys
        print("Error while creating a sqlite table,", error, file=sys.stderr)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            # print("sqlite connection is closed")

dbName = "SQL_PoC.db"
def tryOutCreatingDb():
    createDbWithTable(dbName, "IPsTable", '''
                                    id INTEGER PRIMARY KEY,
                                    IP TEXT NOT NULL UNIQUE,
                                    source TEXT NOT NULL,
                                    obtainedFromSourceDate datetime''')#, @Todo: This and the source  IN FOREIGN KEY NOT NULL''')

def insertToDbTable(pathToDb, tableName, recordList):
    """ For the schemaDefinition see sqlite3.cursor.execute parameter's docs """  
    #<sample/insert>
    try:
        sqliteConnection = sqlite3.connect(pathToDb)
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")
        queryTemplateToInsert = "INSERT INTO "+tableName+"""
                          (id, IP, source, obtainedFromSourceDate) 
                          VALUES (?, ?, ?, ?);"""

        cursor.executemany(queryTemplateToInsert, recordList)
        sqliteConnection.commit()
        # print("Total", cursor.rowcount, "records inserted into", tableName, "table.")
        cursor.close()

    except sqlite3.Error as error:
        import sys
        print("Failed inserting given records into the sqlite table,", error, file=sys.stderr)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()

def tryOutInsertingToDb():
    import datetime
    now = datetime.datetime.now()
    # todayISO=now.strftime("%Y-%m-%d")
    # print( todayISO)
    insertToDbTable( dbName, "IPsTable", [(0, "1.1.1.1", "vymyšlený", now)] )

if __name__ == "__main__":
    tryOutCreatingDb()
    tryOutInsertingToDb()
    #view the db to check all ok.. 
