#Regular if example
userInput = input('Enter 1 or 2:')

if userInput == "1":
    print("Hello World")
    print("How are you")
elif userInput == "2":
    print("Python Rocks!")
    print("I love Python")
else:
    print("You did not enter a valid number")

#Inline If example 
num = 12 if userInput=="1" else 13

print("This is task A" if userInput == "1" else "This is task B")

#for loop regualar iterable
pets = ['cats', 'dogs', 'rabbits', 'hamsters']

for myPets in pets:
    print(myPets)

#To display index of the list memebers using for loop
for index, myPets in enumerate(pets):
    print(index, myPets)

#for loop in dictionaries
age = dict(Peter = 5, John = 7)

for i in age:
    print(i)

#To print value and a key from a dictionary

for i in age:
    print("Name = %s, Age = %d" %(i, age[i]))

#To print value and a key from a dictionary key-data pair tuple using items method

for i, j in age.items():
    print("Name = %s, Age = %d" %(i,j))

#Using for loop to iterate through a string

message = 'Hello'

for i in message:
    print(i)

#Using range to loop trough the sequence of numbers

for i in range(5):
    print(i)

#Simple while loop condition

counter  = 5

while counter > 0:
    print("Counter = ", counter)
    counter = counter - 1
