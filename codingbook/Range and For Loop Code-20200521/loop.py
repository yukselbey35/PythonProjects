temperature = 120
while temperature > 117:
    print(temperature)
    temperature = temperature - 1
print("Temperature right now: ", temperature)
print("You can take your drink out of the fridge")

# WHILE LOOP
list = [1, 2, 3, 4, 5]
count_odd = 0
count_even = 0
i = 0
while list[i] in list:
    if list[i] % 2 == 0:
        print("The number ", list[i], " is even")
        count_even += 1
    else:
        print("The number ", list[i], " is odd")
        count_odd += 1
    i += 1
print("The number of even numbers is: ", count_even)
print("The number of odd numbers is: ", count_odd)

# FOR LOOP
list = [1, 2, 3, 4, 5]
count_odd = 0
count_even = 0
for i in list:
    if i % 2 == 0:
        print("The number ", i, " is even")
        count_even += 1
    else:
        print("The number ", i, " is odd")
        count_odd += 1
print("The number of even numbers is: ", count_even)
print("The number of odd numbers is: ", count_odd)

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number)

# Error
# number = [1:100]
# print(number)

numbersRange = range(1, 10, 1)
print(type(numbersRange))

numbersRange = range(1, 10, 1)
numbers = list(numbersRange)
print(numbers)

numbers = list(range(1, 10, 1))
print(numbers)

numbers = list(range(1, 10, 2))
print(list(range(10)))
number = 10
print(number in range(1, 6))
number = 10

if number in range(1, 6):
    print("Number is in " + str(list(range(1,6))))
else:
    print("Number is not in " + str(list(range(1, 6))))
number = 1

while number <= 5:
    print(number)
    number += 1

for number in range(1, 6):
    print(number)

for organ in ['heart', 'brain', 'lung']:
    print(organ)

for number in range(1, 5):
    print(number)
    print("End of for loop")

number = 10
for number in range(2, 11):
    print(1)
    print(2)
    number += 1
print(3)

print(list(range(2, 11)))
number = 10

# Error
# for number < 10:
#     print(1)
#     number += 1

for number in range(6):
    print(number)
    break
print("End of for loop")

for number in range(6):
    if number == 3:
        break
    print(number)
print("End of for loop")

for number in range(6):
    print(number)
    for number2 in range(3):
        print(number2 ** 2)
        break
    print("End of for loop2")
print("End of for loop1")

for i in [1, 2, 3, 4, 5]:
    if i == 3:
        pass
    print(i)
print("Exit")