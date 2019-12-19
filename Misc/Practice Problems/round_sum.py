"""
Codingbat Problems
Logic II - round_sum

For this problem, we'll round an int
value up to the next multiple of 10 if
its rightmost digit is 5 or more, so 15
rounds up to 20. Alternatively, round down
to the previous multiple of 10 if its rightmost
digit is less than 5, so 12 rounds to 10.

Given 3 ints, a b c, return the sum of their
rounded values. To avoid code repetition, write
a seperate helper function "def round10(num):"
and call it 3 times. Write the helper entirely below
at the same indent level as round_sum()

"""

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

def round10(num):
    mod_10 = num%10
    if mod_10 < 5:
        return (num-mod_10)
    elif mod_10 => 5:
        return (num+(num-10))