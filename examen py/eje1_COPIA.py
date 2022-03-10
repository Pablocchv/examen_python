import mysql.connector
mysql=mysql.connector.connect(
    host='localhost',
    user='pablo',
    password='pablo',
    port='3306',
    database='empresa'
)
cursor1=mysql.cursor()

isbn=input("Escribe el ISBN")
tipo=input("Escribe el tipo de libro")
nombre=input("Escribe el nombre del libro")

ins="insert into libros (isbn,tipo,nombre)values ('"+isbn +"','"+ tipo+"','" +nombre +"' )"

cursor1.execute(ins)
mysql.commit()
mysql.close()

