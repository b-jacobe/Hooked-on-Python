"""
number_of_coins

Write a function that takes
in a number of cents (USD) as an
integer less than or equal to 100
and prints out the least amount
of coins needed to represent it.
"""

def number_of_coins(cents):
    # U.S. coin value list
    coin_list = [100,25,10,5,1]
    least_coins = list()
    # Floor expression to check if cents 
    # can be appended to least_coin
    for coin in coin_list:
        number_coins = cents//coin
        if number_coins == 0:
            continue
        else:
            cents = cents - number_coins * coin
            least_coins.extend(number_coins * [coin])
    return print(least_coins)

# Driver Code
if __name__ == "__main__":
    number_of_coins(67)
    number_of_coins(55)
    number_of_coins(99)
