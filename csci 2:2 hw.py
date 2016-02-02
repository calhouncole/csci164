# Cole Calhoun
# CSCI 164 Homework 
# Feb 2, 2016
from __future__ import division
from math import exp, pi
import random




# Chapter 3

# 3)

def chapter3Problem3(n):
    estimation = 0
    for each in range(n):
        randomInt = random.random()
        estimation += exp(exp(randomInt))
    print "Chapter 3, Problem 3\nThe estimation is: %s" % (estimation/n)

chapter3Problem3(100)

# 8)

def chapter3Problem8(n):
    estimation = 0
    for each in range(n):
        randomInt = random.random()
        randomInt *= (2 * pi)
        estimation += exp(randomInt*randomInt)
    print "\nChapter 3, Problem 8\nThe estimation is: %s" % (estimation/n)

chapter3Problem8(100)

# Chapter 4

# 1)

def problem1(n):
    oneThird = 0
    twoThirds = 0
    counter = 0
    while counter <= n:
        testNumber = random.random()
        if testNumber <= (1/3):
            oneThird+=1
        else:
            twoThirds+=1


        counter+=1
    print "N = %s P1 = %s%% P2 = %s%%" % (n, (oneThird / n), (twoThirds / n)) 


print("\nChapter 4, Question 1:\n")
problem1(100)
problem1(1000)
problem1(10000) 

# 3)

def problem3(n):
    # X=1
    One = 0
    # X=2
    Two = 0
    # X=3
    Three = 0
    # X=4
    Four = 0

    counter = 0

    while counter <= n:
        testNumber = random.random()

        # ASSIGN ALL VARIABLES TO THEIR EXPECTED PROPORTIONS

        if testNumber <= (.3): 
            One+=1
        elif testNumber >(.3) and testNumber <=(.5):
            Two+=1
        elif testNumber >(.5) and testNumber <=(.85):
            Three += 1
        elif testNumber >(.85) and testNumber <=(1):
            Four +=1

        counter+=1

    print("\nChapter 4, Question 3:\n")
    print "N = %s\nOne = %s%%\nTwo = %s%%\nThree = %s%%\nFour = %s%%\n" % (n, (One / n), (Two / n), (Three / n), (Four / n))

problem3(100)


# 7)

def problem7(n):

    # INITIALIZE A DICTIONARY OF ALL POSSIBLE ROLLS WITH A VALUE OF FALSE
    # WHEN THE ROLL IS ROLLED - CHANGE THE VALUE TO TRUE
    # IF ALL VALUES IN THE DICTIONARY ARE TRUE -- ALL POSSIBLE ROLLS HAVE BEEN ROLLED
    # COUNT HOW MANY ROLLS IT TOOK

    # DO THIS FOR YOUR SAMPLE SIZE AND DIVIDE THE TOTAL NUMBER OF ROLLS BY THE SAMPLE SIZE

    sumOfRolls = 0

    for each in range(n):
        numberOfRolls = 0
        dictionary = {2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False, 10: False, 11: False, 12: False}
        possibilitiesMet = 0
        allPossibilitesMet = False
        while allPossibilitesMet == False:
            numberOfRolls += 1
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            completeRoll = dice1 + dice2
            if dictionary[completeRoll] == False:
                dictionary[completeRoll] = True
            possibilitiesMet = 0
            for each in dictionary:
                if dictionary[each] == False:
                    break
                else:
                    possibilitiesMet += 1
                if possibilitiesMet == 11:   
                    sumOfRolls += numberOfRolls
                    allPossibilitesMet = True
                    break
        numberOfRolls = 0 
        possibilitiesMet = 0      


    print "\nChapter 4, Question 7:\n"
    print "It took an average of %s rolls for all possibilities to be rolled out of %s tries" % (sumOfRolls/n, n)
problem7(1000)




