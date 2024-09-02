def solution(n, m, licenses, spec):
    answer = []

    for i in range(len(spec)):
        is_qualified  = True

        for li in licenses:
            if spec[i][li-1] == 0:
                is_qualified = False
                break
        if not is_qualified:
            continue

        if sum(spec[i]) >= m:
            answer.append(i+1)
    
    return answer