def hanoi(n):
    if n == 0:
        return 0
    return 2 * hanoi(n-1)+1
print(hanoi(1))
print(hanoi(2))
n = int(input("Enter a number "))
print(hanoi(n))