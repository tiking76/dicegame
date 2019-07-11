import random
a = random.randint(1,6)
b = random.randint(1,6)
d = input("What is your name ?  ")
print("Hello, " + str(d) + "!")
print("Rolling the dice...")
print("Die 1: " + str(a))
print("Die 2: " + str(b))
c = 0
c = a + b
print("Total value: " + str(c))
if c > 7:
    print(str(d) + " won!")
else:
    print(str(d) + " lost!")