###Write a program to reverse the list...

#without using built-in function.
numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Reversed list:", reversed_list)




#with using built-in function.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers.reverse()

print("Reversed list:", numbers)
