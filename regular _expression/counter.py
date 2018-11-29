import sys
import os


def make_counter(x):
    print('entering make_counter')
    while 1:
        yield x
        print('incrementing x')
        x = x + 1
counter = make_counter(2)
print(counter)
print(next(counter))
foo = long_function_name(
    var_one,
    var_two,
    var_three,
    var_four)
if (this_is_one_thing and
        that_is_another_thing):
        # Add a comment, which will provide some distinction in editors
        do_something()
# Add a comment, which will provide some distinction in editors
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)