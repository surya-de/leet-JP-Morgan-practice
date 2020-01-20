class Solution:
    def isHappy(self, n):
    	storage = set()
    	def findSum(i):
    		total = 0
    		while i != 0:
    			rem = i % 10
    			i = i // 10
    			total += rem ** 2
    		return total
    	val = findSum(n)
    	while val != 1:
    		if val not in storage:
    			storage.add(val)
    			val = findSum(val)
    		else:
    			return False
    	else:
    		print(storage)
    		return True

if __name__ == '__main__':
	s = Solution()
	print(s.isHappy(0))