def dfs_sockets(k, limits, sockets, node):
    cur_power = 0
    cur_cnt = 0
    total_cnt = 0

    for socket in sockets[node]:
        if socket == -1:
            cur_power += k
        elif socket != 0:
            new_power, new_cnt = dfs_sockets(k, limits, sockets, socket)
            cur_power += new_power
            total_cnt += new_cnt

    if cur_power > limits[node]:
        excess = cur_power - limits[node]
        cur_cnt = excess // k
        if excess % k > 0:
            cur_cnt += 1
        
        cur_power -= cur_cnt * k
        total_cnt += cur_cnt

    return cur_power, total_cnt


def solution(k, limits, sockets):
    sockets = [[]] + sockets
    limits = [0] + limits

    a, answer = dfs_sockets(k, limits, sockets, 1)

    return answer