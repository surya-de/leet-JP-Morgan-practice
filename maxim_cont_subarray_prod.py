class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        prod = 1
        left = 0
        cntr = 0
        # When K is less than 1 ther can't
        # be any possible values.
        if k <= 1:
        	return 0
        # Go through all the elements in the
        # list and index it.
        for right, elems in enumerate(nums):
        	# Calculate the product for each
        	# iteration.
        	prod *= elems
        	# Keep removing the first element
        	# till the sum is more than K.
        	while prod >= k:
        		print(left)
        		# Remove the first element as
        		# the product goes over k.
        		prod /= nums[left]
        		# Increment the left counter.
        		left += 1
        	# Increment the counter.
        	cntr = cntr + (right - left) + 1
        return cntr
if __name__ == '__main__':
	s = Solution()
	#ls  = [10, 5, 2, 6]
	ls = [1, 2, 3]
	print(s.numSubarrayProductLessThanK(ls, 0))