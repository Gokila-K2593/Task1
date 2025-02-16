a=int(input("Enter an integer:"))
reversed_num=0
while a !=0:
    reversed_num=int(str(a)[::-1])
    print("The reverse number of", a,"is",reversed_num)
    break;