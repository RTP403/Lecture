# %%
# Python: CSV reading
import csv
with open('rectangles_data.csv', newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# %%