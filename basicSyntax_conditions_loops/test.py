# Въведете височината на сърцето
height = int(input("Въведете височината на сърцето: "))

# Горна част на сърцето
for i in range(height // 2, height + 1, 2):
    print(" " * ((height - i) // 2), end="")
    print("*" * i, end="")
    print(" " * ((height - i) // 2), end="")
    print("*" * i)

# Долна част на сърцето
for i in range(height, 0, -1):
    print(" " * (height - i), end="")
    print("*" * (2 * i), end="")
    print(" " * (height - i))
