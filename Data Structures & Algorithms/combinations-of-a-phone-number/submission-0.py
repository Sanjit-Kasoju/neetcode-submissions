class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res,sol=[],[]
        n=len(digits)

        letter_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if digits=="":
            return []

        def backtrack(i=0):
            if i==n:
                res.append(''.join(sol))
                return 

            for j in letter_map[digits[i]]:
                sol.append(j)
                backtrack(i+1)
                sol.pop()

        backtrack(0)
        return res
        