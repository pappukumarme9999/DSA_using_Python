# 1. Two-Pointer Swapping
def reverse_in_place(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

# 2. Index Swapping (Negative Indexing)
def reverse_in_place(lst):
    for i in range(len(lst) // 2):
        lst[i], lst[-i - 1] = lst[-i - 1], lst[i]
    return lst

# 3. Index Swapping (Explicit Calculation)
def reverse_in_place(lst):
    for i in range(len(lst) // 2):
        lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
    return lst


# Not Truly In-Place (Creates Intermediate Structures or Slices)
# These **reassign `lst[:]`**, so they technically mutate the original list but rely on **intermediate objects**, hence not true in-place in low-level terms.
# 4. Recursion with Slicing
def reverse_in_place(lst):
    if len(lst) <= 1:
        return lst
    lst[0], lst[-1] = lst[-1], lst[0]
    return reverse_in_place(lst[1:-1])


# Out-of-Place (Normal Reversal Techniques)
# These **create new lists** (or use stack-like/functional operations) and assign them back to the original list using `lst[:] = ...`. Though they appear in-place syntactically, they are logically not.
# 5. Using a Stack (List)
def reverse_in_place(lst):
    stack = []
    for item in lst:
        stack.append(item)
    for i in range(len(lst)):
        lst[i] = stack.pop()
    return lst

# 6. Using a Queue (FIFO via list)
def reverse_in_place(lst):
    queue = []
    for item in lst:
        queue.append(item)
    for i in range(len(lst)):
        lst[i] = queue.pop(0)
    return lst

# 7. Using a Deque (Efficient Pop from End)
def reverse_in_place(lst):
    from collections import deque
    queue = deque(lst)
    for i in range(len(lst)):
        lst[i] = queue.pop()
    return lst

# 8. List Comprehension (Backwards Indexing)
def reverse_in_place(lst):
    lst[:] = [lst[i] for i in range(len(lst) - 1, -1, -1)]
    return lst

# 9. Generator Expression
def reverse_in_place(lst):
    lst[:] = (lst[i] for i in range(len(lst) - 1, -1, -1))
    return lst

# 10. Lambda with `map()`
def reverse_in_place(lst):
    lst[:] = list(map(lambda x: lst[len(lst) - 1 - x], range(len(lst))))
    return lst

# 11. `filter()` with Generator
def reverse_in_place(lst):
    lst[:] = list(filter(lambda x: True, (lst[len(lst) - 1 - i] for i in range(len(lst)))))
    return lst

# 12. `reduce()` Function
from functools import reduce
def reverse_in_place(lst):
    lst[:] = reduce(lambda x, y: [y] + x, lst, [])
    return lst

# 13. Using `zip()` —  Not functionally correct for reversal
def reverse_in_place(lst):
    lst[:] = list(zip(*[iter(lst)] * len(lst)))
    return lst

# 14. List Comprehension with Step
def reverse_in_place(lst):
    lst[:] = [lst[i] for i in range(len(lst) - 1, -1, -1)]
    return lst

# 15. Slicing with Negative Step
def reverse_in_place(lst):
    lst[:] = lst[::-1]
    return lst


# 16. Using `reversed()` Function
def reverse_in_place(lst):
    lst[:] = list(reversed(lst))
    return lst
