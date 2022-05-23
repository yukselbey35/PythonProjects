python: order a list of numbers without built-in sort, min, max function
print("Hello world")
list1 = [-5, -23, 5, 0, 23, -6, 23, 67]

new_list1 = []

while list1:
    min_number = list1[0] #Random number
    for i in list1:
        if i < min_number:
            min_number = i
    new_list1.append(min_number)
    list1.remove(min_number)
print(new_list1)

##########################################
# FOR LOOP
"""
Write a guessing game that works like this: 
Your code will be given a number that is between 0 and 100. 
In every turn, you will guess a number. 
If your guess is lower than the answer, your program will say “up”, if not, 
it will say “down”. This way after a couple of turns your program will find the answer.
"""
guessNumber=int(input("Enter a secret number:"))
userNumber =int(input("Guess a number:"))
while guessNumber != userNumber:
    if guessNumber < userNumber:
        print("Go down")
        userNumber =int(input("Guess a number:"))
    elif guessNumber > userNumber:
        print("Go up")
        userNumber =int(input("Guess a number:"))
    else:
        
        break
print(f"{userNumber} is the number:")