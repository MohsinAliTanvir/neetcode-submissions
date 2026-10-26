class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:

        rows = len(matrix)
        cols = len(matrix[0])

        memo = {}

        def dfs(r, c):

            if (r, c) in memo:
                return memo[(r, c)]

            longest = 1

            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            for dr, dc in directions:

                new_r = r + dr
                new_c = c + dc

                if (
                    0 <= new_r < rows
                    and 0 <= new_c < cols
                    and matrix[new_r][new_c] > matrix[r][c]
                ):

                    path = 1 + dfs(new_r, new_c)

                    longest = max(longest, path)

            memo[(r, c)] = longest

            return longest

        answer = 0

        for r in range(rows):
            for c in range(cols):

                answer = max(
                    answer,
                    dfs(r, c)
                )

        return answer