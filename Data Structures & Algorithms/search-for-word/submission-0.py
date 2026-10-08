class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
    
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(r, c, i):

            # Found the entire word
            if i == len(word):
                return True

            # Invalid position or character
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited or
                board[r][c] != word[i]):
                return False

            # Choose
            visited.add((r, c))

            # DFS in four directions
            found = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            # Undo (backtrack)
            visited.remove((r, c))

            return found

        # Try every cell as a starting point
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False