import random
import string

psn = int(input("How long do you want your password to be"))
def auto_gene(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    pasw = ''.join(random.choice(characters) for i in range(length))
    return pasw 

a = print(auto_gene())