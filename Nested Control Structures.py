'''
Programmer: Wyatt McComb
Date: 10/15/19
Program: Double For Loop

This Program will nest a For Loop inside of another For Loop.
'''

for i in range(3):
    print('Outer For Loop: ' + str(i))
    for l in range(2):
        print("     Inner For Loop: " + str(l))



print("\n************\n")

'''
Programmer: Wyatt McComb
Date: 10/22/19
Program: Average Test Scores

This Program asks for the test scores for multiple people and reports 
the average test score for each portion.
'''

num_people = int(input("How many people are taking the test: "))
test_per_person = int(input("How many test are going to be averaged: "))

for i in range(num_people):
    name = input("Enter Name: ")
    sum = 0
    for j in range(test_per_person):
        score = int(input("  Enter a score: "))
        sum = sum + score
    average = float(sum) / test_per_person
    print("     Average for " + name + ": " + str(round(average, 2)))

print(\n***************\n)

'''
Programmer: Wyatt McComb
Date 10/22/19
Program: For Loop + While Loop

This program will ask users of an internet to them then ask for two items related to that interest
'''

for i in range(4):
    print('Outer For Loop: ' + str(i))
    x = 1
    while x >= 0:
        print('    While Loop: ' + str(x))
        x = x - 1
        

