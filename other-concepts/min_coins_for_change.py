"""
Find minimum number of ocins that make a given value

Given a value V, if we want to make change for V cents, and we have infinite
supply of each of C = [C1, C2, ..., Cm] valued coins, what is the minimum number
of coins to make the change?

http://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/

Example:
	Input: 		coins = [25, 10, 5], V = 30
	Output:		2

	Input:		coins = [9, 6, 5, 1], V = 11
	Output:		2
"""

# iterative soltuion; does not cover all cases
def min_coins_for_change(coins, value, total_count=0):
	for coin in coins:
		coin_count = value/coin
		total_count += coin_count
		value -= coin*coin_count
		print "coin", coin
		print "coin count", coin_count
		print "new value", value

	return total_count

# recursive solution that covers all cases
def min_coins_for_change_v2(coins, value):
	if value == 0:
		return 0

	res = float('inf')

	for coin in coins:
		if coin <= value:
			coin_result = min_coins_for_change_v2(coins, value-coin)
			if coin_result + 1 < res:
				res = coin_result + 1

	return res