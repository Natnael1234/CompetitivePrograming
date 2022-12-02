n,m = map(int, input().split())
array = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

happiness = 0 
for i in array:
    if i in a:
        happiness += 1
    elif i in b:
        happiness -= 1
    else:
        pass
print(happiness)
