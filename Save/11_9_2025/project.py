import random

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "`~!@$#$%^&*()_+-=<>?,./:;"

def isprime(n):
    if (n<2): return False
    for i in range(1, int((n+1)**0.5)):
        if (n%i==0):
            return False
    else:
        return True

pass_lenght = int(input("Enter password lenght: "))
count = int(input("Enter number of passwords: "))
print("Your passwords lenght")
for i in range(count):
    password = ""
    for j in range(pass_lenght):
        if (isprime(j)):
            password += random.choice(letters.upper())
        elif (isprime(int(j**0.5))):
            password += random.choice(numbers)
        elif (j%6==0):
            password += random.choice(symbols)
        else:
            password += random.choice(letters)
    print(password)