class Solution:
    def reverse(self, x):
    	# Initiate a max value because
    	# the answer expects to return
    	# 0 if the value is more than
    	# max size of integers.
    	MAX_VAL = 2147483647
    	form_rev = rev_x = 0
    	# If the value is a negative
    	# integer the reverse logic
    	# can be done for absolute
    	# value of the integer.
    	i = abs(x)
    	# If the integer is 0 then
    	# return 0
    	if i == 0:
    		return 0
    	# Module to find the reverse
    	# interger of the given inp.
    	while i != 0:
    		# Extract the last value
    		# of the input integer.
    		rev_x = i % 10
    		# Form the input after
    		# removingthe last value.
    		i = i // 10
    		# Check for overflow in the
    		# reversed integer.
    		if form_rev > MAX_VAL // 10 or form_rev == MAX_VAL // 10 and rev_x > 7:
    			return 0
    		# If no chance of overflow
    		# form the reversed integer.
    		form_rev = (form_rev * 10) + rev_x
    	# return the reversed value
    	# with sign as provided in
    	# input.
    	return form_rev * int(x / abs(x))
if __name__ == '__main__':
	s = Solution()
	print(s.reverse(1534236469))