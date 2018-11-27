def solution(S):


    push = ('{','[','(')
    pop = {
        '}':'{',
        ']':'[',
        ')':'('
    }

    stack = []

    for i in S:
        if i in push:
            stack.append(i)

        else:
            try:
                if pop[i] == stack[-1]:
                    stack.pop()

                else:
                    return 0
            except:
                return 0

    if len(stack)!=0:
        return 0

    return 1


print(solution('{[()()]}'))