## Student Management System Login System
import mysql.connector as sql
def user_check(u,p):
    connector = sql.connect(host="localhost",username="root",passwd="123456",database="stms1")
    if connector.is_connected():
        print("Successfully Connected to the MySQL Server!")
        print("Checking Your Credentials")
        cursor=connector.cursor()
        u1=u_hashing(u)
        p1=p_hashing(p)
        query = "SELECT * FROM user_login WHERE username = '{}'".format(u1)
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data)>0:
            if data[0][0]==u1:
                if data[0][1]==p1:
                    print("User Successfully Authenticated")
                    print("Logging You In")
                    return True
                else:
                    print("Password Incorrect")
            else:
                print("User Not Found")
                return False
        else:
            print("Username not found")
            print("Please enter a valid username!")
    
def p_hashing(p):
    p_hash = ''
    for i in range(len(p)):
        ph = str(ord(p[i]))+"-"
        p_hash+=ph
    return p_hash
    
def u_hashing(u):
    u_hash = ""
    for i in range(len(u)):
        uh = str(ord(u[i]))+"-"
        u_hash+=uh
    return u_hash
