# Cole Calhoun
# CSCI 164 Homework 
# Feb 2, 2016
from __future__ import division
import random




# Chapter 3

# 3)

# 8)

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


print("Chapter 4, Question 1:\n")
problem1(100)
problem1(1000)
problem1(10000) 

# 3)

def problem3(n):
    One = 0
    Two = 0
    Three = 0
    Four = 0
    counter = 0

    while counter <= n:
        testNumber = random.random()

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

