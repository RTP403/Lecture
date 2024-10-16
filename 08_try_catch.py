# The try block:
#            tests a block of code for errors.
# The except block:
#            handles the error.
# The else block:
#            executes, if no errors were raised
# The finally block:
#            executes, regardless of the result of the try- and except blocks.

# %%
a = 2

try:
    print('hello' + c)
except Exception as e:
    print('Something is wrong')
    print(e)

# %%

a = 'text'
try:
    print('hello' + a)
except Exception as e:
    print('Something is wrong')
    print(e)
else:
    print('Nothing is wrong')
finally:
    print('Done')
# %%

a = 'text'
try:
    print('hello' + c)
except NameError:
    print('No such variable exists')
except Exception as e:
    print('Something is wrong')
    print(e)
else:
    print('Nothing is wrong')
finally:
    print('Done')