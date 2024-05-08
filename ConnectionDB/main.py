import pyodbc


conn= pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server}; Server=192.168.0.1;DATABASE=infoporcinos;UID=sa;PWD=sq!-d4705!;")


with conn.cursor() as connect:



    sql =connect.execute( """
        SELECT 1,2,3,3,6,4
    
        """).fetchall()


    for i in sql:

            print(i)
