class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) < 1:
            return []

        number_dict = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        result = []
        def dfs(i, current_path):
            if i >= len(digits):
                result.append(current_path)
            else:
                for letter in number_dict[digits[i]]:
                    dfs(i + 1, current_path + letter)
        
        dfs(0, "")
        return result

        