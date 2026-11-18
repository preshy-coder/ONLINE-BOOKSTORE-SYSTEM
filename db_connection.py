import mysql.connector

# Connect to the MySQL databasedb = mysql.connector.connect(
    host="localhost",        # MySQL host
    user="root",             # Your MySQL username
    password="",             
    database="online_bookstore"  # The name of your database
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# query to test connection 
cursor.execute("SHOW TABLES")

# Fetch and display the results
tables = cursor.fetchall()
print("Tables in the database:")
for table in tables:
    print(table)

# Close the connection
cursor.close()
db.close()
