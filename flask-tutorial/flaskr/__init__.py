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
         password="123456",
         database="mydatabase"
         )
      return conn
      
   except mariadb.Error as e:
      print(f"Error connecting to the database: {e}")
      sys.exit(1)

conn = connectToDB()
cur = conn.cursor()

def createUsers():
   try:
      cur.execute("CREATE TABLE tick (id INT AUTO_INCREMENT PRIMARY KEY, FirstName varchar(255), LastName varchar(255))")
      sql = ("INSERT INTO tick FirstName, LastName VALUES (%s, %s)")
      val = ('Peter', 'Parker')
      cur.execute(sql, val)
      conn.commit()
      cur.execute("SELECT * FROM tick")
      print(cur.fetchall())
   except:
      cur.close()



createUsers()

""""
def updateUsers():
   try:
      update = "UPDATE users SET FirstName = 'Harry', LastName = 'Potter' WHERE FirstName = 'Jack'"
      cur.execute(update)
      conn.commit()
      cur.execute("SELECT * FROM users")
      print(cur.fetchall())
   except:
      cur.close()

updateUsers()
"""

"""
def deleteUsers():
   try:
      cur.execute("USE mydatabase")
      sql = "DELETE FROM users WHERE FirstName='John'"
      cur.execute(sql)
      conn.commit()
      cur.execute("SELECT * FROM users")
      print(cur.fetchall())
   except:
      cur.close()
   

deleteUsers()


def dropDatabase ():
   cur = connectToDB()
   try: 
      cur.execute("DROP DATABASE yea")
      cur.execute("DROP DATABASE no")
   except:
      cur.close()


# Use Connection
@app.route('/', methods=['GET','POST'])
def database():  
   try:
      cur.execute("USE mydatabase")
      sql = "SELECT * FROM users"
      cur.execute(sql)
      result = cur.fetchall()
      return "{}".format(result)
   except:
      cur.close()
   





if __name__ =='__main__':
 app.run(debug=True, host='0.0.0.0')
"""