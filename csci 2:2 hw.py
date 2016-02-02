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

# 3)

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
    print "N = %s P1 = %s P2 = %s" % (n, (oneThird / n), (twoThirds / n)) 


print("Question 3:")
problem1(100)
problem1(1000)
problem1(10000) 


# 7)

