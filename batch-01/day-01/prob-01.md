# rotate image 

## notes

- n-i-1   to reverse access

```python
# print array in reverse

li = [10,20,30,40]
n = len(li)
for i in range(n):
	print(li[n-i-1])
```



## solution 1

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        temp = [ [ 0 for _ in range(n) ] for _ in range(n) ]

        for i in range(n):
        	for j in range(n):
        		temp[i][j] = matrix[i][j]

        print(temp)

        for i in range(n):
        	for j in range(n):
        		matrix[i][j] = temp[n-j-1][i]
      	
        print(matrix)
```


## solution 2

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
        	for j in range(n):
        		if i<=j:
        			matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for i in range(n):
        		matrix[i] = matrix[i][::-1]

```


## solution 3 

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
        	for j in range(n):
        		if i<=j:
        			matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for i in range(n):
        	for j in range(n//2):
        		matrix[i][n-j-1],matrix[i][j] = matrix[i][j], matrix[i][n-j=1]

```
