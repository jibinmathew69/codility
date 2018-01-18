"""
A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given a zero-indexed array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:

def solution(X, A)

that, given a non-empty zero-indexed array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
the function should return 6, as explained above.

Assume that:

N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(X), beyond input storage (not counting the storage required for input arguments).

"""

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
