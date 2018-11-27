def solution(A):


    A.sort()

    for i in range(0,len(A)-2):
        if A[i]+A[i+1]>A[i+2]:
            return 1

    return 0


print(solution([10,50,5,1]))