def someFunction(a, b, c=1, d=2, e=3):
    print(a, b, c, d, e)

someFunction(20, 30, 40, 50, 60)


#non-keyworded variable argument list
def addNumbers(*num):
    sum = 0
    for i in num:
        sum = sum + i
    print(sum)

addNumbers(20,30,50,60)

#keyworded variable length argument list
def printMemberAge(**age):
    for i, j in age.items():
        print("Name = %s, Age = %s" %(i, j))


printMemberAge(Peter = 5, John = 7)

printMemberAge(Peter = 5, John = 7, Yvonne = 10)

'''
The order of a function
with a normal argument
non-keyworded and keyworded
def someFunction2(farg, *args, **kwargs):
'''

