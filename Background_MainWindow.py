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


#Screen DialogClothes
def fn_GetListClothes(v_type, v_size,):
    cursor = connection.cursor()
    query = (f"SELECT  t_clothes.c_id,t_clothes.c_type, t_clothes.c_size, t_employee.c_firstname,t_employee.c_lastname FROM t_clothes LEFT JOIN t_employee ON t_clothes.c_id_employee = t_employee.c_id WHERE c_size "
             f"LIKE '{v_size}%' AND c_type LIKE '{v_type}%';")
    cursor.execute(query)
    results = cursor.fetchall()
    return results
    cursor.close()

#Screen DialogSearchPerson

def fn_GetListEmployee(v_firstname, v_lastname):
    cursor = connection.cursor()
    print(v_firstname, v_lastname)
    query = f"SELECT * FROM t_employee WHERE c_firstname LIKE '{v_firstname}%' AND c_lastname LIKE '{v_lastname}%';"
    cursor.execute(query)
    results = cursor.fetchall()
    return results
def fn_AssignCloth(v_idcloth,v_idperson):
    cursor = connection.cursor()
    query = f"UPDATE t_clothes SET c_id_employee = {v_idperson} WHERE c_id = {v_idcloth};"
    cursor.execute(query)
    connection.commit()
    cursor.close()
