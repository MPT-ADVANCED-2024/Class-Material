# Delete from Array

```python
def delete_from_array(arr: list[int], idx: int) -> None:
    for i in range(idx, len(arr) - 1):
        arr[i] = arr[i + 1]
    arr.pop()  # End the function with popping the last element
```
