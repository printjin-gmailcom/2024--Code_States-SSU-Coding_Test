def solution(order, single_price, set_menu, set_price):
    min_price = float('inf')

    price = 0
    for i in range(len(order)):
        price += order[i]*single_price[i]
    
    min_price = min(min_price, price)

    for i in range(len(set_menu)):
        price = set_price[i]
        cur_order = order[:] 

        for j in range(len(cur_order)):
            cur_order[j] -= set_menu[i][j]
            if cur_order[j] < 0:
                cur_order[j] = 0
        
        for j in range(len(cur_order)):
            price += cur_order[j]*single_price[j]
        
        min_price = min(min_price, price)
    
    for i in range(len(set_menu)):
        for k in range(len(set_menu)):
            price = set_price[i] + set_price[k]
            cur_order = order[:]
						
            for j in range(len(cur_order)):
                cur_order[j] -= set_menu[i][j] + set_menu[k][j]
                if cur_order[j] < 0:
                    cur_order[j] = 0
            
            for j in range(len(cur_order)):
                price += cur_order[j]*single_price[j]
            
            min_price = min(min_price, price)

    return min_price

print(solution([2, 0, 3, 2, 1], [3000, 2000, 10000, 1000, 5000], [[0, 1, 1, 0, 1], [0, 0, 3, 0, 0], [1, 0, 2, 3, 0]], [12000, 27000, 20000]))