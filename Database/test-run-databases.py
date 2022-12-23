import mysql.connector as sql
connector = sql.connect(host="localhost",user="root",passwd="27Adich@",database="stms")
if connector.is_connected():
    print("Successfully Connected to the MySQL Server!")
cursor=connector.cursor()
print("Fetching Data From The Database!")
cursor.execute("SELECT Admn_no FROM student_records")
data = cursor.fetchall()
for i in data:
    if 6359 in i:
        print("True")
