class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)

        dp = [[False] * n for _ in range(n)]

        count = 0

        for length in range(1, n + 1):

            for left in range(n - length + 1):

                right = left + length - 1

                if s[left] == s[right]:

                    if length <= 2 or dp[left + 1][right - 1]:

                        dp[left][right] = True
                        count += 1

        return count