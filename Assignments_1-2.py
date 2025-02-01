#QNO:1.a
L = [10, 20, 30, 40, 50, 60, 70, 80]
L.append(200)
L.append(300)
print(L)

#QNO:1.b
L = [10, 20, 30, 40, 50, 60, 70, 80, 200, 300]
L.remove(10)
L.remove(30)
print(L)

#QNO:1.c
L = [20, 40, 50, 60, 70, 80, 200, 300]
L.sort()
print(L)

#QNO:1.d
L = [20, 40, 50, 60, 70, 80, 200, 300]
L.sort(reverse=True)
print(L)

#QNO:2.a
scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)

highest_score = max(scores)
index_of_highest = scores.index(highest_score)

print("Highest Score:", highest_score)
print("Index of Highest Score:", index_of_highest)

#QNO:2.b
scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)

lowest_score = min(scores)
count_of_lowest = scores.count(lowest_score)

print("Lowest Score:", lowest_score)
print("Count of Lowest Score:", count_of_lowest)

#QNO:2.c
scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)

reversed_scores = list(scores[::-1])

print("Reversed Scores as List:", reversed_scores)

#QNO:2.d
scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)

user_input = 76  # Replace this with input() to take user input

if user_input in scores:
    index_of_score = scores.index(user_input)
    print(f"Score {user_input} is present at index:", index_of_score)
else:
    print(f"Score {user_input} is not present in the tuple.")

#QNO:3.a
import random

random_numbers = [random.randint(100, 900) for _ in range(100)]
odd_numbers = [num for num in random_numbers if num % 2 != 0]

print("Odd Numbers:", odd_numbers)
print("Count of Odd Numbers:", len(odd_numbers))

#QNO:3.b
import random

random_numbers = [random.randint(100, 900) for _ in range(100)]
even_numbers = [num for num in random_numbers if num % 2 == 0]

print("Even Numbers:", even_numbers)
print("Count of Even Numbers:", len(even_numbers))

#QNO:3.c
import random

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

random_numbers = [random.randint(100, 900) for _ in range(100)]
prime_numbers = [num for num in random_numbers if is_prime(num)]

print("Prime Numbers:", prime_numbers)
print("Count of Prime Numbers:", len(prime_numbers))

#QNO:4.a
A = {34, 56, 78, 90}
B = {78, 45, 90, 23}

unique_scores = A.union(B)

print("Unique Scores (Union of A and B):", unique_scores)

#QNO:4.b
A = {34, 56, 78, 90}
B = {78, 45, 90, 23}

common_scores = A.intersection(B)

print("Common Scores (Intersection of A and B):", common_scores)

#QNO:4.c
A = {34, 56, 78, 90}
B = {78, 45, 90, 23}

exclusive_scores = A.symmetric_difference(B)

print("Exclusive Scores (Symmetric Difference of A and B):", exclusive_scores)

#QNO:4.d
A = {34, 56, 78, 90}
B = {78, 45, 90, 23}

is_subset = A.issubset(B)
is_superset = B.issuperset(A)

print("Team A's scores are a subset of Team B:", is_subset)
print("Team B's scores are a superset of Team A:", is_superset)

#QNO:4.e
A = {34, 56, 78, 90}
user_input = 78  # Replace this with input() to take user input

if user_input in A:
    A.remove(user_input)
    print("Updated Set A:", A)
else:
    print(f"Score {user_input} is not present in Set A.")

#QNO:5.a
my_dict = {'name': 'John', 'city': 'New York', 'age': 30}

# Rename key 'city' to 'location'
if 'city' in my_dict:
    my_dict['location'] = my_dict.pop('city')

print("Updated Dictionary:", my_dict)