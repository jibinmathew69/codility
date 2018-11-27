
"""
The intution here is that the counters get kind of reinitiated when the value is of A[i] is greater than N


correct : 100% but 60% in time complexity
def solution(N, A):
    B = [0]*N
    combinedCounter = 0
    leng = len(A)
    max = 0
    for i in range(0,leng):
        if A[i] <= N:
            B[A[i]-1] += 1
            if max<B[A[i]-1]:
                max = B[A[i]-1]
        else:
            B = [0]*N
            combinedCounter+=max
            max = 0

    for i in range(0,N):
        B[i] += combinedCounter

    return B
    
I realised the reason being B = [0]*N results in overall time complexity of N^2

"""

def solution(N, A):
    B = [0]*N
    min = 0
    leng = len(A)
    max = 0
    for i in range(0,leng):
        if A[i] <= N:
            if B[A[i]-1]<min:
                B[A[i]-1] = min
            B[A[i]-1] += 1
            if max<B[A[i]-1]:
                max = B[A[i]-1]
        else:
            min = max

    for i in range(0,N):
        if B[i]<min:
            B[i] = min

    return B

print(solution(5,[3,4,4,6,1,4,4]))