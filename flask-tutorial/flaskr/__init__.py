import mariadb
import datetime
from flask import Flask, render_template, request, redirect
import sys

app = Flask(__name__)

# Define function that connects to Database
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


# Create Home Route

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


# Create Recipes Route

@app.route('/recipes/', methods=['GET', 'POST'])
def recipeList():
   if request.method == 'POST':
      try:
         dbc = connectToDB()
         crc = dbc.cursor()
         crc.execute("USE myrecipes")
         delete = ("DELETE FROM recipes where id=s%")
         crc.execute(delete)
         print("This has be deleted")
         crc.commit()
      except:
         crc.close()
        

   else:
      try:
         dbc = connectToDB()
         crc = dbc.cursor()
         crc.execute("USE myrecipes")
         sql = "SELECT * FROM recipes"
         crc.execute(sql)
         results = crc.fetchall()
      
      except:
         crc.close() 
   return render_template("recipes.html", results=results)  

# @app.route('/recipes/<int:id>', methods=["POST"])
# def select1Recipe(id):
#    try:

#       cur.execute("USE myrecipes")
#       delete = "DELETE FROM recipes where id='1'"
#       cur.execute(delete)
#       conn.commit()
#       print("Entry Deleted")

#       cur.execute("SELECT * FROM recipes")
#       results = cur.fetchall()

#    except:
#       cur.close()
#    return render_template("recipes.html", results=results)    
   
   # return redirect('/recipes/')
   # return render_template("recipes.html")

if __name__ =='__main__':
 app.run(debug=True, host='0.0.0.0')

