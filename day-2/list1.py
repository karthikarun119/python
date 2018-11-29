'''Define a function sum() and a function multiply() that sums and multiplies (respectively)
 all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and
  multiply([1, 2, 3, 4]) should return 24.
'''

def sum1(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def multiply(numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total
print (sum1([1, 2, 3, 4]))
print (multiply([1, 2, 3, 4]))
 