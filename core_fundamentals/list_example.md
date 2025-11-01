# Python Lists – Examples from `list_example.py`

This document explains the Python list features demonstrated in `list_example.py` with short examples and outputs.

## Create a list
```python
users = ["user1", "user2", "user3"]
print(users)  # ['user1', 'user2', 'user3']
```

## Append an item (add to end)
```python
users.append("user4")
print(users)  # ['user1', 'user2', 'user3', 'user4']
```

## Insert at an index
```python
users.insert(4, "user5")  # index 4 is after current last item
print(users)  # ['user1', 'user2', 'user3', 'user4', 'user5']
```

## Delete by index
```python
del users[0]
print(users)  # ['user2', 'user3', 'user4', 'user5']
```

## Reverse in place
```python
users.reverse()
print(users)  # ['user5', 'user4', 'user3', 'user2']
```

## Get length
```python
print(len(users))  # 4
```

## Iterate items
```python
for user in users:
    print(user)
# user5
# user4
# user3
# user2
```

## Iterate a numeric range (not a list, but common with loops)
```python
for i in range(1, 5):
    print(i)
# 1
# 2
# 3
# 4
```

## Numeric lists and aggregations
```python
numbers = [1, 2, 3, 4, 5]
print(f"Max number is {max(numbers)}")  # Max number is 5
print(f"Min number is {min(numbers)}")  # Min number is 1
```

## List comprehension (transform each element)
```python
x2Numbers = [value * 2 for value in numbers]
print(x2Numbers)  # [2, 4, 6, 8, 10]
```

## Slicing (sublist)
```python
# Slice from index 1 up to (but not including) index 3
slicedNumbers = numbers[1:3]
print(slicedNumbers)  # [2, 3]
```

---

## Quick cheatsheet
- **Create**: `lst = [a, b, c]`
- **Append**: `lst.append(x)`
- **Insert**: `lst.insert(i, x)`
- **Delete by index**: `del lst[i]`
- **Reverse**: `lst.reverse()`
- **Length**: `len(lst)`
- **Iterate**: `for item in lst: ...`
- **Range loop**: `for i in range(start, stop): ...`
- **Max/Min**: `max(lst)`, `min(lst)` (works for comparable elements)
- **List comprehension**: `[expr for item in lst]`
- **Slice**: `lst[start:stop]` (stop is exclusive)
