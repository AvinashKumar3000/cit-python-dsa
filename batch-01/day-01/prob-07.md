# medium - LC_73 set matrix zeros

```python
class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        
        first_row = False
        first_col = False

        for i in range(m):
            if matrix[i][0] == 0:
                first_col = True
                break

        for j in range(n):
            if matrix[0][j] == 0:
                first_row = True
                break

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row == True:
            for j in range(n):
                matrix[0][j] = 0
        if first_col == True:
            for i in range(m):
                matrix[i][0] = 0
```

## another solution

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        ic = set()
        jc = set()
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    ic.add(i)
                    jc.add(j)
        for i in range(r):
            for j in range(c):
                if i in ic or j in jc:
                    matrix[i][j] = 0
                
```
