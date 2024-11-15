import random

from colorama import *
init(autoreset=True)
#if you are new to colorama, run: pip install colorama , to install.

password = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890qwertyuiopasdfghjklzxcvbnm!@#$&?-.,"
password_length = int(input("ENTER THE LENGTH OF THE PASSWORD: "))
a = "".join(random.sample(password, password_length))

print(Fore.GREEN + f"Your Strong Password is: {a}")