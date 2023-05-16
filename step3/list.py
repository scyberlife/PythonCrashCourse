names = ["Sergei", "Andrei", "Alex", "Clop", "Alexandr"]
print(names[0], names[1], names[2])
print(f"{names[0]}, hi")
names.append("Bill")
print(names)
del names[0]
print(names)
names.remove("Andrei")
print(names)
names.insert(2, "Lock")
print(names)
name = names.pop()
print(name)
