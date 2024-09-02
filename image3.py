def solution(image):
    answer = []

    is_left = False
    arrow_length = 0

    for img in image:
        if img == "-": 
            arrow_length += 1
        
        if img == "<":
            if is_left: 
                answer.append([-1, arrow_length])
                arrow_length = 0
            else: 
                is_left = True
        
        if img == ">":
            if is_left: 
                answer.append([0, arrow_length])
                arrow_length = 0
                is_left = False
            else: 
                answer.append([1, arrow_length])
                arrow_length = 0
    
    if arrow_length: 
        answer.append([-1, arrow_length])
   
    return answer