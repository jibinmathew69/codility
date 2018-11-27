
"""
Trying to understand the fact that is a tape and the total length of the tape is constant and is the sum of all the array values.

for and every iteration over the index if the value at the idex is added and at the same time substracted then the length of the 2 segments
could be determined and compared with previously most minimum value.
"""
import sys
def solution(A):
    length = len(A)
    totalLength = sum(A)
    tapeA = A[0]
    min = sys.maxsize
    for i in range(1,length):
        tapeB = totalLength-tapeA
        diff = abs(tapeB-tapeA)
        if diff<min:
            min = diff
        tapeA += A[i]
    return min

print(solution([5, 6, 2, 4, 1]))
print(solution([1, 1]))
print(solution([-1, 1]))
