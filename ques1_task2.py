a=int(input("Enter an integer:"))
reversed_num=0
remainder=0
while a !=0:
    remainder=a%10
    reversed_num=reversed_num+10+remainder
    a=a//10
    print("The reverse number of", a,"is",reversed_num)