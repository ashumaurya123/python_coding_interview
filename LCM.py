a=int(input("ENTER FIRST NUMBER"))
b=int(input("ENTER SECOND NUMBER"))


maxnum = max(a, b)


while(True):

    if ( maxnum%a == 0 and maxnum%b == 0):
        lcm = maxnum

        break
    maxnum = maxnum+1

print(maxnum)


