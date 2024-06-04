# Python program to reverse a string using iteratively and recursion

#Reverse a string in Python using loop

def reverse(string):
    str = ""
    for i in string:
        str = i + str
    return str

string=input("Enter string: ")
data = reverse(string)
print("The original string is : ", end="")
print(string)
 
print("The reversed string(using loops) is : ", end="")
print(reverse(string))

#Reverse a string in Python using recursion
def recurse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]

print("The reversed string(using recursion) is : ", end="")
print(recurse(string))