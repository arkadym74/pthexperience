#Prints the Words "Hello World"
'''This is a multiline comment'''
print("Hello World")

userAge, userName = 30, 'Peter'

x = 5
y = 10

y = x
print("x = ", x)
print("y = ", y)


brand = 'Apple'

exchangeRate  = 1.235235245

message = 'The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.2f} USD to 1 EUR'.format('Apple', 1299, 1.235235245)


message1 = '{0} is easier than {1}'.format('Pyhon', 'Java')
message2 = '{1} is easier than {0}'.format('Python', 'Java')
message3 = '{:10.2F} and {:d}'.format(1.234234234, 12)
message4 = '{}'.format(1.234234234)
print(message1)
print(message2)
print(message3)
print(message4)

#List
userAge = [21, 22, 23 ,24, 25]

userAge3 = userAge[2:4]

print(userAge3)

userAge4 = userAge[1:5:2]

print(userAge4)

userAge5 = userAge[:4]

print(userAge5 )

userAge[2] = 30

print(userAge)

userAge.append(100)

print(userAge)

del userAge[3]

print(userAge)

myList = [1,2,3,4,5,"Hello"]

print(myList)

print(myList[2])

print(myList[-1])

myList2 = myList[1:5]

print(myList2)

myList[1] = 20

print(myList)

myList.append('How are you')

print(myList)

del myList[6]

print(myList)

#Tupple
monthOfYear = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct","Nov", "Dec")

print(monthOfYear[0])

print(monthOfYear[-1])

#Dictionary

