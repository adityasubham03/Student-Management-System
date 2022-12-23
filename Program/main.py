import security
import designs
import getpass
import students
import marks
login = False
count = 3
while login is False:
    designs.print_bar()
    username = input("Enter your username:- ")
    password = getpass.getpass(prompt='Enter your password:- ')
    if security.user_check(username,password) is True:
        print("Welcome To The Student Data Management System")
        login = True
    else:
        count=count-1
        print(f"Only {count} tries left!")
        print("Please Try Again With Correct Credentials")
        if count == 0:
            break
    designs.print_bar()

while login is True:
    designs.print_bar()
    print("""Enter your choice
    1. Manage Students
    2. Manage Students Marks
    0. Exit""")
    choice = int(input())
    designs.print_bar()
    if choice == 1:
        students.students_menu(True)
        designs.print_bar()
    elif choice==2:
        marks.exams_menu(True)
        designs.print_bar()
    elif choice==0:
        login = False
else:
    print("You have logged out successfully!")
a = input("Press enter to exit the window")
