
"""
Here the intutive Idea about solving the problem would come to be everytime checking if the leaves are on all the point between the source
and the destination, However, that doesn't meet the requirement in terms of optimized result.

Codility does provide a hint to this problem that space complexity be O(X),
so what could be done is mark all the point between source and destination as 0 and as soon as a leaf fall at that point a counter is increment
for the firsta time a leaf falls at that point, thus counter when reaches the same value as X, ensures that leaves are at
all points between the source and the destination.
"""

def solution(X, A):
    B = [0]*X
    leng = len(A)
    counter = 0
    for i in range(0,leng):
        if B[A[i]-1] == 0:
            B[A[i]-1] = 1
            counter+=1
        if counter == X:
            return i
    return -1

print(solution(5,[1,3,1,4,2,3,5,4]))
