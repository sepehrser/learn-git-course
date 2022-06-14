a, b, x = map(int,input().split())
tedad = 0

for i in range(1,a + 1):
    if a % i == 0:
        
        for j in range(1, b + 1):
            if (b % j == 0) and ((i + j) <= x):
                tedad += 1
            
        

#a, b, x = map(int,input().split())
tedad = 0

for i in range(1,a + 1):
    if a % i == 0:
        
        for j in range(1, b + 1):
            if (b % j == 0) and ((i + j) <= x):
                tedad += 1
            
        
print(tedad)
