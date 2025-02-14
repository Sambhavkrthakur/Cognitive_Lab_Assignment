
#Q.NO-1.a
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
arr_addition = arr + 2

print("Original Array:", arr)
print("Array after adding 2:", arr_addition)

#Q.NO-1.b
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
arr_multiplication = arr * 3

print("Original Array:", arr)
print("Array after multiplying by 3:", arr_multiplication)

#Q.NO-1.c
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
arr_division = arr / 2

print("Original Array:", arr)
print("Array after dividing by 2:", arr_division)

#Q.NO-2.a
import numpy as np

arr = np.array([1, 2, 3, 6, 4, 5])
arr_reversed = arr[::-1]

print("Original Array:", arr)
print("Reversed Array:", arr_reversed)

#Q.NO-2.b.i
import numpy as np
from collections import Counter

x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
counter = Counter(x)
most_frequent = counter.most_common(1)[0][0]
indices = np.where(x == most_frequent)[0]

print("Original Array:", x)
print("Most Frequent Value:", most_frequent)
print("Indices of Most Frequent Value:", indices)

#Q.NO-2.b.ii
import numpy as np
from collections import Counter

y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])
counter = Counter(y)
most_frequent = counter.most_common(1)[0][0]
indices = np.where(y == most_frequent)[0]

print("Original Array:", y)
print("Most Frequent Value:", most_frequent)
print("Indices of Most Frequent Value:", indices)

#Q.NO-3.a
import numpy as np

arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
element = arr[0, 1]

print("Original Array:")
print(arr)
print("Element at 1st row, 2nd column:", element)

#Q.NO-3.b
import numpy as np

arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
element = arr[2, 0]

print("Original Array:")
print(arr)
print("Element at 3rd row, 1st column:", element)

#Q.NO-4
import numpy as np

Your_Name = np.linspace(10, 100, 25)

print("Array:", Your_Name)
print("Dimensions:", Your_Name.ndim)
print("Shape:", Your_Name.shape)
print("Total Elements:", Your_Name.size)
print("Data Type:", Your_Name.dtype)
print("Total Bytes Consumed:", Your_Name.nbytes)

transpose_array = Your_Name.reshape(25, 1)
print("Transpose using reshape:\n", transpose_array)
print("Transpose using T attribute:\n", Your_Name.T)

#Q.NO-5
import numpy as np

ucs420_yourname = np.array([[10, 20, 30, 40], 
                            [50, 60, 70, 80], 
                            [90, 15, 20, 35]])

mean_value = np.mean(ucs420_yourname)
median_value = np.median(ucs420_yourname)
max_value = np.max(ucs420_yourname)
min_value = np.min(ucs420_yourname)
unique_elements = np.unique(ucs420_yourname)

reshaped_ucs420_yourname = ucs420_yourname.reshape(4, 3)
resized_ucs420_yourname = np.resize(ucs420_yourname, (2, 3))

print(ucs420_yourname)
print("Mean:", mean_value)
print("Median:", median_value)
print("Max:", max_value)
print("Min:", min_value)
print("Unique Elements:", unique_elements)
print(reshaped_ucs420_yourname)
print(resized_ucs420_yourname)
