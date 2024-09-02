def duel(team):
    n = len(team)

    if n == 1:
        return team
    
    team1 = duel(team[:n//2])
    team2 = team[n//2:]

    new_team = []
    for i in range(n//2):
        if team1[i][0] < team2[i][0]:
            new_team.append(team1[i])
            new_team.append(team2[i])
        else:
            new_team.append(team2[i])
            new_team.append(team1[i])

    return new_team

def solution(n, win_cnt):
    answer = []

    teams = [(i+1, win_cnt[i]) for i in range(n)]
    teams.sort(key=lambda x: (-x[1], x[0]))
    
    result = duel(teams)
    for r in result:
        answer.append(r[0])
    
    return answer