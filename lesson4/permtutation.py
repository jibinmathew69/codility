
"""
the immediate solution that would come to mind is to use n*(n+1)//2 formula which we used in one of our problems which would solve it in
time : O(n) and space : O(1), but the catch here is that it never states that the numbers are unique or consequtive. hence what could happen is
say the array length is 4 so we expect the sum to be 10 but what if the array is [1,1,1,7] = 10
hence a solution like this would not work

def solution(A):
    length = len(A)
    expectedSum = (length*(length+1))//2
    if sum(A) == expectedSum:
        return 1
    else:
        return 0

Rather going by the hint in the question from the space complexity, we could create a set from the array and check whether an iteration
on array has an element in the set and if the counter runs over the length of the array then it means that all the iteration values where 
there in the set and hence a permutation

"""


def solution(A):
    leng = len(A)
    A = set(A)

    num = 1
    while A.__contains__(num):
        num+=1

    if num > leng:
        return 1
    else:
        return 0

print(solution([1,1]))