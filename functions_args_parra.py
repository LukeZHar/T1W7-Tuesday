# Greeting someone
def greet():
    print("Hello Coders")

greet()

def greet():
    print("Hello friends")

greet()

def greet():
    print("Hello foes")

greet()

def greet(name): # <-- parrameter
    print(f"Hello coders, {name}")

greet("woo")

def greeting(fname, lname):
    print(f"Hello coder, {fname} {lname}")

greeting("Luke", "Harris")

def subtract(a, b=1):
    difference = a - b
    return difference

result = subtract(a=4, b=3)

print(result)
