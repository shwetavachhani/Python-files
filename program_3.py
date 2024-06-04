#check if a sequence is a Palindrome.

def isPalindrome(s):
    print('hi')
    return s == s[::-1]
  
# Driver code
s=input("Enter number or string: ")
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")

#Python palindrome program w/o string functions
def reverse(text):
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]

n = input("ENTER  STRING\n")
if n==reverse(n):
    print ("It's a palindrome")
else:
    print ("It's not a palindrome")