n = int(input())

def decrement(start):
    if start == 0:
        return
    print(start)
    decrement(start - 1)

decrement(n)
