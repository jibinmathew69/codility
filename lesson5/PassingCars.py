
#
# def solution(A):
#
#     count = 0
#
#     length = len(A)
#     for i in range(length):
#
#         if A[i] == 0:
#             for j in range(i+1,length):
#                 if A[j] == 1:
#                     count+=1
#
#     if count > 1000000000:
#         return -1
#
#     return count


def solution(A):

    zeroesCount = 0
    pairs = 0

    for  i in range(len(A)):
        if A[i] == 0:
            zeroesCount += 1
        else:
            pairs+=zeroesCount

        if pairs>1000000000:
            return -1

    return pairs