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

def idk(n):
    t = int(n**0.5)
    if (n==t*t): return isprime(t)
    return False

def check(s):
    t = s.lower()
    if (t=="yes" or t=="true" or t=="no" or t=="false"):
        return True
    else:
        return False

valid = False
pass_count = "#"
while (not valid):
    strict_requirement = input("All Requirement: ")
    if (check(strict_requirement)):
        if (strict_requirement=="yes" or strict_requirement=="true"):
            strict_requirement = True
        else:
            strict_requirement = False
    else:
        print("Invalid All Requirement input!")
        continue
    while (True):
        pass_length = input("Enter password length: ")
        if (pass_length.isdigit()):
            pass_length = int(pass_length)
            if (pass_length>0): break
            print("Invalid password length input!")
        print("Invalid password length input!")
    if (strict_requirement and pass_length<4):
        print("Password must have atleast 4 characters when All requirement is True")
        continue
    while (True):
        pass_count = input("Enter passwords count: ")
        if (pass_count.isdigit()):
            pass_count = int(pass_count)
            if (pass_count>0):
                valid = True
                break
            print("Invalid password count!")
        print("Invalid password count!")
for i in range(pass_count):
    password = []
    lenght = pass_length
    if (strict_requirement):
        password.append(random.choice(letters.upper()))
        password.append(random.choice(letters))
        password.append(random.choice(numbers))
        password.append(random.choice(symbols))
        lenght -= 4
    for j in range(lenght):
        if (isprime(j)):
            password.append(random.choice(letters.upper()))
        elif (idk(j)):
            password.append(random.choice(numbers))
        elif (j%6==0):
            password.append(random.choice(symbols))
        else:
            password.append(random.choice(letters))
    random.shuffle(password)
    print(''.join([x for x in password]))