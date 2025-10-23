'''
class Dog:
    # Class attribute - shared by all instances of the class
    species = "Canine"

    # Constructor method - initializes a new instance of the class
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    # Instance method - a function associated with an object
    def bark(self):
        return f"{self.name} says Woof!"

    def celebrate_birthday(self):
        self.age += 1
        return f"Happy birthday, {self.name}! You are now {self.age} years old."



# Create instances (objects) of the Dog class
dog1 = Dog("Buddy", 3)

# Access attributes of the objects
print(f"{dog1.name} is a {dog1.species} and is {dog1.age} years old.")

# Call methods on the objects
print(dog1.bark())
print(dog1.celebrate_birthday())
print(f"{dog1.name} is now {dog1.age} years old.")

#=============================
'''

import subprocess

def ping(address):
    command = ["ping", "-n", "4", address]
    print("Let's ping this address:",address)
    result = subprocess.run(command, capture_output=True, text=True, timeout=15)
    if result.returncode == 0:
        print("✅ ping command sent successfully.")
        print(result.stdout)

ip = ("142.250.176.206", "127.0.0.1", "127.0.0.1")

for address in ip:
    ping(address)
#================================================================


from concurrent.futures import ThreadPoolExecutor, as_completed

commands = [
    "ping -n 2 8.8.8.8",
    "ping -n 2 1.1.1.1",
    "ping -n 2 google.com",
    "ping -n 2 8.8.8.8",
    "ping -n 2 1.1.1.1",
    "ping -n 2 google.com",
    "ping -n 2 8.8.8.8",
    "ping -n 2 1.1.1.1",
    "ping -n 2 google.com",
    "ping -n 2 8.8.8.8",
    "ping -n 2 1.1.1.1",
    "ping -n 2 google.com",
    "ping -n 2 8.8.8.8",
    "ping -n 2 1.1.1.1",
    "ping -n 2 google.com",
]

def run_command(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return cmd, result.returncode, result.stdout.strip(), result.stderr.strip()

with ThreadPoolExecutor(max_workers=30) as executor:
    futures = [executor.submit(run_command, cmd) for cmd in commands]

    for future in as_completed(futures):
        cmd, code, out, err = future.result()
        print(f"\n>>> {cmd}")
        print(f"Exit code: {code}")
        print(f"Output:\n{out}")

#================================================================
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something before the function.")
        result = func(*args, **kwargs)
        print("Something after the function.")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()