import mariadb
from flask import Flask
import sys

app = Flask(__name__)

def connectToDB():
   try:  
      conn = mariadb.connect(
         host="172.19.0.3",
         port=3306,
         user="root",
         password="123456")
      cur = conn.cursor()
      return cur
   
   except mariadb.Error as e:
      print(f"Error connecting to the database: {e}")
      sys.exit(1)
"""
def createDatabase ():
   cur = connectToDB()
   try:
      cur.execute("CREATE DATABASE ")     
   except:
      cur.close()
"""

def createTable(): 
   cur = connectToDB()
   try:
      cur.execute("USE mydatabase")
      cur.execute("CREATE TABLE new (FirstName varchar(255), LastName varchar(255))")
      cur.execute("INSERT INTO new (FirstName, LastName)" "VALUES ('Gang', 'Kup')")
      cur.connection.commit()
   except:
      cur.close() 

createTable()


"""
def dropDatabase ():
   cur = connectToDB()
   try: 
      cur.execute("DROP DATABASE yea")
      cur.execute("DROP DATABASE no")
   except:
      cur.close()

"""


"""
# Use Connection
@app.route('/', methods=['GET','POST'])
def database():




if __name__ =='__main__':
   app.run(debug=True, host='0.0.0.0')
"""