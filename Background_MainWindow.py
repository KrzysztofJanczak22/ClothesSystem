import mysql.connector

#connect to database


def fn_ConenctToDatabase():
    host = 'localhost'
    user = 'krzysztof'
    password = 'password'
    database = 'db_clothes'
    try:
        connection = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )

        if connection.is.connected():
            print("Polaczono")
            return connection
    except Exception as e:
        print(f'Blad polaczenia {e}')

def