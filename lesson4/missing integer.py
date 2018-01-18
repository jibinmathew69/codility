"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

"""
"""
The problem is pretty easy just convert into a set , the all element become unique start counting from 1 and aslong as the counter value exist
in the set increment the counter and as soon as the loop break , the value of the counter is the desired value.
"""
def solution(A):
    A = set(A)
    num = 1
    while A.__contains__(num):
        num+=1

    return num

print(solution([-11,-1]))