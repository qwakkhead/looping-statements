size_array = int(input("Enter how many size of the array"))
elements = []

for i in range(size_array):
    element = int(input(f"Enter element {i+1}: "))
    elements.append(element)

for element in elements:
    print(element ** 3)