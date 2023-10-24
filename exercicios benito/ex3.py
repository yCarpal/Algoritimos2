n = 100000000000

count = 0
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
        count += 1

if count == 2:
    print("Número primo")