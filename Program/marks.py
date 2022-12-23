import mysql.connector as sql
connector = sql.connect(host="localhost",username="root",passwd="123456",database="stms1")
cursor=connector.cursor()
def exams_menu(menu):
    while menu is True:
        print('''Enter 1 to Display the marks of all the students
                Enter 2 to Edit the marks of the Students
                Enter 3 to Add marks of student
                Enter 4 to delete marks of student
                Enter 5 to Go Back to Previous Menu''')
        choice_1 = True
        while choice_1:
            x = input("Enter your choice:- ")
            if x in ['1','2','3','4','5']:
                x = int(x)
                choice_1 = False
            else:
                print("Only integers are allowed between 1 and 5")
        if x==1:
            displaymarks()
        elif x==2:
            edit_marks()
        elif x==3:
            add_marks()
        elif x==4:
            del_marks()
        elif x==5:
            menu=False

def displaymarks():
    query = "SELECT * FROM student_marks"
    cursor.execute(query)
    data = cursor.fetchall()
    print("|------------------------------------------------------------------------|")
    print("|Roll Number | Chemistry| Physics   | Maths | Computer Science | English |")
    print("|------------------------------------------------------------------------|")
    for i in data:
        if i[0]<10:
            ff = " "
        else:
            ff=""
        print(f"|{i[0]}{ff}          |{i[1]}        | {i[2]}        | {i[3]}    | {i[4]}               | {i[5]}      |")
    print("|------------------------------------------------------------------------|")
def add_marks():
    Roll_no = int(input("Enter the Roll number of the student:- "))
    a = check_id(Roll_no)
    if a is True:
        print("Data Already Exists")
    else:
        english = int(input("Enter the marks for English:- "))
        maths = int(input("Enter the marks for Maths:- "))
        physics = int(input("Enter the marks for Physics:- "))
        chemistry = int(input("Enter the marks for Chemistry:- "))
        cs = int(input("Enter the marks for Computer Science:- "))
        vals = (Roll_no,chemistry,physics,maths,cs,english)
        query = "INSERT INTO student_marks VALUES({},{},{},{},{},{})".format(Roll_no,chemistry,physics,maths,cs,english)
        cursor.execute(query)
        connector.commit()
        print("Data has been inserted!")


def edit_marks():
    Roll_No = int(input("Enter the roll number:- "))
    gg = check_id(Roll_No)
    if gg is True:
        print('''To edit chemistry marks input 'c'
        To edit physics marks input 'p'
        To edit maths marks input 'm'
        To edit Computer Science marks input 'cs'
        To edit english marks input 'e'
        ''')
        gh = input("Enter your choice:- ").lower()
        if gh == "c":
            um = int(input("Enter corrected marks for chemistry:- "))
            query = "UPDATE student_marks SET Chemistry = {} WHERE Roll_No = {}".format(um,Roll_No)
            cursor.execute(query)
            connector.commit()
            print("Data has been updated successfuly!")
        elif gh == "p":
            um = int(input("Enter corrected marks for Physics:- "))
            query = "UPDATE student_marks SET Physics = {} WHERE Roll_No = {}".format(um,Roll_No)
            cursor.execute(query)
            connector.commit()
            print("Data has been updated successfuly!")
        if gh == "m":
            um = int(input("Enter corrected marks for maths:- "))
            query = "UPDATE student_marks SET Maths = {} WHERE Roll_No = {}".format(um,Roll_No)
            cursor.execute(query)
            connector.commit()
            print("Data has been updated successfuly!")
        if gh == "cs":
            um = int(input("Enter corrected marks for Computer Science:- "))
            query = "UPDATE student_marks SET Computer_Science = {} WHERE Roll_No = {}".format(um,Roll_No)
            cursor.execute(query)
            connector.commit()
            print("Data has been updated successfuly!")
        if gh == "e":
            um = int(input("Enter corrected marks for English:- "))
            query = "UPDATE student_marks SET English = {} WHERE Roll_No = {}".format(um,Roll_No)
            cursor.execute(query)
            connector.commit()
            print("Data has been updated successfuly!")
    else:
        print("Record doesnot exist!")


def del_marks():
    Roll_No = int(input("Enter the roll number to delete:- "))
    gg = check_id(Roll_No)
    if gg is True:
        query = "DELETE FROM student_marks WHERE Roll_No={}".format(Roll_No)
        cursor.execute(query)
        connector.commit()
        print("Successfully deleted the data!")
    else:
        print("Data doesnot exist!")       

def check_id(roll):
    cursor.execute("SELECT Roll_No FROM student_marks")
    data = cursor.fetchall()
    l = []
    if len(data)==0:
        print("Empty")
    else:
        for i in range(len(data)):
            g = data[i][0]
            l.append(g)
        else:
            if roll in l:
                return True
            else:
                return False

