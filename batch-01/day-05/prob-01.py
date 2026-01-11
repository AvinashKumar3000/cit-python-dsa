# LC_200
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