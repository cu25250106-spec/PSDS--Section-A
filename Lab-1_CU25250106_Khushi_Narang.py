'''import numpy as np

arr = np.array([1, 2, 3])
arr = np.append(arr, 4)
print("After push:", arr)
arr = np.delete(arr, -1)
print("After pop:", arr)

arr = np.array([10, 20, 30, 40, 50])

while len(arr) > 0:
    popelement = arr[-1]
    print("Popping this item:", popelement)
    arr = np.delete(arr, -1)
    print("Array after pop:", arr)'''



# Enqueue and Dequeue Operation
import numpy as np

queue = np.array([10, 20, 30])
print("Original queue:", queue)

queue = np.append(queue, 40)
print("After enqueue:", queue)

dequeued_item = queue[0]
print("Dequeued item:", dequeued_item)

queue = np.delete(queue, 0)
print("After dequeue:", queue)
