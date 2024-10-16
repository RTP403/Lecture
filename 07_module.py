# %%
# Use the import statement to import a module
import math
print(math.pow(2, 6))
print(math.sin(2))

# %%
# To import only parts from a module, use the from keyword.
from datetime import datetime

print(datetime.now())
print(datetime.now().date())
print(datetime.now().time())
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)

print(datetime.now().strftime('%d / %m / %y'))

# %%
# To rename when you import a module, use the as keyword:
import statistics as st

a_list = [2, 5, 4, 9, 7, 2, 6, 9]
print(st.mean(a_list))
print(st.stdev(a_list))


# %%