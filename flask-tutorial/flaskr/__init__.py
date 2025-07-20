import mariadb
from flask import Flask, render_template, request, redirect
import sys

app = Flask(__name__)

# Connect to database function.
def connectToDB(): 
   try:  
      conn = mariadb.connect(
         host="172.19.0.3", # Address to connect to database
         port=3306, # Port used by database application
         user="root", # Username of database user
         password="123456", # Password of database user
         database="myrecipes" # Database to connect to
         )
      return conn     
   except mariadb.Error as e: # Set mariadb.error as variable e
      print(f"Error connecting to the database: {e}") # Print error connecting and the mariadb error as well
   sys.exit(1)


# Redirect / to Home Page
@app.route('/', methods=['GET'])  # / Route
def redirectToHome(): # Function to Redirect / to Home
      return redirect('/home/') # Return home

#  Home route, Function allows user to enter Recipes and submit them to the Database if no errors.
@app.route('/home/', methods=['GET', 'POST']) # Home Route with GET and POST HTTP Request Methods
def enterRecipe(): # EnterRecipe function
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
         finally:
            cr.close()
            db.close()

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
   
   if request.method == 'GET': 
      try:
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
      finally:
         cr.close()
         db.close()
         return render_template("update.html", results=results)
   
   elif request.method == 'POST':
      try:

         recipename = request.form['recipe_name']
         mealtime = request.form['meal_time']
         ingredients = request.form['ingredients']
         instructions = request.form['instructions']

         cr.execute(
         "UPDATE recipes SET RecipeName = ?, MealTime = ?, Ingredients = ?, Instructions = ? WHERE id = ?",
         (recipename, mealtime, ingredients, instructions, id)
)

         db.commit()
      except cr.IntegrityError:
         error = "failure"
         print("Error")
      finally:
         cr.close()
         db.close()
         return redirect('/recipes/') 
   else:
         error = "failure"
         print("Error in listRecipe:")
         results = []  
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
         finally:
            cr.close()
            db.close()
      else: 
         return redirect('/recipes/')
    


if __name__ =='__main__':
 app.run(debug=True, host='0.0.0.0')

