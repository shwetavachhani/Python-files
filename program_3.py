#check if a sequence is a Palindrome.

def isPalindrome(s):
    return s == s[::-1]
  
# Driver code
s=input("Enter number or string: ")
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")