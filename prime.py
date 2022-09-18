a=int(input())
b=int(input())

for i in range(a,b+1):
    for j in range(2, i+1):
        if ((i%j)==0):
            break


    if(i == j):
        print("no. is prime {}".format(i))
