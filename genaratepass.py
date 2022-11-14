import string
import random

def genpassword():
    lenopass = random.randint(7,11)
    S = lenopass
    ran = ''.join(random.choices(string.ascii_letters + string.digits, k = S))
    return "Hey Buddy. I just generated an awesome strong password for you. Your password is " + ran

password = genpassword()
print(password)