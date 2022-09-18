number = int(input("enter some number:"))


def check_armstrong(num):

    order = len(str(num))
    result = 0
    original = num
    while num > 0:
        digit = num % 10
        result = result + (digit ** order)
        num = num // 10
    if original == result:
        return True
    return False


if check_armstrong(number):
    print("THIS IS ARMSTRONG")
else:
    print("THIS IS NOT ARMSTRONG")