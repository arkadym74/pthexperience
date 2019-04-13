import random #first type
import random as r #second type
from random import randrange #third type
import sys
import prime

test1 =  random.randrange(1, 10)

print(test1)

test2 = r.randrange(2, 30)

print(test2)

test3 = randrange(40,60)

print(test3)

#creating your own modules
answer = prime.checkIfPrime(13)
print(answer)

