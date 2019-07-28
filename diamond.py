spaces = 3
while(spaces >= 0):
    if(spaces != 3):        
        print(" " * spaces + "*" ,end = "")
    else:
        print(" " * spaces + "*")
    i = 3 - spaces 
    spaces = spaces - 1
    innerspace  = i * 2 - 1
    if i == 0:
        continue
    print(" " * innerspace + "*")
    #added a line