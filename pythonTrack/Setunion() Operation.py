
n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
ans = a.union(b)
count = 0
for i in ans:
    count = count + 1
print (count)
