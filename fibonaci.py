# print till nth term fibonacci series
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181


a = 0
b = 1
c = 0
n= int(input("how much term you needed in fibonacci "))
for i in range(0, n):
    print(c,end=" ")
    a = b
    b = c
    c = a+b



# print till nth even  term wants in fibonacci series

# a = 0
# b = 1
# c = 0
# n= int(input("how much even th term you wants in fibonacci "))
# for i in range(0, n):
#     if i%2 ==0:
#         print(c,end=" ")
#     a = b
#     b = c
#     c = a+b
