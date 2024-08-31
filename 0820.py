# https://school.programmers.co.kr/learn/courses/30/lessons/86051?language=python3

def solution(numbers):
    all_numbers = set(range(10))
    missing_numbers = all_numbers - set(numbers)
    return sum(missing_numbers)

print(solution([1,2,3,4,6,7,8,0]))  # 14
print(solution([5,8,4,0,6,7,9]))    # 6

# https://school.programmers.co.kr/learn/courses/30/lessons/178871?language=python3

def solution(players, callings):
    player_index = {player: i for i, player in enumerate(players)}
    
    for calling in callings:
        current_index = player_index[calling]
        if current_index > 0:
            player_in_front = players[current_index - 1]
            players[current_index], players[current_index - 1] = players[current_index - 1], players[current_index]
            player_index[calling] -= 1
            player_index[player_in_front] += 1
    
    return players

# https://school.programmers.co.kr/learn/courses/30/lessons/92334?language=python3

def solution(id_list, report, k):
    report_dict = {user: set() for user in id_list}
    
    for r in report:
        user, reported_user = r.split()
        report_dict[reported_user].add(user)
    
    suspended_users = [user for user, reporters in report_dict.items() if len(reporters) >= k]
    
    result = [0] * len(id_list)
    
    for i, user in enumerate(id_list):
        for suspended_user in suspended_users:
            if user in report_dict[suspended_user]:
                result[i] += 1
    
    return result

# https://school.programmers.co.kr/learn/courses/30/lessons/118666?language=python3

def solution(survey, choices):
    scores = {
        'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0
    }
    
    for i in range(len(survey)):
        left, right = survey[i][0], survey[i][1]
        choice = choices[i]
        
        if choice < 4:
            scores[left] += 4 - choice
        elif choice > 4:
            scores[right] += choice - 4
    
    result = ''
    result += 'R' if scores['R'] >= scores['T'] else 'T'
    result += 'C' if scores['C'] >= scores['F'] else 'F'
    result += 'J' if scores['J'] >= scores['M'] else 'M'
    result += 'A' if scores['A'] >= scores['N'] else 'N'
    
    return result

# https://school.programmers.co.kr/learn/courses/30/lessons/150370?language=python3

def date_to_days(date_str):
    year, month, day = map(int, date_str.split('.'))
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    term_dict = {}
    for term in terms:
        term_type, duration = term.split()
        term_dict[term_type] = int(duration)
    
    today_in_days = date_to_days(today)
    expired_indices = []
    
    for i, privacy in enumerate(privacies):
        privacy_date, privacy_type = privacy.split()
        expiration_date_in_days = date_to_days(privacy_date) + term_dict[privacy_type] * 28 - 1
        
        if expiration_date_in_days < today_in_days:
            expired_indices.append(i + 1)
    
    return expired_indices

# https://school.programmers.co.kr/learn/courses/30/lessons/12938?language=python3

def solution(n, s):
    if s < n:
        return [-1]
    
    quotient, remainder = divmod(s, n)
    result = [quotient] * n
    
    for i in range(remainder):
        result[i] += 1
    
    return sorted(result)
