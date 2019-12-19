"""
fizzbuzz.py

Write a a program to output
the first n FizzBuzz numbers
where any number divisible by 3
is 'fizz' and any number divisible
by 5 is buzz
"""

def fizzbuzz(n):
    num_list = []
    for i in range(1,n+1):
        if i%3 == 0:
            num_list.append('fizz')
        elif i%5 == 0:
            num_list.append('buzz')
        else:
            num_list.append(i)
    return num_list

# TEST CASE
print(fizzbuzz(100))
