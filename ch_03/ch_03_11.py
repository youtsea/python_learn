import random

values = [1, 2, 3, 4, 5, 6]

print random.choice(values)
print random.choice(values)
print random.choice(values)
print random.choice(values)
print random.choice(values)

print random.sample(values, 2)
print random.sample(values, 2)
print random.sample(values, 2)
print random.sample(values, 2)

random.shuffle(values)
print values
random.shuffle(values)
print values
random.shuffle(values)
print values

print random.randint(0, 10)
print random.randint(0, 10)
print random.randint(0, 10)
print random.randint(0, 10)
print random.randint(0, 10)

print random.random()
print random.random()
print random.random()
print random.random()

print random.getrandbits(200)
