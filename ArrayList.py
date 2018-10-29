# Python Array user input by single input
list1 = []
num = int(input("Enter length: "))
print("Enter Number: ")
for i in range (num):
    data = int(input())
    list1.append(data)
print("You have entered: ")
for i in range (num):
    print(list1[i])
