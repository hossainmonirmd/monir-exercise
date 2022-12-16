noofrep = int(input())
start = 1
while start <= noofrep:
    num1 = int(input())
    num2 = int(input())
    if num1 < num2:
        print("positive")
    elif num1 > num2:
        print("negative")
    elif num1 == num2:
        print("good")
    start += 1
