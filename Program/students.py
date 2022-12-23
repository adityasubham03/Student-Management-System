import mysql.connector as sql
import datetime
connector = sql.connect(host="localhost",username="root",passwd="123456",database="stms1")
cursor=connector.cursor()
def students_menu(menu):
    while menu is True:
        print('''Enter 1 to Display the details of all the students
                Enter 2 to Edit the details of the Students
                Enter 3 to Add a new student
                Enter 4 to delete a student
                Enter 5 to Go Back to Previous Menu''')
        choice_1 = True
        while choice_1:
            x = input("Enter your choice:- ")
            if x in ['1','2','3','4''5']:
                x = int(x)
                choice_1 = False
            else:
                print("Only integers are allowed between 1 and 5")
        if x==1:
            displayStudents()
        elif x==2:
            edit_student()
        elif x==3:
            add_student()
        elif x==4:
            del_student()
        elif x==5:
            menu=False

def displayStudents():
    query = "SELECT * FROM student_records"
    cursor.execute(query)
    data = cursor.fetchall()
    print(f"|{'-'*115}-|")
    print(f"|Roll|Name{' '*34}| Dob        | Admission Number | Gender | Fathers Name{' '*18}|")
    print(f"|{'-'*115}-|")
    for i in data:
        if i[0]<10:
            ff = " "
        else:
            ff=""
        max=30
        space=30-len(i[1])
        print(f"|{i[0]}{ff}  |{i[1]}{' '*space}        | {i[2]} | {i[3]}             | {i[4]}      | {i[5]}{' '*(30-len(i[5]))}|")
    print(f"|{'-'*115}-|")

def add_student():
    roll = int(input("Enter the Roll Number of the student:- "))
    name = input("Enter the name of the student:- ").upper()
    year = int(input("Enter the birth month in the order (yyyy):- "))
    month = int(input("Enter the birth month in the order (mm):- "))
    date = int(input("Enter the birth date in the order (dd):- "))
    dob = datetime.date(year,month,date)
    admn = int(input("Enter the admission number:- "))
    gender = input("Enter M for Male and F for Female:- ").upper()
    fname = input("Enter father's name of the student:- ").upper()

    query = "INSERT INTO student_records VALUES('{}','{}','{}','{}','{}','{}')".format(roll,name,dob,admn,gender,fname)
    cursor.execute(query)
    connector.commit()
    print("Data has been inserted!")

def edit_student():
    back = False
    while back is False:
        admn = int(input("Enter the admission number to edit:- "))
        id100 = check_id(admn)
        if id100 is False:
            print("Admission Number doesnot Exist")
            back = True
        else:
            print('''To edit student\'s name please input "name" 
                    To edit DOB please input "dob"
                    To edit Father\'s name input "fname"
                    To go back to the previous menu input "pre"
            ''')
            echoice = input("What do you want to edit:- ").lower()
            if echoice == 'name':
                uadmn = admn
                uname = input("Enter the corrected name:- ")
                vals = (uname,admn)
                uquery = "UPDATE student_records SET Name=%s WHERE Admn_no=%s"
                cursor.execute(uquery,vals)
                connector.commit()
                print("Data Has Been Updated Successfully!")
                back = True
            elif echoice == 'dob':
                dob_year = int(input("Enter the year of birth:- "))
                dob_month = int(input("Enter the month of birth:- "))
                dob_day = int(input("Enter the day of birth:- "))
                dob_update = datetime.date(dob_year,dob_month,dob_day)
                vals = (dob_update,admn)
                udob = "UPDATE student_records SET Dob=%s WHERE Admn_no=%s"
                cursor.execute(udob,vals)
                print("Date of birth will be updated to:-",dob_update)
                connector.commit()
                print("Data has been updated Successfully!")
                back = True
            elif echoice == 'fname':
                fadmn = admn
                fname = input("Enter the corrected name:- ")
                fvals = (fname,fadmn)
                ufquery = "UPDATE student_records SET Father_name=%s WHERE Admn_no=%s"
                cursor.execute(ufquery,fvals)
                connector.commit()
                print("Data Has Been Updated Successfully!")
                back = True
            elif echoice == 'pre':
                back = True
            else:
                print("Enter correct option:- ")
                back = True

def check_id(admn):
    cursor.execute("SELECT Admn_no FROM student_records")
    data = cursor.fetchall()
    l = []
    if len(data)==0:
        print("Empty")
    else:
        for i in range(len(data)):
            g = data[i][0]
            l.append(g)
        else:
            if admn in l:
                return True
            else:
                return False

def del_student():
    back = False
    id100 = False
    while back is False:
        while id100 is False:
            admn = int(input("Enter the admission number to edit:- "))
            id100 = check_id(admn)
            if id100 == False:
                print(f"Admission number {admn} Doesn't Exist.If you want to try again enter 't' otherwise enter 'q' to go back to previous menu!")
                hh = input("Enter your choice:- ").lower()
                if hh == 'q':
                    back = True
        else:
            query="delete from student_records WHERE Admn_no = {}".format(admn)
            cursor.execute(query)
            connector.commit()
            print("The record has been deleted successfully")
            back = True
