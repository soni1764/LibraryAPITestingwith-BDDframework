import configparser
import mysql.connector
from mysql.connector import Error


def getconfig():
    config = configparser.ConfigParser()
    config.read(".\\utilities\\propertiese.ini")
    return config


conn_config = {
    "host": getconfig()["SQL"]["host"],
    "database": getconfig()["SQL"]["database"],
    "user": getconfig()["SQL"]["user"],
    "password": getconfig()["SQL"]["password"]
}


def getConnection():
    try:
        conn = mysql.connector.connect(**conn_config)
        if conn.is_connected():
            print("Connection Successful")
            return conn
    except Error as e:
        print(e)


def getQuery(query):
    conn = getConnection()
    curser = conn.cursor()
    curser.execute(query)
    row = curser.fetchone()
    conn.close()
    print(row)
    return row


def getUsername():
    return "soni1764"


def getToken():
    return "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"

