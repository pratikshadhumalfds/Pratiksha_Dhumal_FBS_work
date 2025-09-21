#Accept a number from user and check if this element is present in the list or not.
# Also tell how many times it is present in the list.


n = int(input("Enter number of elements in the list: "))
numbers = []

for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    numbers.append(val)

n = int(input("Enter the number to search for: "))

count = 0
for num in numbers:
    if num == n:
        count += 1

if count > 0:
    print(f"The number {n} is present in the list.")
    print(f"It appears {count} times.")
else:
    print(f"The number {n} is not present in the list.")
