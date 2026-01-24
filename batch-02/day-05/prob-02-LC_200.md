# LC_200 No of islands 

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        land = 0
        directions = [
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        ]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    land += 1
                    stack = [(i,j)]
                    grid[i][j] = "0"

                    while len(stack) != 0:
                        x,y = stack.pop()
                        for dx,dy in directions:
                            nx,ny = x+dx, y+dy
                            if 0 <= nx < rows and 0 <= ny < cols:
                                if grid[nx][ny] == "1":
                                    stack.append( (nx,ny) )
                                    grid[nx][ny] = "0"
        return land
```

```python
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            # base cases
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] == '0':
                return

            # mark current land as visited (sink it)
            grid[r][c] = '0'

            # explore all 4 directions
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)

        return islands

```
