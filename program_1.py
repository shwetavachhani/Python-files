# Program to display the Fibonacci sequence up to n-th term

fibbo = int(input("How many terms? "))

n1=0
n2=1
count =0

if(fibbo<1):
    print('please enter valid number')
else:
    print('Fibbonacci Series:')
    while(count<fibbo):
        print(n1)
        nth=n1+n2

        n1=n2
        n2=nth
        count +=1
        