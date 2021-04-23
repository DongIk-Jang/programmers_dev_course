import itertools
from math import sqrt

def solution(n):
    l = []
    for i in range(2, n):
        temp = 1
        for j in range(2, int(sqrt(i)+1)):
            if i % j == 0:
                temp = 0
        if temp == 1:
            l.append(i)
    return l

print(solution(19))
a = itertools.combinations(solution(19), 3)
print(list(a))
for i, j, k in a:
    if i+j+k == n:
        answer += 1


            






# def find_prime_number(x):
#     temp = True
#     if x <= 1:
#         return False
#     if x % 2 == 0 and x > 2:
#         return False
#     elif x == 2:
#         return True
#     elif x > 2:
#         for i in range(2, int(sqrt(x))+1):
#             if x % i == 0:
#                 temp = False
#         return temp
    
# def all_numbers(numbers):
#     all_number = []
#     for i in range(2, len(numbers)+1):
#         temp = list(map(''.join, permutations(list(numbers), i)))
#         all_number += list(map(int, temp))
#     return all_number

# def solution(numbers):
#     data_list = all_numbers(numbers)
#     temp = []
#     for j in list(map(int, list(numbers))):
#         if find_prime_number(j) == True:
#             temp.append(j)
#     for i in data_list:
#         if find_prime_number(i) == True:
#             temp.append(i)
#     temp = set(temp)
#     return len(temp)