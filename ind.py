data = tuple(map(int, input("Enter elements of the tuple separated by spaces: ").split()))

first_element = data[0]
count = sum(1 for i in data if i == first_element)

count = min(count, len(data))

remaining_elements = data[count:]

print(f"Count of identical elements at the beginning: {count}")
print(f"Elements after the last identical element: {remaining_elements}")
