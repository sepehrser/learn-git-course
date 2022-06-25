n, x = input().split()
for i in range(int(n)):
    a, b = input().split()
    if a == x:
        x = b
    elif b == x:
        x = a 

print(x)