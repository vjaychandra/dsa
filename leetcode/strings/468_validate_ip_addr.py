
def validIPAddress(s):

    res = ""

    if "." in s and s.count(".") == 3:
        if all(str(i) == str(int(i)) and 0<=int(i)<=255 for i in s.split(".")):
            res = "IPv4"

    
