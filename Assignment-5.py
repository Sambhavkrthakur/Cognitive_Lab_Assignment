
#Q.NO-1.i
import numpy as np

gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')
sum_elements = np.sum(gfg)

print("Sum of all elements:", sum_elements)

#Q.NO-1.ii
import numpy as np

gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')
sum_elements = np.sum(gfg)
sum_row_wise = np.sum(gfg, axis=1)

print("Sum of all elements:", sum_elements)
print("Sum of all elements row-wise:", sum_row_wise)

#Q.NO-1.iii
import numpy as np

gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')
sum_column_wise = np.sum(gfg, axis=0)

print("Sum of all elements column-wise:", sum_column_wise)

#Q.NO-2.a.i
import numpy as np

array = np.array([10, 52, 62, 16, 16, 54, 453])
sorted_array = np.sort(array)

print("Sorted array:", sorted_array)

#Q.NO-2.ii
import numpy as np

array = np.array([10, 52, 62, 16, 16, 54, 453])
sorted_indices = np.argsort(array)

print("Indices of sorted array:", sorted_indices)

#Q.NO-2.iii
import numpy as np

array = np.array([10, 52, 62, 16, 16, 54, 453])
four_smallest_elements = np.sort(array)[:4]

print("Four smallest elements:", four_smallest_elements)

#Q.NO-2.iv
import numpy as np

array = np.array([10, 52, 62, 16, 16, 54, 453])
five_largest_elements = np.sort(array)[-5:]

print("Five largest elements:", five_largest_elements)

#Q.NO-2.b.i
import numpy as np

array = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])
integer_elements = array[array == array.astype(int)]

print("Integer elements only:", integer_elements)

#Q.NO-2.b.ii
import numpy as np

array = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])
float_elements = array[array != array.astype(int)]

print("Float elements only:", float_elements)

#Q.NO-3.a
import numpy as np

initials = ['F', 'L']
ascii_sum = sum(ord(char) for char in initials)

sales = np.array([ascii_sum, ascii_sum + 50, ascii_sum + 100, ascii_sum + 150, ascii_sum + 200])

print("Sales dataset:", sales)

#Q.NO-3.b
import numpy as np

initials = ['F', 'L']
ascii_sum = sum(ord(char) for char in initials)

sales = np.array([ascii_sum, ascii_sum + 50, ascii_sum + 100, ascii_sum + 150, ascii_sum + 200])

tax_rate = ((ascii_sum % 5) + 5) / 100

taxed_sales = sales * (1 + tax_rate)

print("Personalized tax rate:", tax_rate)
print("Sales after tax:", taxed_sales)

#Q.NO-3.c
import numpy as np

initials = ['F', 'L']
ascii_sum = sum(ord(char) for char in initials)

sales = np.array([ascii_sum, ascii_sum + 50, ascii_sum + 100, ascii_sum + 150, ascii_sum + 200])

tax_rate = ((ascii_sum % 5) + 5) / 100

taxed_sales = sales * (1 + tax_rate)

discounted_sales = np.where(sales < ascii_sum + 100, sales * 0.95, sales * 0.90)

print("Personalized tax rate:", tax_rate)
print("Sales after tax:", taxed_sales)
print("Sales after discount:", discounted_sales)

#Q.NO-3.d
import numpy as np

initials = ['F', 'L']
ascii_sum = sum(ord(char) for char in initials)

sales = np.array([ascii_sum, ascii_sum + 50, ascii_sum + 100, ascii_sum + 150, ascii_sum + 200])

tax_rate = ((ascii_sum % 5) + 5) / 100

taxed_sales = sales * (1 + tax_rate)

discounted_sales = np.where(sales < ascii_sum + 100, sales * 0.95, sales * 0.90)

weekly_sales = np.vstack([sales] * 3)
weekly_multiplier = np.array([1.00, 1.02, 1.04]).reshape(3, 1)
weekly_sales_adjusted = weekly_sales * weekly_multiplier

print("Personalized tax rate:", tax_rate)
print("Sales after tax:", taxed_sales)
print("Sales after discount:", discounted_sales)
print("Weekly sales adjusted:", weekly_sales_adjusted)
