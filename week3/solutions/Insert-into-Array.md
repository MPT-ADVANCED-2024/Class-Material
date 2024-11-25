# Insert into Array

```python
def insert_into_array(arr: list[int], idx: int, val: int) -> None:
    arr.append(0) # Start with creating an new empty space at the end of the array
    for i in reversed(range(idx + 1, len(arr))):
        arr[i] = arr[i - 1]
    arr[idx] = val
```
