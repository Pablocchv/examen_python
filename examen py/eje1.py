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



cursor2=mysql.cursor()

isbn=input("Escribe el ISBN")
tipo=input("Escribe el tipo de libro")
nombre=input("Escribe el nombre del libro")

ins2="insert into libros (isbn,tipo,nombre)values ('"+isbn +"','"+ tipo+"','" +nombre +"' )"

cursor2.execute(ins2)
mysql.commit()
mysql.close()


cursor3=mysql.cursor()

isbn=input("Escribe el ISBN")
tipo=input("Escribe el tipo de libro")
nombre=input("Escribe el nombre del libro")

ins3="insert into libros (isbn,tipo,nombre)values ('"+isbn +"','"+ tipo+"','" +nombre +"' )"


cursor3.execute(ins3)
mysql.commit()
mysql.close()


