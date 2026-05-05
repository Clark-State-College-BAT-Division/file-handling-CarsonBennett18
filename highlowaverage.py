#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the number
#Average
#Highest number
#Lowest number
#Correct answers for the included file: 15
numbers = []

with open("numbers.txt", "r") as file:
    for line in file:
        numbers.append(int(line.strip()))

count = len(numbers)
total = sum(numbers)
average = total / count
highest = max(numbers)
lowest = min(numbers)

print(f"How many numbers: {count}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Highest number: {highest}")
print(f"Lowest number: {lowest}")
