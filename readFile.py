#userfile = None
try:
    userfile = open('user.txt','r')
    #content = userfile.read()
    
    line = userfile.readline()
    while line!='':
        print(line)
        line = userfile.readline()
    userfile.close()

    
    lines = []
    userfile = open('user.txt','r')
    for line in userfile:
        lines.append(line)
    userfile.close()

    for line in lines:
        print(line)

    #print(content)
    #print(f"'{line1}', '{line2}', '{line3}'")
except FileNotFoundError:
    print("FileNotFoundError try agan")
#finally:    
#    userfile.close()
