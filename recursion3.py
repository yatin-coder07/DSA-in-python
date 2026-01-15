
n= int(input())
def sum(start, end):
    if start == end + 1:
        return 0
    return start + sum(start + 1 , end)

print(sum(1,n))