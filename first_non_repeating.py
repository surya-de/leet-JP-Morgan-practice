from collections import Counter, OrderedDict
# Class to implement Ordered counter to
# store the count of occurances in the
# order they were encountered.
# This uses the concept of Ordered dict
# and counter from Python collections.
class OrderedCounter(Counter, OrderedDict):
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

class Solution:
    def firstUniqChar(self, s: str) -> int:
    	# Ordered counter object that stores
    	# the count of elemnts of string in
    	# the orderer they were encountered.
        counter = OrderedCounter(s).items()
        # Filter the Ordered dict items where
        # the value is 1.
        k = list(filter(lambda x : x[1] == 1, counter))
        # The length of the list is 0 means
        # there is no element present where
        # the occurance count is 1.
        if len(k) == 0:
        	return -1
        # Else return the index of the 1st
        # element in the list.
        # Since the order is intact, the
        # first element in list will always
        # be the 1st occurance.
        return s.index(k[0][0])

if __name__ == '__main__':
	s = Solution()
	print(s.firstUniqChar('cc'))