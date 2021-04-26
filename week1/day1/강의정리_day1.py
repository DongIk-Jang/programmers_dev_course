# test_list = [{1 : 'gfg', 2 : 'best'}, {3 : 'for', 4 : 'geeks'}]

# res = dict()
# res.update(test_list[0].values(), )
# print(res)


# for sub in test_list:
#     print(sub)
#     print(sub.values())
#     res.update((sub.values(), ))

# print(res)

# test_list = [{1 : 'gfg', 2 : 'best'}, {3 : 'for', 4 : 'geeks'}]
  
# # printing original list
# print("The original list is : " + str(test_list))
  
# # Value Dictionary from Record List
# # Using zip() + iter()
# res = dict()
# for sub in test_list:
#     itr = iter(sub.values())
#     res.update(dict(zip(itr, itr)))
  
# # printing result 
# print("The values dictionary is : " + str(res)) 

# def iterative_fibo(x):
#     if x == 1:
#         return 0
#     if x == 2:
#         return 1
#     n1 = 0
#     n2 = 1
#     for i in range(1, x):
#         n1, n2 = n2, (n1+n2)
#     return n1

# print(iterative_fibo(5))

# a = 1
# b = 1

# if a == 1 and b == 1:
#     print("a=1, b=1")
# else:
#     print("else")
#     if a == 1 and b >1:
#         print("a=1, b>1")
#     elif a >= 1 or b < 2:
#         print("?")

k = [1,2,3,None, None, None]
i = 0
while k[i]:
    print(k[i])
    i += 1