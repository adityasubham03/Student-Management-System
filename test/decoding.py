def decoding(u):
    decoded_str=''
    decoding=u.split("-")
    for k in decoding:
        if len(k)>0:
            decoded_str+=chr(int(k))
    return decoded_str
a = input("Enter the encoded string:- ")
print(f"The decoded string is '{decoding(a)}'")
