#input 
myName = input("Please enter your name:")

#inputs using string formators
myAge = input("Hi %s, what about your age: " %(myName))

myAge = input("Hi {}, what about your age: ".format(myName))

#regular print
print("Hello World, my name is", myName, "and I am", myAge, "years old.")

#print using formators
print("Hello world, my name is %s and I am %s years old." %(myName, myAge))


print("Hello world, my name is {} and I am {} years old".format(myName, myAge))

#Multiline print
print(''' Hello World.
My Name is James and
I am 20 years old''')


#Tab
print('Hello\tWorld')

#New Line
print('Hello\nWorld')

#if needs to print a double quote character like in this example
print("I am 5'4\" tall")

#if needs to print a single quote character like in this example
print('I am 5\'4" tall')

#If we don't want to use special characters afte the forward slash
print(r'Hello\tWorld')

