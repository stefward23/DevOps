import mariadb
import datetime
from flask import Flask, render_template, request, redirect
import sys

app = Flask(__name__)

def connectToDB():
   try:  
      conn = mariadb.connect(
         host="172.19.0.3",
         port=3306,
         user="root",
         password="123456",
         database="myrecipes"
         )
      return conn
      
   except mariadb.Error as e:
      print(f"Error connecting to the database: {e}")
      sys.exit(1)

conn = connectToDB()
cur = conn.cursor()

def createUsers():
   try:
      cur.execute("CREATE TABLE IF NOT EXISTS avengers (id INT AUTO_INCREMENT PRIMARY KEY, FirstName VARCHAR(255), LastName VARCHAR(255))")
      print("works")
      sql = "INSERT INTO avengers (FirstName, LastName) VALUES (%s, %s)"
      val = ('Bruce', 'Cat')
      cur.execute(sql, val)
      conn.commit()
      cur.execute("SELECT * FROM avengers")
      print(cur.fetchall())
   except:
      print("did not work")


def updateUsers():
   try:
      update = "UPDATE users SET FirstName = 'Harry', LastName = 'Potter' WHERE FirstName = 'Jack'"
      cur.execute(update)
      conn.commit()
      cur.execute("SELECT * FROM users")
      print(cur.fetchall())
   except:
      cur.close()


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
   


def dropDatabase ():
   cur = connectToDB()
   try: 
      cur.execute("DROP DATABASE yea")
      cur.execute("DROP DATABASE no")
   except:
      cur.close()

def database():  
   try:
      cur.execute("USE mydatabase")
      sql = "SELECT * FROM users"
      cur.execute(sql)
      result = cur.fetchall()
      return "{}".format(result)
   except:
      cur.close()

# #Creates loop 
 
# names = [
#          {"firstName": "John", "lastName": "Smith"},
#          {"firstName": "Betty", "lastName": "White"},
#          {"firstName": "Carl", "lastName": "Ben"},
#    ]

# for name in names:
#    print(names[0]["firstName"])


content = "Static content added to the html form"

# Use Connection

@app.route('/home/', methods=['GET', 'POST'])
def enterRecipe():
   if request.method == 'POST':
      recipename = request.form['recipe_name']
      mealtime = request.form['meal_time']
      ingredients = request.form['ingredients']
      instructions = request.form['instructions']
      db = connectToDB()
      cr = db.cursor()
      error = None

      # if not recipename:
      #    error = "Recipe is needed."
      # elif not mealtime:
      #    error = "Mealtime is needed."
      # elif not ingredients:
      #    error = "Ingredients is needed."
      # elif not instructions:
      #    error = "Instructions is needed."

      if error is None:
         try:
            cr.execute(
            "INSERT INTO recipes (RecipeName, MealTime, Ingredients, Instructions) VALUES (?, ?, ?, ?)", (recipename, mealtime, ingredients, instructions),
            )
            db.commit()
         except cr.IntegrityError:
            error = f"Recipe {recipename} is already entered."
         else: 
            return render_template("home.html")

   return render_template("home.html")    


@app.route('/recipes/')
def recipeList():  
   try:
      cur.execute("USE myrecipes")
      sql = "SELECT * FROM recipes"
      cur.execute(sql)
      # results = cur.fetchall()
      results = cur.fetchall()
      
   except:
      cur.close()

   return render_template("recipes.html", results = results)    


@app.route('/recipes/<int:id>', methods=["GET"])
def select1Recipe(id):
   try:

      cur.execute("USE myrecipes")
      delete = "DELETE FROM recipes where id='4'"
      cur.execute(delete)
      conn.commit()
      results = cur.fetchone()
   

      results = cur.execute("SELECT * FROM recipes").fetchall()
   except:
      cur.close()
   return redirect('/recipes/')
   # return render_template("recipes.html")

if __name__ =='__main__':
 app.run(debug=True, host='0.0.0.0')

