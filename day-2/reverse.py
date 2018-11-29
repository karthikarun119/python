'''Define a function reverse() that computes the reversal of a string. 
For example, reverse("I am testing") should return the string "gnitset ma I".
'''
def reverse(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0] 
  
s = "I am testing"
  
 
  

print (reverse(s)) 