
"""
in order to solve this problem in the given time complexity we need to understand and use XOR operation
the operator symbol is ^
2^2 = 0
3^3 = 0
so if we continously xor iterating for the given array , we should cancel out all the pair and finally be left with only the odd 
occurance number
"""

def solution(A):
    oddnumber = 0
    for i in A:
        oddnumber = oddnumber^i

    return oddnumber

print(solution([9,3,9,3,9,7,9]))