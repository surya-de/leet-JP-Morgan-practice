class Solution:
    def letterCombinations(self, digits):
        store = []
        dictnary = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
            }
        def backtrack(let, newxt_val):
            if len(newxt_val) == 0:
                store.append(let)
            else:
                for elems in dictnary[newxt_val[0]]:
                    backtrack(let + elems, newxt_val[1:])
        if digits:
            backtrack('', digits)
        return store
if __name__ == '__main__':
	s = Solution()
	a = ''
	print(s.letterCombinations(a))