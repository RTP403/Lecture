# Operators

x = 25
y = 3

# Arithmetic operators
# x + y
# x - y
# x * y
# x / y 
# x ** y 
# x % y
# x // y

print(x ** y)
print(x // y)
print( x % y)

# %%
# Example 1 - get all odd number from 10 to 100 and store in a list
odd_numbers = [i for i in range(10,101) if i % 2 != 0 ]
print(odd_numbers)

odd_numbers_2 = [i for i in range(10,101) if i % 2  ]
print(odd_numbers_2)

even_numbers = [i for i in range(10,101) if i % 2 == 0 ]
print(even_numbers)

# %%
# Example 2 - multiple all numbers by 3 in a list
print([i  for i in range(5,20,2)])

print([i * 3 for i in range(5,20,2)])
# Assignment Operator

x = 1
x += 5 # x = x + 5
x -= 2 # x = x - 2
print(x)

# %%
# Comparison operators
# x == y
# x != y
# x > y
# x < y
# x >= y
# x <= y

# %%
# Logical operators
print( x > 1 and x < 10)
print( x > 1 or x < 10)
print(not(x < 5))



# %%
# Identity operators


# %%
# Membership Operators
print('x' in ['x', 'z'])
print('x' in ['y', 'z'])
print('x' not in ['t', 'z'])
# %%
