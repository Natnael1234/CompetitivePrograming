# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
set_country = set()
for i in range(n):
    set_country.add(input())
print(len(set_country))
