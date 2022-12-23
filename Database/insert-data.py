import mysql.connector as sql
connector = sql.connect(host="localhost",user="root",passwd="YourPasswordHere",database="stms")
if connector.is_connected():
    print("Successfully Connected to the MySQL Server!")
cursor=connector.cursor()
print("Inserting Data")
query1 = "INSERT INTO user_login VALUES('{}','{}')".format("97-100-109-105-110-","97-100-109-105-110-")
query2 = "INSERT INTO user_login VALUES('{}','{}')".format("97-110-99-","97-100-105-116-121-97-115-117-98-104-97-109-48-51-")
query3 = "INSERT INTO user_login VALUES('{}','{}')".format("97-100-105-100-97-115-","97-100-105-49-51-50-48-48-51-")
cursor.execute(query1)
cursor.execute(query2)
cursor.execute(query3)
connector.commit()
print("Data Inserted")
