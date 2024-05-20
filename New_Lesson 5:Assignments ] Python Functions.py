#Lesson 5:Assignments ] Python Functions
#1.The Calculator App
 # This function addition two number
def addnum():
    fnum = int(input("Enter an number: ")) 
    snum = int(input("Enter an integer: "))
    sum = fnum + snum
    print("The sum of ", fnum, "and",snum, "is" ,sum)
 # This function subtraction two number
def difnum():
    dif1 = int(input("Enter an integer: "))
    dif2 = int(input("Enter an integer: "))
    dift = dif1 - dif2
    print(dift, " is The diference of the numbers!")
 # This function multiplies two numbers
def multinum():
    mult1 = int(input("Enter an integer: "))
    mult2 = int(input("Enter an integer: "))
    multt = mult1 * mult2
    print(multt, "is The product is!")
 # This function divides two numbers
def divnum():
    div1 = int(input("Enter an integer: "))
    div2 = int(input("Enter an integer: "))
    if div2 == 0:
        print("Denominator is zero")
        print(divt)
    else: 
        divt >= 0
        divt = div1/div2
        div2 == 0
        print("Denominator is zero")
d1a = input('Would you like to add, subtract, multiply, or divide?')
if d1a == 'add':
    addnum()
    print("The product of the numbers!")
elif d1a == 'subtract':
    difnum()
    print("The diference of the numbers!")
elif d1a == 'multiply':
    multinum()
    print("The multiple of the numbers!")
elif d1a == 'divide':
    divnum()
    print("The quotient of the numbers!")     
#2. The Shopping List Maker
#Task 1
# use a fuction we can call in it use while loop to ask what we want to add to get users input their input add to my list by apend is the best way to add
#add it to back of the list let them continue to add things
Shoping_list = ['Ice cream', 'jello', 'gummies', 'life savers']
print("lets go shopping")
action = input("go or stop")
print(Shoping_list)
if action == "go":
    print("Shoping is a go")
    YN= input("add items or remove items")
    if YN == "add items":
        print("add an item to the shoping list")
        Shoping_list.append(input("Enter an item"))
        print(Shoping_list)
        print("complete")
    elif YN == "remove items":
            print("remove an item from the shoping list")
            Shoping_list.remove(input("Enter an item to remove"))
            print(Shoping_list)
else:
    action == "stop"
    print("Shoping Complete")
#Remove an item from the list
#3
#Task 1 
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
def Average():
    return sum(grades)/ len(grades)
Average()
print("Average of the grades =")
print(Average(grades))
#Task 2 
def lowgrades():
    return min(grades)
lowgrades()
print("Lowest grade =")
print(min(grades))
#BONUS
for grade in grades:
    if grade >= 90:
        print("Your Grade is an A")
    elif grade  >=80:
        print("Your grade is a B")
    else:
        print("Your grade is a C")