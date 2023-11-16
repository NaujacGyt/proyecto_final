#print "Resultados de MySQLdb:"
import mysql.connector
miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='Naujac00+', db='semillero' )
cur = miConexion.cursor()
cur.execute( "SELECT name_customer, lastname_customer FROM customers" )
for nombre, apellido in cur.fetchall() :
    print (nombre,apellido)
miConexion.close()