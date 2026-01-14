import mysql.connector as mysql
from dotenv import load_dotenv
import os
load_dotenv()  # loading the .env file

db = mysql.connect(
    host="localhost",
    user="root",
    password=os.getenv("SECRET_KEY"),
    database="expense_tracker"
)
if db.is_connected():
    print("DB is connected")
cursor = db.cursor()
product_name = input("Enter product name: ")
product_amount = float(input("Enter product amount: "))
product_date = input("Enter specific date and time (YYYY-MM-DD HH:MM:SS), else press enter for current time: ")

if product_date == '':
    my_sql = "INSERT INTO expenses (product_name, amount, date) VALUES (%s,%s,NOW());"
    values = (product_name, product_amount)
else:
    my_sql = "INSERT INTO expenses (product_name, amount, date) VALUES (%s,%s,%s);"
    values = (product_name, product_amount, product_date)
cursor.execute(my_sql, values)
db.commit()
cursor.execute("SELECT * FROM expenses;")
all_expenses = cursor.fetchall()
print(all_expenses)
