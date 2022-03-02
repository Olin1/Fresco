num=21
val=1
def primegenerator(num, val):
    # Write your code here
    primes = []
    for i in range(2, num):
        for j in range(2, int(i / 2) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)
        
    for i in range(1 - val, len(primes), 2):
        yield primes[i]
print(primegenerator(num,val))