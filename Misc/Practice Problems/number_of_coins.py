"""
number_of_coins

Write a function that takes
in a number of cents (USD) as an
integer less than or equal to 100
and prints out the least amount
of coins needed to represent it.
"""

def number_of_coins(cents):
    coin_list = [100,25,10,5,1]
    least_coins = []
    for coin in coin_list:
        number_coins = cents//coin
        if number_coins == 0:
            continue
        else:
            cents = cents - number_coins * coin
            least_coins.extend(number_coins * [coin])
    return least_coins

#TEST CASES
print(number_of_coins(67))
print(number_of_coins(55))

p_challenge_value = 2**38
print(p_challenge_value)