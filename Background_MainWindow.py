import mysql.connector

host = 'localhost'
user = 'krzysztof'
password = 'password'
database = 'db_clothes'

connection = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )




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

        if connection.connected():
            print("Polaczono")
            return connection
    except Exception as e:
        print(f'Blad polaczenia {e}')



def fn_GetListClothes(v_type, v_size,):
    global cursor
    cursor = connection.cursor()
    query = f"SELECT  t_clothes.c_id,t_clothes.c_type, t_clothes.c_size, t_employee.c_firstname,t_employee.c_lastname FROM t_clothes LEFT JOIN t_employee ON t_clothes.c_id_employee = t_employee.c_id WHERE c_size LIKE '{v_size}%' AND c_type LIKE '{v_type}%';"
    cursor.execute(query)
    results = cursor.fetchall()
    return results
    cursor.close()



