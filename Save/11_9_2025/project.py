import random

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "`~!@$#$%^&*()_+-=<>?,./:;"

#kiem tra so nguyen to
def isprime(n):
    if (n<2): return False
    for i in range(1, int((n+1)**0.5)):
        if (n%i==0):
            return False
    else:
        return True

#kiem tra so chi co 3 uoc
def idk(n):
    t = int(n**0.5)
    if (n==t*t): return isprime(t)
    return False

#kiem tra All Requirement input
def check(s):
    if (s=="yes" or s=="true" or s=="y" or s=="no" or s=="false" or s=="n"):
        return True
    else:
        return False

valid = False
pass_count = "#"
#kiem tra dau vao input den khi nao hop le thi dung
while (not valid):
    strict_requirement = input("All Requirement: ")
    t = strict_requirement.lower()
    if (check(t)): #kiem tra All Requirement input
        #nhap lai All Requirement input khi ko hop le
        if (t=="yes" or t=="true" or t=='y'):
            strict_requirement = True
        else:
            strict_requirement = False
    else:
        print("Invalid All Requirement input!")
        continue
    while (True):
        #Kiem tra password length input
        #nhap lai password length khi ko hop le
        pass_length = input("Enter password length: ")
        if (pass_length.isdigit()):
            pass_length = int(pass_length)
            if (pass_length>0): break
            print("Invalid password length input!")
            continue
        print("Invalid password length input!")
    if (strict_requirement and pass_length<4):
        print("Password must have atleast 4 characters when All requirement is True")
        continue
    while (True):
        #kiem tra password count input
        #nhap lai password count khi ko hop le
        pass_count = input("Enter passwords count: ")
        if (pass_count.isdigit()):
            pass_count = int(pass_count)
            if (pass_count>0):
                valid = True
                break
            print("Invalid password count!")
            continue
        print("Invalid password count!")
for i in range(pass_count):
    password = []
    lenght = pass_length
    if (strict_requirement): #neu All Requirement = True
        password.append(random.choice(letters.upper()))
        password.append(random.choice(letters))
        password.append(random.choice(numbers))
        password.append(random.choice(symbols))
        #dam bao co it nhat 1 ky tu viet hoa, 1 ky tu viet thuong, 1 ky tu so, 1 ky tu dac biet
        lenght -= 4
    #generate password
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
    #in ra password
    print(''.join([x for x in password]))