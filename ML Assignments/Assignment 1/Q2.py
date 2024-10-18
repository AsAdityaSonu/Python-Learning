import numpy as np

# --------------- a ---------------
array = np.array([[1, -2, 3], [-4, 5, -6]])

absolute_values = np.abs(array)
print("Element-wise absolute values:\n", absolute_values)

# --------------- b ---------------
flattenedArray = array.flatten()

percentile_25 = np.percentile(flattenedArray, 25)
percentile_50 = np.percentile(flattenedArray, 50)
percentile_75 = np.percentile(flattenedArray, 75)

print("25th percentile:", percentile_25)
print("50th percentile:", percentile_50)
print("75th percentile:", percentile_75)

# --------------- c ---------------
percentile_25Col = np.percentile(array, 25, axis=0)
percentile_50Col = np.percentile(array, 50, axis=0)
percentile_75Col = np.percentile(array, 75, axis=0)

print("25th percentile col:", percentile_25Col)
print("50th percentile col:", percentile_50Col)
print("75th percentile col:", percentile_75Col)

# --------------- d ---------------
# Percentiles for each row
percentile_25Row = np.percentile(array, 25, axis=1)
percentile_50Row = np.percentile(array, 50, axis=1)
percentile_75Row = np.percentile(array, 75, axis=1)

print("25th percentile row:", percentile_25Row)
print("50th percentile row:", percentile_50Row)
print("75th percentile row:", percentile_75Row)

# --------------- e ---------------
mean = np.mean(flattenedArray)
median = np.median(flattenedArray)
std = np.std(flattenedArray)

print("Mean:", mean)
print("Median:", median)
print("SD:", std)

# --------------- f ---------------
meanCol = np.mean(array, axis=0)
medianCol = np.median(array, axis=0)
stdCol = np.std(array, axis=0)

print("Mean column:", meanCol)
print("Median column:", medianCol)
print("SD column:", stdCol)

meanRow = np.mean(array, axis=1)
medianRow = np.median(array, axis=1)
stdRow = np.std(array, axis=1)

print("Mean row:", meanRow)
print("Median row:", medianRow)
print("SD row:", stdRow)

# --------------- g ---------------
a = np.array([-1.8, -1.6, -0.5, 0.5, 1.6, 1.8, 3.0])

# Floor
floorValues = np.floor(a)
print("Floor :", floorValues)

# Ceiling 
ceilingValues = np.ceil(a)
print("Ceiling :", ceilingValues)

# Truncated 
truncatedValues = np.trunc(a)
print("Truncated :", truncatedValues)

# Rounded 
roundedValues = np.round(a)
print("Rounded :", roundedValues)
