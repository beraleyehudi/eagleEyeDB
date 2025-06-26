import mysql.connector

# class Dal:
conn = mysql.connector.connect(

    host="localhost",
    user="root",
    database="eagleeyedb")

# cursor = conn.cursor()

# @staticmethod
def dal_add(table, columns: str, values:tuple):
    encapsul = ','.join(["%s" for i in range(len(values))])
    with conn.cursor() as cursor:
        cursor.execute(f"INSERT INTO {table} ({columns}) VALUES ({encapsul})", values)
        conn.commit()


def dal_get(table, query):
    with conn.cursor(dictionary=True) as cursor:
        # cursor = conn.cursor(dictionary=True)
        cursor.execute(f"SELECT {query} FROM {table}")
        data = cursor.fetchall()

    return data

def dal_update(table, column, value, condition):
    with conn.cursor() as cursor:
        cursor.execute(f"UPDATE {table} SET {column} = {value} WHERE {condition}")
        conn.commit()

def del_delete(table, row):
    with conn.cursor() as cursor:
        cursor.execute(f"DELETE {row} FROM {table}")
        conn.commit()













