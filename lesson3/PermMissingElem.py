
"""
the intution we have here is that exactly 1 element is missing in between, thus if there are 5 elements in the array then max of all
the numbers will be 6 and minimum obviously is 1.

so finding the sum of first n natural numbers is (n*(n+1))/2(enforces integer division)
and the from that if we subtract the  sum of the present array then we get the missing number 
"""


def solution(A):
    length = len(A)
    expectedSum = ((length+1)*(length+2))//2
    actualsum = sum(A)

    return expectedSum-actualsum

print(solution([2,3,1,5]))