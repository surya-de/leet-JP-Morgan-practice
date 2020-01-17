'''
 First task would br to find
 minimum pricr and followed
 by that we need to find the
 maximum profit associated to
 that minimum value.
'''
import sys
class Solution:
    def maxProfit(self, prices):
    	min_item = sys.maxsize
    	max_profit = 0
    	for elems in ls:
    		# If price is less than
    		# the minimum item till
    		# now update the min val.
    		if elems < min_item:
    			min_item = elems
    		# If the current list item
    		# is not a minimum value
    		# update the maximum profit
    		# value associated with the
    		# local minimum.
    		elif elems - min_item > max_profit:
    			max_profit = elems - min_item
    	return max_profit
if __name__ == '__main__':
	#ls = [7, 1, 5, 3, 6, 4]
	ls = [4, 3, 2, 1]
	s = Solution()
	print(s.maxProfit(ls))