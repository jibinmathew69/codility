
"""
This is something similar to classic cylic queue
"""

def solution(A, K):
    length = len(A)
    B = [0] * length

    for i in range(0,length):
        j = (i+K)%length
        B[j] = A[i]

    return B

print(solution([3, 8, 9, 7, 6],3))