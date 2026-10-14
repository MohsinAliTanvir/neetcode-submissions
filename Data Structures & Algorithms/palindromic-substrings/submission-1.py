class Solution:
    def countSubstrings(self, s: str) -> int:


        n = len(s)
        dp = [False] * n
        count = 0

        for left in range(n - 1, -1, -1):

            for right in range(n - 1, left - 1, -1):

                if s[left] == s[right]:

                    if right - left <= 2 or dp[right - 1]:
                        dp[right] = True
                        count += 1
                    else:
                        dp[right] = False

                else:
                    dp[right] = False

        return count
        