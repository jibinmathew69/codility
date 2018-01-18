"""
For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

def solution(A)

that, given a zero-indexed array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
"""
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