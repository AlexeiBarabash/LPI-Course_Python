# this is solution for task 3,A
lst = [17, 1, 12, 54, 23, 9, 21]

lst_sum = sum(i for i in lst if i > 3 and i < 20)

print(lst_sum)


# this is solution for task 3,B
print("Human please enter a numbers that are less then 10 ill stop you when the sum is greater then 30")
user_input = input("Human please enter a number: ")
user_list =[]

# This is better exception if the user insert char better error message
try:
    while int(user_input) < 10:
        user_list.append(int(user_input))
        if sum(user_list) >= 30:
            print("Human the sum of the list is 30 or greater ")
            print(sum(user_list))
            break
        user_input = input("Human please enter a another number: ")

    # we put check to determine the issue that he exited before the break
    if int(user_input) > 10:
        print("Human next time please insert numbers less then 10")
    print("Good Bye Human!")
except ValueError:
    print("Human don`t play with me INSERT ONLY INTEGERS!")


# this is solution for task 3,C

lst_length = input("Human how long do you want the array to be  :")
l = []

while len(l) <= int(lst_length)-1:
    while len(l) < 3:
        x = int(input("Human put a number: "))
        l.append(x)

    x = int(input("Human put a number: "))
    if x < 5:
        l.append(x + x)
    if x < 10 and x > 6:
        l.append(x * x)
    if x > 10:
        l.append(x ** x)

print(l)





