n = int(input())

def print_name(count, limit):
    if count == limit:
        return
    print("Yatin")
    print_name(count + 1, limit)

limit = min(n, 5)
print_name(0, limit)
