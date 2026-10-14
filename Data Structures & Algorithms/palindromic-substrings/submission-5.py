# class Solution:
#     def countSubstrings(self, s: str) -> int:

#         n = len(s)

#         dp = [[False] * n for _ in range(n)]

#         count = 0

#         for length in range(1, n + 1):

#             for left in range(n - length + 1):

#                 right = left + length - 1

#                 if s[left] == s[right]:

#                     if length <= 2 or dp[left + 1][right - 1]:

#                         dp[left][right] = True
#                         count += 1

#         return count

class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)

        memo = [[None] * n for _ in range(n)]

        def isPalindrome(left, right):

            # Empty or single character
            if left >= right:
                return True

            # Already calculated
            if memo[left][right] is not None:
                return memo[left][right]

            # Outside characters match
            # AND inside is palindrome
            # memo[left][right] = (
            #     s[left] == s[right]
            #     and
            #     isPalindrome(left + 1, right - 1)
            # )

            if s[left] != s[right]:
                memo[left][right] = False

            else:
                memo[left][right] = isPalindrome(left + 1, right - 1)

            return memo[left][right]


        count = 0

        for left in range(n):
            for right in range(left, n):

                if isPalindrome(left, right):
                    count += 1

        return count