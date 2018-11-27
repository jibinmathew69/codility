
"""
It is a simple problem, basically all that needs to be done is to get the distance between the 2 point and then obtain the number of 
exact complete jumps or complete jump+1 to crossover. what needs to be taken care is the integer value of number of steps.  
"""


def solution(X, Y, D):
    dist = Y-X
    jumps = dist//D
    if dist%D!=0:
        jumps+=1
    return jumps