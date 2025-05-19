# Greatest Common Divisor (GCD) of two integers n and m is the largest integer which divides both of n and m. It can by computed using recursive division Relatively prime integers are the integers whose GCD is 1. Using the GCD(n,m) function
# as the building block, write a function rel_prime(n) which will compute the probability
# that two randomly chosen integers lesser than a given integer n will be relatively prime.
# User will call this function and give n as input

def gcd (x,y):
    if x % y == 0:
        return y
    else:
        return (gcd (y, x % y))

def relative_prime(p):
    Total_pairs = 0
    relative_primes = 0
    for i in range(0,p+1):
        for j in range(i + 1,p+1):
            result = gcd(i,j)
            print(i,j)
            print(result)
            if result == 1:
                Total_pairs  += 1
                relative_primes += 1
            else:
                Total_pairs += 1
    print("Total pairs are ",Total_pairs)
    print("Realtive Primes are :",relative_primes)
    probability = relative_primes /Total_pairs
    print("Probability  is :", probability)
    
relative_prime(9)