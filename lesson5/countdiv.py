

# def solution(A, B, K):
#
#     num = ((B-1)-A)//K
#
#     if B%K == 0:
#         num+=1
#     if A%K == 0:
#         num+=1
#     return max(num,0)
#
# print(solution(4,4,4))


def solution(A, B, K):

    num = (B//K) - (A//K)
    if A % K == 0:
        num+=1

    return num