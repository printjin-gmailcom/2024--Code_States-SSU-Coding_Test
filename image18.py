def solution(levels):
    answer = [0, 0]

    lev_cnt = {}
    for lev in levels:
        if lev not in lev_cnt:
            lev_cnt[lev] = 0
        lev_cnt[lev] += 1
    
    max_level = max(lev_cnt.keys())
		
    for lev in range(1, 1+max_level):
        if lev not in lev_cnt:
            lev_cnt[lev] = 0
        
        node_limit = 2**(lev-1)

        if lev_cnt[lev] > node_limit:
            answer[0] += lev_cnt[lev] - node_limit
            lev_cnt[lev] = node_limit
    
    for lev in range(max_level, 0, -1):
        if lev not in lev_cnt:
            lev_cnt[lev] = 0

        if lev+1 not in lev_cnt:
            children = 0
        else:
            children = lev_cnt[lev+1]
        
        node_needed = (children+1) // 2

        if node_needed > lev_cnt[lev]:
            answer[1] += node_needed - lev_cnt[lev]
            lev_cnt[lev] = node_needed
        
    return answer