# %%
# Use def keyword to define a function
def greeting (name):
    print(f'{name}, Welcome to ACDA class!')

greeting('Heather')

# %%
def add(a, b):
    return a + b

print (add(23, 12))

print(add('Hello', 'Bye'))

# %%
# Declare data type
def new_add(a: int, b: int):
    return a + b

print(new_add(12, 45))
# print(new_add(12, 'Bye')) wrong data type as defined in new_add
print(new_add(12, 45.8))

# %%
# Use return keyword if the function has a return value.

# %%
# Declare the data type

# %%
# Casting the variables

a = 22
b = '35'

print(str(a) + b)
print(a + int(b))