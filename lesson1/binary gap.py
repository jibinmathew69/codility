
def solution(N):
    flag = False
    currseqlen = 0
    length = 0

    while N:
        if N&1==1:
            if flag == False:
                flag = True
            else:
                length = max(length,currseqlen)
            currseqlen = 0
        else:
            currseqlen += 1
        N >>= 1
    return length
