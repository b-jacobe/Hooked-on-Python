"""
Codingbat Problems
Logic II - make_chocolate

We want to make a package of goal kilos of
chocolate. We have small bars (1) and big
bars (5). 

Return the number of small bars
to use, assuming we always use big bars
before small bars. Return -1 if it can't
be done.

Conditions: No Loops

"""

def make_chocolate(small, big, goal):
    big = mod_value(big, goal)
    sum_chocolate = small + (big*5)
    if sum_chocolate == goal:
        return small
    elif sum_chocolate < goal:
        return -1
    else:
        return goal - big


def mod_value(big, goal):
    mod_chocolate = goal%5
    if mod_chocolate > 5:
        big -= 1
        return mod_value(big, goal)
    else:
        return big

value_a = 18
value_b = 9

print(value_a%5)
print(value_b%5)

