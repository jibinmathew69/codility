
"""
The problem is pretty easy just convert into a set , the all element become unique start counting from 1 and aslong as the counter value exist
in the set increment the counter and as soon as the loop break , the value of the counter is the desired value.
"""
def solution(A):
    A = set(A)
    num = 1
    while A.__contains__(num):
        num+=1

    return num

print(solution([-11,-1]))