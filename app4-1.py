#!/usr/bin/env python3

list = []
while (len(list) <= 10):
    x = input("Human Put a number: ")
    list.append(x)
s = set(list)
print("Here is your Set : " + str(s))
