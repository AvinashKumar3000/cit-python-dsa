# topics

.append()
.extend()
.sort()
sorted()
li.copy()

```python

> > > li1 = [10,20,30]
> > > li2 = [ *li1 ] # unpacking using \*
> > > li2
> > > [10, 20, 30]
> > > li1
> > > [10, 20, 30]
> > > li1[0] = 999
> > > li1
> > > [999, 20, 30]
> > > li2
> > > [10, 20, 30]
```
---

```python
#     -9  -8  -7  -6  -5  -4  -3  -2  -1
li = [10, 20, 30, 40, 50, 60, 70, 80, 90]
#      0   1   2   3   4   5   6   7   8

>>> li[-1: -3]
[]
>>> li[-1: -3: -1]
[90, 80]
>>> li[100:200]
[]
>>> li[::0]
ValueError: slice step cannot be zero
>>> li[ :-7:1]
[10, 20]
>>> li[ :-7:-1]
[90, 80, 70, 60, 50, 40]

# list comprehension

res = []
for i in range(5):
	res.append(i*2)

res = [ i*2 for i in range(5) ]
res = [ i*10 for i in range(5,10) ]

li = [10,20,30,40,50]
res = [ x//10 for x in li ]

name = "tom"
res = [ ch for ch in name ]
# [ 't','o','m']

li = [1,2,3,4,5,6]
res = []
for x in li:
	if x%2!=0:
	   res.append(x)

res = [ x for x in li if x%2!=0 ]
# [1,3,5]

# 3*3 matrix with value 0
matrix = []
for _ in range(3):
  row = []
  for _ in range(3):
     row.append(0)
  matrix.append(row)

r = 3
c = 3
matrix = [ [ 0 for _ in range(c) ] for _ in range(r) ]
```
