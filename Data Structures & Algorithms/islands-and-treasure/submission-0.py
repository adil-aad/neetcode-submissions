class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        q = deque()
        visited = set()

        def fill(r, c):
            if (r < 0 or r == rows or c < 0 or c == cols 
                or grid[r][c] == -1 or (r,c) in visited):
                return
            visited.add((r,c))
            q.append([r,c])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append([r,c])

        dist = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                fill(r, c + 1)
                fill(r, c - 1)
                fill(r + 1, c)
                fill(r - 1, c)

            dist += 1