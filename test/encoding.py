def encoding(u):
    u_hash = ""
    for i in range(len(u)):
        uh = str(ord(u[i]))+"-"
        u_hash+=uh
    return u_hash
username = input("Enter the string to encode:- ")
print(f"The decoded string is '{encoding(username)}'")
