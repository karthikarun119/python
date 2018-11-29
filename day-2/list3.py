'''
Define a function is_palindrome() that recognizes palindromes 
(i.e. words that look the same written backwards).
 For example, is_palindrome("radar") should return True.
'''
def reverse(s):
    print(s)
    print(s[::-1])
    if s == s[::-1]:
        return True
    else :
        return False

string=input()
bool=reverse(string)
if bool==True:
    print("Given string %s is palindrome"%string)
else:
    print("Given string %s is not a palindromes"%string)