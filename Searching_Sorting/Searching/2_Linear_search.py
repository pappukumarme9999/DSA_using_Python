'''

Linear search or sequential search
    -> checks each element in a list one by one until the desired element is found or the list ends.
------------------------------------------------------------------------------------------------------------
Time Complexity: O(n) - Each element is checked once.

Space Complexity: O(1) - Only a constant amount of extra space is used.
Best Case: O(1) - The target element is the first element.
Average Case: O(n/2) - On average, the target element is found halfway through the list.
Worst Case: O(n) - The target element is the last element or not present.
------------------------------------------------------------------------------------------------------------
No sorting required
brute force approach is used
------------------------------------------------------------------------------------------------------------

Applications
1. Small Data Sets
Linear search is efficient for small-sized data sets where the overhead of more complex algorithms is not justified.

2. Unsorted or Randomly Ordered Lists
Linear search is suitable for unsorted lists where no assumptions can be made about the order of elements.

3. Linked Lists
In linked lists, where elements are not stored in contiguous memory locations, linear search is often the only option due to the lack of random access.

4. Simple Search Operations
When search operations are infrequent or performance is not a critical concern, linear search provides a straightforward solution.

5. Finding a Single Instance
When searching for a specific item that is expected to occur only once in the list, linear search is straightforward and effective.

6. Preliminary Check
In some cases, linear search is used as a preliminary check before performing more complex operations on the data set.

Example Use Cases
Finding a Contact in a List: Searching for a contact in a list of names stored in an address book application.
Checking Attendance: Verifying the presence of a student's name in an attendance list.
Basic Data Validation: Checking if an input value exists within a predefined set of valid values.
Simple Lookup Operations: Searching for a product in a small inventory list in a retail application.

'''

def linear_search(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return -1
    
arr = [2,5,6,9,11,15,8,4,10,3,1,77,88,34,76,21,78,90,67,44,5,67]
print(linear_search(arr, 2))
print(linear_search(arr, 5))        # first occurance

result = linear_search(arr, 888)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found")

