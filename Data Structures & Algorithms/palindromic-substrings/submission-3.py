# Given i, if exist palindrome ending in i-1 and palindrome starting in i+1, then add 1 to result
class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = [ [False] * len(s) for _ in range(len(s)) ] # isPalindrome(start, end)
        result = 0

        for start in range(len(s) -1, -1, -1):
            for end in range(start, len(s)):
                if s[start] == s[end] and (end - start <= 1 or memo[start+1][end-1]):
                    memo[start][end] = True
                    result += 1
        
        return result

        

            