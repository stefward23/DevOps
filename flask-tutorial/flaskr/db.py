# Module Import
import mariadb
import sys

# Instantiate Connection
try:
   conn = mariadb.connect(
      host="192.0.2.1",
      port=3306,
      user="db_user",
      password="USER_PASSWORD")
except mariadb.Error as e:
   print(f"Error connecting to the database: {e}")
   sys.exit(1)

# Use Connection
# ...

# Close Connection
conn.close()
