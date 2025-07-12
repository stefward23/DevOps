import mariadb
import datetime
from flask import Flask, render_template, request, redirect
import sys

app = Flask(__name__)

# Connect to database function.
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


#  Home route, function allows user to enter recipes and submit them to the database if no errors.
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


def fetchNewRecipes():
   try:
      dbc = connectToDB()
      crc = dbc.cursor()
      crc.execute("USE myrecipes")
      sql = "SELECT * FROM recipes"
      crc.execute(sql)
      results = crc.fetchall()
      return results
   except Exception as e:
      print("Error in fetchNameRecipes:", e)
      return[]
   finally:
      crc.close()
      dbc.close()
   
      

# Recipes route, function lists recipes from database.
@app.route('/recipes/', methods=['GET', 'POST'])
def listRecipe():

   
   try:
      results = fetchNewRecipes()
   except:
      print("Error in listRecipe:")
      results = []
   return render_template("recipes.html", results=results)  

# Update database, allows users to update database entries.
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def updateRecipe(id):
   db = connectToDB()
   cr = db.cursor()
   error = None
   
   if error is None:  
      try:
         print("one")
         # results = fetchNewRecipes(id) 
         results = "SELECT * FROM recipes WHERE id=?"
         print(results,(id,))
         cr.execute(results,(id,))
         results = cr.fetchall()
         db.commit()
         print(results)
      except cr.IntegrityError:
         error = "failure"
         print("Error in listRecipe:")
         results = []
      else:
         return render_template("update.html", results=results)

# Show whats in the form 
   
   # if request.method == 'GET':
   #    recipename = request.form['recipe_name']
   #    mealtime = request.form['meal_time']
   #    ingredients = request.form['ingredients']
   #    instructions = request.form['instructions']
   #    db = connectToDB()
   #    cr = db.cursor()
   #    results = fetchNewRecipes()
   #    error = None

      # if error is None:
      #    try:
      #       cr.execute(
      #       "UPDATE recipes (RecipeName, MealTime, Ingredients, Instructions) VALUES (?, ?, ?, ?)", (recipename, mealtime, ingredients, instructions),
      #       )
      #       db.commit()
      #    except cr.IntegrityError:
      #       error = f"Recipe {recipename} is already entered."
      #    else: 
      #       return render_template("update.html")
   
   return render_template("update.html", results=results)


# Delete route, function deletes entry from database.
@app.route('/delete/<int:id>', methods=['POST'])
def deleteRecipe(id):
   if request.method == 'POST':
      db = connectToDB()
      cr = db.cursor()
      error = None

      if error is None:
         try:
            cr.execute(
            "DELETE FROM recipes where id=?", (id,)
            )
            db.commit()
         except cr.IntegrityError:
            error = "failure"
         else: 
            return redirect('/recipes/')
    
 


if __name__ =='__main__':
 app.run(debug=True, host='0.0.0.0')

