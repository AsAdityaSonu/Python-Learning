import numpy as np

array1 = np.array([10, 52, 62, 16, 16, 54, 453])
sortedArray = np.sort(array1)
sortedIndices = np.argsort(array1)
smallestElements = np.partition(array1, 4)[:4]
largestElements = np.partition(array1, -5)[-5:]

array2 = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])
integerElements = array2[array2 == array2.astype(int)]
floatElements = array2[array2 != array2.astype(int)]

print("Sorted array:", sortedArray)
print("Indices of sorted array:", sortedIndices)
print("4 smallest elements:", smallestElements)
print("5 largest elements:", largestElements)
print("Integer elements:", integerElements)
print("Float elements:", floatElements)
