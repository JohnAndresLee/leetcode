# 哈希表的创建

## set

```python
>>> s = set([1, 2, 3])
>>> s
{1, 2, 3}

>>> s = set([1, 1, 2, 2, 3, 3])
>>> s
{1, 2, 3}

# set中添加元素
>>> s.add(4)
>>> s
{1, 2, 3, 4}
>>> s.add(4)
>>> s
{1, 2, 3, 4}

# set中删除元素
>>> s.remove(4)
>>> s
{1, 2, 3}

# 集合的操作
>>> s1 = set([1, 2, 3])
>>> s2 = set([2, 3, 4])
>>> s1 & s2
{2, 3}
>>> s1 | s2
{1, 2, 3, 4}

```



## dict

```python
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]

>>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
>>> d['Michael']
95

# 查询元素是否在字典中
>>> 'Thomas' in d
False

# 二是通过dict提供的get()方法，如果key不存在，可以返回None，（注意：返回None的时候Python的交互环境不显示结果）。或者自己指定的value：
>>> d.get('Thomas')
>>> d.get('Thomas', -1)
-1
```

