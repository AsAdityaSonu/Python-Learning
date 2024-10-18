import numpy as np

# --------------- a ---------------
arr = np.array([1,2,3,4,5,6])
rev = arr[::-1]
print("Reversed Array: ", rev)

# --------------- b ---------------
array1 = np.array([[1,2,3],[2,4,5],[1,2,3]])
flattened1 = array1.flatten()
print("Flattened Array: ", flattened1)
flattened2 = array1.ravel()
print("Flattened Array: ", flattened2)

# --------------- c ---------------
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[1,2], [3,4]])

areEqual = np.array_equal(arr1, arr2)
print(areEqual)

# --------------- d ---------------
x = np.array([1,2,3,4,5,1,2,1,1,1])
mostFrequent = np.bincount(x).argmax()
print("Most Frequent Value: ", mostFrequent)
indices = np.where(x == mostFrequent)[0]
print("Indices of Most Frequent Value: ", indices)

# --------------- e ---------------
gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')

totalSum = np.sum(gfg)
print("Sum of all elements:", totalSum)

rowSum = np.sum(gfg, axis=1)
print("Row-wise sum:", rowSum)

colSum = np.sum(gfg, axis=0)
print("Column-wise sum:", colSum)

# --------------- f ---------------
n_array = np.array([[55, 25, 15], [30, 44, 2], [11, 45, 77]])
diagonalSum = np.trace(n_array)
print("diagonal sum: ", diagonalSum)

eigenValue, eigenVector = np.linalg.eig(n_array)
print("Eigen Values: ", eigenValue)
print("Eigen Vector", eigenVector)

inverseMat = np.linalg.inv(n_array)
print("Inverse of matrix: \n", inverseMat)

determinant = np.linalg.det(n_array)
print("Determinant of matrix: ", determinant)

# --------------- g ---------------
p1 = np.array([[1,2],[2,3]])
q1 = np.array([[3,4], [6,7]])

result1 = np.dot(p1, q1)
print("multiplication of p and q:\n", result1)

covariance1 = np.cov(p1, q1, rowvar=False)
print("Covariance of p and q:\n", covariance1)

p2 = np.array([[1, 2], [2, 3], [4, 5]])
q2 = np.array([[4, 5, 1], [6, 7, 2]])

result2 = np.dot(p2, q2)
print("multiplication of p and q:\n", result2)

covariance2 = np.cov(p2, q2, rowvar=False)
print("Covariance of diff dimensions p and q:\n", covariance2)

# --------------- g ---------------
x = np.array([[2, 3, 4], [3, 2, 9]])
y = np.array([[1, 5, 0], [5, 10, 3]])

innerProduct = np.inner(x, y)
print("Inner product:\n", innerProduct)

outerProduct = np.outer(x, y)
print("Outer product:\n", outerProduct)

cartesianProduct = np.transpose([np.tile(x.flatten(), len(y.flatten())), np.repeat(y.flatten(), len(x.flatten()))])
print("Cartesian product:\n", cartesianProduct)
