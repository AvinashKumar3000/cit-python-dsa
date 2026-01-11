# prob-02 LC_994

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]):
        if len(grid) == 0:
            return -1

        fresh = 0
        time = -1
        rows = len(grid)
        cols = len(grid[0])
        directions = [
            (-1,0),
            (0,-1),
            (1,0),
            (0,1)
        ]
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append([i,j])

        if fresh == 0:
            return 0

        while len(q) != 0:
            size = len(q)

            for _ in range(size):
                x,y = q.popleft()
                for dx,dy in directions:
                    nx,ny = x+dx, y+dy
                    if 0 <= nx < rows and 0 <= ny < cols and fresh > 0:
                        if grid[nx][ny] == 1:
                            grid[nx][ny] = 2
                            q.append([nx,ny])
                            fresh -= 1
            time += 1

        if fresh == 0:
            return time
        else:
            return -1