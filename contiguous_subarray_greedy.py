'''
This is a Greedy approach which
targets to find the maximum val
for each step.
'''
class Solution:
    def maxSubArray(self, nums):
    	local_sum = global_sum = nums[0]
    	for i in range(1, len(nums)):
    		# The local maximum at each step
    		# can either be the begining of a
    		# new sequence of the continuation
    		# of the previous sequence.
    		local_sum = max(nums[i], local_sum + nums[i])
    		# Find the maximum of the local sum
    		# and previously decided global sum.
    		global_sum = max(local_sum, global_sum)
    	return global_sum
if __name__ == '__main__':
	ls = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
	s = Solution()
	print(s.maxSubArray(ls))