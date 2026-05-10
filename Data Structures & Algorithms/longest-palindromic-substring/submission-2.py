class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        best_palindrome = ""
        best_palindrome_len = 0
        for i in range(len(s)):
            L = R = i
            while L >= 0 and R < len(s) and s[L] == s[R]:
                palindrome_len = R - L + 1
                if palindrome_len > best_palindrome_len:
                    best_palindrome_len = palindrome_len
                    best_palindrome = s[L: R + 1]
                L -= 1
                R += 1

            L = i
            R = i + 1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                palindrome_len = R - L + 1
                if palindrome_len > best_palindrome_len:
                    best_palindrome_len = palindrome_len
                    best_palindrome = s[L: R + 1]
                L -= 1
                R += 1
        return best_palindrome