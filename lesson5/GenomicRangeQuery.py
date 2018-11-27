

# o(m*n)
# def solution(S, P, Q):
#     M = len(P)
#     vocab = {
#         'A': 1,
#         'C': 2,
#         'G': 3,
#         'T': 4,
#     }
#
#     ret = []
#     for i in range(M):
#         ret.append(S[P[i]:Q[i]+1])
#
#
#
#     return ret


def writeCharToList(S, last_seen, c, idx):
    if S[idx] == c:
        last_seen[idx] = idx
    elif idx > 0:
        last_seen[idx] = last_seen[idx - 1]


def solution(S, P, Q):
    if len(P) != len(Q):
        raise Exception("Invalid input")

    last_seen_A = [-1] * len(S)
    last_seen_C = [-1] * len(S)
    last_seen_G = [-1] * len(S)
    last_seen_T = [-1] * len(S)

    for idx in range(len(S)):
        writeCharToList(S, last_seen_A, 'A', idx)
        writeCharToList(S, last_seen_C, 'C', idx)
        writeCharToList(S, last_seen_G, 'G', idx)
        writeCharToList(S, last_seen_T, 'T', idx)

    solution = [0] * len(Q)

    for idx in range(len(Q)):
        if last_seen_A[Q[idx]] >= P[idx]:
            solution[idx] = 1
        elif last_seen_C[Q[idx]] >= P[idx]:
            solution[idx] = 2
        elif last_seen_G[Q[idx]] >= P[idx]:
            solution[idx] = 3
        elif last_seen_T[Q[idx]] >= P[idx]:
            solution[idx] = 4
        else:
            raise Exception("Should never happen")

    return solution


print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))