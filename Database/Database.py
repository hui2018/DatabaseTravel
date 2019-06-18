import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='localhost',
                             database='world',
                             user='jack',
                             password='oregon123')
    if connection.is_connected():
       db_Info = connection.get_server_info()
       print("Connected to MySQL database... MySQL Server version on ",db_Info)
       """
       cursor = connection.cursor()
       cursor.execute("select database();")
       record = cursor.fetchone()
       print ("Your connected to - ", record)
       """

       sql_select_Query = "select * from world.country"
       cursor = connection.cursor(buffered=True)
       cursor.execute(sql_select_Query)
       fetching_size = 4
       records = cursor.fetchmany(fetching_size)
       #records = cursor.fetchall()
       for row in records:
           print ("ID=", row, "\n")
           print ("testing", row[0], "\n")
       cursor.close()

except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
