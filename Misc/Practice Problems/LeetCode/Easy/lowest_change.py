"""
lowest_change.py

This function will return the least
amount of change needed in USD.
"""

def lowest_change(coins):
	coin_list = [25,10,5,1]
	output_list = []
	for coin in coin_list:
		coin_check = coins // coin
		if coin_check == 0:
			continue
		else:
			coins = coins - coin_check * coin
			output_list.extend(coin_check * [coin])
	return output_list

# TEST CASE

print(lowest_change(67))

print(lowest_change(55))

print(lowest_change(2))

print(lowest_change(8))

print(lowest_change(99))
