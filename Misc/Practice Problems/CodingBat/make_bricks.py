"""
Codingbat Problems
Logic II - make_bricks

We want to make a row of bricks that is
goal inches long. We have a number of small
bricks(1 inch) and big bricks(5 inches).

Return True if it is possible to make the goal
by choosing the given bricks.

Conditions: No Loops

"""

def make_bricks(small, big, goal):
    if big > 0:
        big_value = 5*big
        mod_brick = goal%5
        if small + big_value == goal:
            return True
        elif small + big_value < goal:
            return False
        elif small >= mod_brick:
            return True
        elif mod_brick > small:
            return False
    elif big == 0 and small < goal:
        return False
    elif small > goal:
        return True


# Test Cases

print(make_bricks(3, 1, 8)) #True
print(make_bricks(3, 1, 9)) #False
print(make_bricks(3, 2, 9)) #False
print(make_bricks(20, 4, 39)) #True
print(make_bricks(1000000, 1000, 1000100)) #True
print(make_bricks(2, 1000000, 100003)) #False

