# enumerate_zip_examples.py

names = ["Ali", "Bek", "Dana"]
scores = [85, 90, 78]

# enumerate()
for index, name in enumerate(names):
    print(index, name)

# zip()
for name, score in zip(names, scores):
    print(name, score)

# sorted()
print("Sorted scores:", sorted(scores))

# Type checking
x = "123"
print("Type before:", type(x))

x = int(x)
print("Type after:", type(x))