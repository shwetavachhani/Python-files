# Program to hollow rectangle


def hollow_rect(n,m):
    for i in range(1,n):
        for j in range(1,m):
            if(i==1 or i==n or j==1 or j==m):
                print("*",end="")
            else:
                print(" ",end="")




rows=6
cols=20
hollow_rect(rows,cols)



