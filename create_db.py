import MySQLdb

db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="Sarya_12")
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS gym_tracker;")
print("Database gym_tracker created successfully!")
db.close()
