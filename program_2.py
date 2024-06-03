# To take input from the user
num=int(input("Enter number: "))
# define a flag variable
flag= False

if(num==1):
    print(num,"is not a Prime number")
else:
    # check for factors
    for i in range(2,num):
        if(num%i)==0:
            # if factor is found, set flag to True
            flag=True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print(num,"is not a Prime number")
    else:
        print(num,"is a Prime number")