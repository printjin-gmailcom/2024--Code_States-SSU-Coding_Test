# https://school.programmers.co.kr/learn/courses/30/lessons/12928?language=python3
def solution(n):
    # 문제 이해 -> 문제의 입출력, 특이점
    # - 입력: n
    # - 출력: n의 약수의 총합
    # - 약수: n을 나누었을 때 나머지가 0이 되는 수
    
    # 제한 사항 -> 시간복잡도 등 제한 사항을 고려
    # - n: 3000 
    # - O(n): 3K
    # - O(n^2): 3K * 3K = 9M
    
    # 아이디어 -> 아이디어 혹은 의사코드
    # - answer 초기화하기 0
#     answer = 0
#     # - n만큼 반복(1 - n)
#     for i in range(1, 1 + n):
        
#     #   - 만약 n을 나눈 나머지가 0인 경우 값 더하기
#         if n % i == 0:
#             answer += i
    
    # 아이디어2 : 
    # - 약수의 합을 만들려고 하면
    # - 약수를 찾아서 더했어
    # - 100
    # - 1, 100
    # - 2, 50
    # - 4, 25
    # - 5, 20
    # - 10, 10
    
    import math # math 라이브러리
    # math.sqrt() # 루트 값을 구할 수 있다.
    
    # - sqrt를 찾는다.
    # - sqrt만큼 반복한다.
    #   - 만약에 나머지가 0인 경우, i, n//i를 더한다. 
    #     - i, n//i 같은 경우 i를 한 번 뺀다.
    
    sqrt = int(math.sqrt(n))
    
    answer = 0
    # O(n) -> O(root n)
    for i in range(1, 1 + sqrt):
        if n % i == 0:
            answer += i
            answer += n // i
        if i*i == n:
            answer -= i
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/120817?language=python3
def solution(numbers):
    # 문제 이해
    # - 입력: 리스트
    # - 출력: 리스트의 평균(int)
    
    # 아이디어
    # - 리스트의 총합을 구한다.
    # - 리스트의 총합을 리스트의 길이로 나눈다.
    
    # 제한사항
    # - numbers 원소: 1,000
    # - numbers 길이: 100
    # - O(n*2) 1M

    answer = 0
    for num in numbers:
        answer += num
    
    return answer/len(numbers)



# https://school.programmers.co.kr/learn/courses/30/lessons/12931?language=python3
def solution(n):
    # 문제 이해
    # - 입력: N 자연수
    # - 출력: N의 자릿수의 합
    
    # 아이디어
    # - 숫자를 입력받아서 -> 문자로 치환
    # - 123 -> "123"
    # - 문자 기준으로 반복하면서 자릿수 더하기
    
    # 제한사항
    # - N 100M
    # - O(N) 100M
    # - O(log n) 100M -> 9
    
    answer = 0
    string = str(n) # 문자로 변환
    
    #123 -> 1 2 3
    # 9 9 9 9 9 
    
    for c in string:
        answer += int(c)
    
    # 10으로 나누면서 풀기
    # n
    # 반복 n이 0이 될 때까지
    #   - n % 10을 더하기
    #   - n을 n // 10으로 업데이트
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/81301?language=python3
def solution(s):
    # 문제 이해
    # - 입력: 일부 숫자가 영단어로 바뀐 "문자열"
    # - 출력: 원래 "숫자"
    
    # 아이디어
    # - 영단어 표를 코드로 구현
    #    - 영단어 표: 리스트
    #    - 영단어 표: 딕셔너리
    # - 입력받은 문자를 해당하는 숫자로 대체
    
    # 제한사항
    # - s 길이 50
    
    answer = 0
    
    word_list = ["zero", "one", "two", "three", "four", "five", 
                 "six", "seven", "eight", "nine"]
    # word_dict = {"zero": 0, "one": 1, ...}
    
    for idx, wl in enumerate(word_list):
        s = s.replace(wl, str(idx))
    
    return int(s)



# https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3
def solution(nums):
    # 문제 이해
    # - N개가 주어짐 -> N/2를 선택하는 문제
    # - N에 중복된 요소가 있을 수 있고
    # - 최대한 중복되지 않는 N/2를 찾는 문제구나
    # - 입력: 폰켓몬 리스트
    # - 출력: 내가 고른 폰켓몬 종류의 수
    
    # 아이디어
    # !! 일단 중복되지 않게 골라야함
    # !! 중복되지 않게 고른 후에는 아무거나 골라도 됨
    # 
    # 중복되지 않는 폰켓몬 리스트를 만들기(unique)
    # - unique의 수 n/2이랑 비교
    #   - unique > n/2: n/2
    #   - n/2 > unique: unique
    
    # 제한사항
    # - n: 10,000 -> 10K
    # O(n^2) -> 10K*10K -> 100 M
    
    answer = 0
    
    # 중복없는 폰켓몬 리스트 만들기
    # uniq = []
    # for n in nums:
    #     if n not in uniq:
    #         uniq.append(n)
            
    uniq = set(nums)
    
    selection = len(nums)//2
    uniq_cnt = len(uniq)
    
    if selection > uniq_cnt:
        answer = uniq_cnt
    else:
        answer = selection
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/181839?language=python3
def solution(a, b):
    # 문제이해
    # - 입력으로 a, b 숫자 (1-6)
    # - 출력: 점수
    #   - 둘 다 홀수일 때
    #   - 하나만 홀수일 때
    #   - 홀수가 없을 때
    
    # 아이디어
    # - 홀수 여부 파악하기
    # - 조건에 따라 점수 계산하기
    
    # 제한사항
    # a, b: 6
    # O(1)
    
    answer = 0
    
    a_odd = a % 2 # 홀수이면 1, 짝수이면 0
    b_odd = b % 2
    
    if a_odd == 1 and b_odd == 1:
        answer = a**2 + b**2
    elif a_odd == 1 or b_odd == 1:
        answer = 2*(a+b)
    else:
        answer = abs(a-b)
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/12938?language=python3
"""
문제 이해
- 최고의 집합: 원소의 합이 S / 원소의 곱이 최대
- 입력: n 원소의 수 / s 원소의 합
    
아이디어
- s를 n개의 원소로 나누었을 때, 원소가 거의 비슷한 값을 가져야 곱이 최대가 됨
- s를 n으로 나눈 몫으로 모든 집합을 채우고, 나머지를 1씩 분배하기
  - n: 3, s: 10
  - 10//3 -> 3 ; 10%3 -> 1
  - 3, 3, 3 > 4, 3, 3
- 합이 n보다 작은 경우; n=2, s=1인 경우 존재하지 않음
- 정렬하기
"""
def solution(n, s):
    if s < n:
        return [-1]
    
    # 기본 값으로 몫을 모든 원소에 채우기
    quotient = s // n
    remainder = s % n
    
    # 기본 값을 리스트에 넣고, 나머지를 분배
    answer = [quotient] * n
    
    for i in range(remainder):
        answer[i] += 1
    
    # 오름차순 정렬하여 반환
    answer.sort()
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/150370?language=python3
"""
문제 이해
- 모든 달은 28일까지 있음
- 개인정보 타입별로 유효기간이 다름
- 유효기간이 지나면 파기해야함

- 입력
  - today: 오늘날짜 -> yyyy.mm.dd
  - terms: 약관별 유효기간 -> "약관타입 v 유효기간(개월)" [리스트]
  - privacies: 동의한 약관들 -> "동의날짜 v 약관 타입" [리스트]
- 출력
  - 파기해야하는 약관의 번호
  
- 약관 번호를 1 ~ n으로 사용해야함

아이디어
- 약관 종류랑 유효기간을 저장할 수 있는 공간 (termsTable) {type:month}
- 개인정보 수집일자 + 유효기간 < 오늘 : 파기
- 출력하기
** 연월일 -> 일
  - 1년: 12개월 * 28일
  - 1개월: 28일
  - "일"

제한사항
- terms: 20 n
- privacies: 100 m
"""
def solution(today, terms, privacies):
    # termsTable 만들기 {type:month}
    termsTable = {}
    for t in terms:
        t = t.split()
        termsTable[t[0]] = int(t[1])
    
    # 오늘날짜를 days로 바꾸기
    today_year, today_month, today_day = map(int, today.split("."))
    today2days = today_year*12*28 + today_month*28 + today_day
    
    answer = []
    
    # privacies를 반복하기
    for idx, prv in enumerate(privacies):
        
        date, term_type = prv.split()
        date_year, date_month, date_day = map(int, date.split("."))
        date2days = date_year*12*28 + date_month*28 + date_day
        
        exp_day = date2days+ termsTable[term_type]*28
        
        if exp_day <= today2days:
            answer.append(idx + 1)
            
    # - 개인정보 수집일자 + 유효기간을 오늘날짜랑 비교하기
    #   - 오늘보다 이전이면 파기가 필요한 것으로 확인하기** "idx+1"
    
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/118666?language=python3
"""
문제 이해
- 입력
  - survey: 질문지 타입 [리스트/문자]
  - choices: 선택한 답변 [리스트/숫자] 1-7
- 출력
  - result: 점수를 기반으로 4자리 문자열
 
아이디어
- 성격 유형 테이블을 만들기(surveyTable)
- RT => 1 -> R:3 / => 7 -> T3
- 1 ~ 7 (-4) => -3 ~ 3
  - 점수가 음수일 때는 : 앞에 유형에 점수를 더해준다!
  - 점수가 양수일 때는 : 뒤에 유형에 점수를 더해준다!
  - 성격 유형 테이블을 완성
- RT / CF / JM / AN 의 성격점수를 비교해서 최종 성격타입을 만들어준다.

제한사항
- survey : 1,000 : 1K
- O(n*2): 1K*1K : 1M
"""
def solution(survey, choices):
    # 설문조사 결과 테이블 만들기 (초기화)
    surveyTable = {
        "R":0, "T":0,
        "C":0, "F":0,
        "J":0, "M":0,
        "A":0, "N":0
    }
    
    # survey & choice를 함께 반복하기
    #  - 조건에 따라 점수주기
    #    - (-4) 기준 점수를 만들고
    #    - 음수일 때 앞 유형 / 양수일 때 뒷 유형에 점수 주기
    for i in range(len(survey)):
        survey_type = survey[i]
        type_a = survey_type[0]
        type_b = survey_type[1]
        
        score = choices[i] - 4
        # 1 ~ 7 ; -3 ~ 3
        
        if score <= 0:
            surveyTable[type_a] += abs(score)
        else:
            surveyTable[type_b] += abs(score)
        
    # 성격 유형별로 조건을 확인해서 result 만들기
    answer = ''
    if surveyTable["R"] >= surveyTable["T"]:
        answer += "R"
    else: answer += "T"
    if surveyTable["C"] >= surveyTable["F"]:
        answer += "C"
    else: answer += "F"
    if surveyTable["J"] >= surveyTable["M"]:
        answer += "J"
    else: answer += "M"
    if surveyTable["A"] >= surveyTable["N"]:
        answer += "A"
    else: answer += "N"
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/92334?language=python3
"""
문제 이해하기
- 입력
  - id_list: 유저의 목록[리스트]
  - report: 유저가 신고한 목록 [리스트] "신고한사람 신고당한사람"
  - k: 정지 기준이 되는 신고 횟수
- 출력
  - 신고가 모두 끝난 후 유저가 받게되는 정지 안내 메일 수[리스트]
- 한 사람이 여러명을 신고할 수 있음
- 한 사람이 한명을 여러번 신고할 수는 없음(중복 불가)
- 신고가 모두 완료된 후에 정지메일을 받음

아이디어
- 신고 받은 사람의 신고 횟수
- reporter가 신고한 사람 중에 정지당한 사람의 수를 세기

제한 사항
- id_list: n: 1,000 1K
- report: 200,000 200ㅏ
- O(n*M) = 1K * 200K = 200M

"""
def solution(id_list, report, k):
    answer = []
    # reportTable: {신고 당한 사람: [신고한 사람]}
    reportTable = {}
    for id in id_list:
        reportTable[id] = []
        
    # reportTable 채우기
    for rep in set(report):
        reporter, reported = rep.split()
        reportTable[reported].append(reporter)
    
        
    # 신고 당한 사람이 unique하게 몇번 신고당했는지 확인
    # bannedTable: 유저리스트 -> 누가 정지됐는지 확인하는 테이블
    
    bannedTable = {} # {신고 당한 사람:신고 여부(True/False)}
    for id in id_list:
        if len(reportTable[id]) >= k:
            bannedTable[id] = True
        else:
            bannedTable[id] = False
    
    #  - k랑 비교
    # id_list를 기준으로 내가 신고한 사람 중에 몇명이나 정지됐는지 확인
    mailCntTable = {} # {신고한 사람: 받은 메일 수}
    for id in id_list:
        mailCntTable[id] = 0
        
    for reported, reporters in reportTable.items():
        if bannedTable[reported]:
            for rep in reporters:
                mailCntTable[rep] += 1
    
    for id in id_list:
        answer.append(mailCntTable[id])
    
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/178871?language=python3
"""
문제 이해
- 입력
  - players: 현재 순위 [리스트]
  - callings: 추월한 선수 이름 [리스트]
- 출력
  - result: 최종 순위 [리스트]

아이디어
- calling을 반복하기
  - calling에서 불려진 선수를 찾아서 앞의 선수랑 순서를 바꿔주면됨
  ** 아이디어: 불려진 선수를 쉽게 찾기 위해서 rank라는 딕셔너리 만들기
    rank: {플레이어 이름: 인덱스}

제한 사항
- n: players : 50,000 : 50K
- m: callings : 1,000,000 : 1M
- O(n*M) = 50K * 1M = 50G > 아이디어 필요할 것!

"""
def solution(players, callings):
    # - rank 딕셔너리 만들기 {플레이어 이름: 인덱스}
    ranks = {}
    for idx, player in enumerate(players):
        ranks[player] = idx
    
    # - calling만큼 반복
    for call in callings:
        cur_rank = ranks[call]
        tar_rank = cur_rank - 1
        tar_player = players[tar_rank]
        
        players[cur_rank], players[tar_rank] = players[tar_rank], players[cur_rank]
        
        ranks[call] = tar_rank
        ranks[tar_player] = cur_rank
        
    #   - rank[player] : 선수의 순위를 찾기
    #   - 선수의 순위를 앞선 선수랑 바꾸기: players
    #   - 바뀐 순위를 rank에 업데이트 해주기
    
    return players



# https://school.programmers.co.kr/learn/courses/30/lessons/86051?language=python3
"""
문제 이해
- 입력: 0-9까지 중복되지 않는 숫자 리스트
- 출력: 0-9까지 중에 리스트에 포함되지 않는 수의 합

아이디어
ver1. 리스트 이용하기
- 요소가 10개 리스트 0-9 등장여부를 확인
- 등장 안한 요소만 조회해서 더하면 답을 구할 수 있지 않을까?

ver2. 세트 이용하기
- full_set {0, 1, 2, 3..., 9}
- numbers = [특정 숫자가 빠진 리스트]
- sum(full_set - numbers)

제한 사항
- n:9 내가 하고 싶은대로 풀어야지 !

"""

def solution(numbers):
    # ver1.
#     checker = [0]*10 # 여기다가 등장여부를 업데이트
    
#     for num in numbers:
#         checker[num] += 1
    
#     answer = 0
#     for idx, chk in enumerate(checker):
#         if chk == 0:
#             answer += idx
    
    full_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    numbers = set(numbers)
    
    diff = full_set.difference(numbers)
    print(diff)
    
    answer = sum(diff)
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/118667?language=python3
"""
문제이해
- 큐가 두개 주어짐
- 두 큐 중 하나를 골라 하나에서 dequeue, 다른 하나로 enqueue
  - 두 큐의 원소의 합을 같도록 조정
  - dequeue and enqueue를 하나로 침
- 두 큐의 합을 2로 나눈 값 -> 우리가 만들어야되는 큐 하나의 합

- 입력: queue1, queue2 ; [리스트]
- 출력: 최소 횟수
  - 각 큐의 원소의 합을 같게 만들 수 없는 경우 -1

아이디어
- 만약에 두큐의 합이 홀수면 -> 실패
- 반복을 계속하다가 결국 답이 안나왔을 때 -> 실패
- MAX Iter: queue*3
"""

from collections import deque

def solution(queue1, queue2):
    answer = -2
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total_sum = sum1 + sum2
    
    # 두 큐의 합 / 2가 홀수인 경우
    if total_sum % 2 == 1:
        return -1
    
    # 반복을 통해 만들어야하는 목표합
    goal = total_sum // 2
    
    # 종료를 위한 최대 반복 수
    MAX_ITER = len(queue1) * 3
    
    # queue1 > goal: queue1 -> queue2
    # queue1 < goal: queue2 -> queue1
    
    iteration = 0
    while iteration < MAX_ITER:
        if sum1 > goal:
            item = queue1.popleft()
            sum1 -= item
            queue2.append(item)
            sum2 += item
        elif sum1 < goal:
            item = queue2.popleft()
            sum2 -= item
            queue1.append(item)
            sum1 += item
        elif sum1 == goal:
            return iteration
        
        iteration += 1
    
    
    return -1



# https://school.programmers.co.kr/learn/courses/30/lessons/42584?language=python3
"""
문제이해
- 입력: 초당 주식가격이 저장된 [리스트] 숫자
- 출력: 주식 가격이 떨어지지 않은 단위 기간(초) 수 
아이디어
- [1, 2, 3, 2, 3]
- [4, 3, 1, 1, 0]

- stack = [(0, 1), (1, 2), (3, 2), (4, 3)
- (3, 2): 스택 안에서 나보다 주식가격이 큰 기수를 빼기
  - stack.pop(): 주식 가격이 유지된 기간을 계산(3-2)

- 기본적으로 해당 초수의 주식가격을 쌓을거에요
- 스택 안에 나보다 가격이 큰 기간이 저장되어있으면 -> 해당 기간의 가격은 유지되지 못함
  - pop해주고 cur - popped (기간)
- 종료된 후에도 Stack 남아있는 값들은 마지막 종료 시기를 기준으로 유지기간을 계산

- 스택에 있는 주식들은 아직 가격이 떨어지지 않은 주식

제한사항
- prices n: 100,000 100K
- O(n*n) = 100K*100K = 10,000 M
"""
def solution(prices):
    # - 기본적으로 해당 초수의 주식가격을 쌓을거에요
    # - 스택 안에 나보다 가격이 큰 기간이 저장되어있으면 -> 해당 기간의 가격은 유지되지 못함
    #   - pop해주고 cur - popped (기간)
    # - 종료된 후에도 Stack 남아있는 값들은 마지막 종료 시기를 기준으로 유지기간을 계산
    
    # answer를 초기화
    answer = [0] * len(prices)
    stack = [] # (sec, price) x sec
    
    # 주식이 유지되지 못한 기간을 업데이트
    for sec in range(len(prices)): # i 0 ~ len(prices) sec
        while stack and prices[sec] < stack[-1][1]:
            popped = stack.pop()
            answer[popped[0]] = sec - popped[0]
            
        stack.append((sec, prices[sec]))
        
    # 끝까지 주식가격이 유지된 시간 업데이트
    while stack:
        popped = stack.pop()
        answer[popped[0]] = (len(prices) - 1) - popped[0]
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/42587?language=python3
"""
문제이해 / 아이디어
- queue에서 프로세스 하나 꺼내기 (dequeue)
- 대기중인 queue 조회
  - 우선순위가 높은 프로세스가 있으면 (enqueue)
  - 없으면 실행하기  
- location에 해당하는 프로세스가 몇번째로 실행되는지 확인하기

- [A(2), B(1), C(3), D(2)]
  - A(2), [B(1), C(3), D(2)]
- [B(1), C(3), D(2), A(2)]
  - B(1), [C(3), D(2), A(2)]
- [C(3), D(2), A(2), B(1)]
  - C(3), [D(2), A(2), B(1)] # 1
- [D(2), A(2), B(1)]

- 입력
  - priorities: 숫자 [리스트]
  - location: 언제 실행되는지 궁금한 프로세스
- 출력
  - location에 해당하는 프로세스가 실행되는 순서
  
제한사항
- priorities : n : 100
"""

from collections import deque

def solution(priorities, location):
    # [2, 1, 3, 2]
    # [0:2, 1:1, 2:3, 3:2]
    
    # 큐 채우기
    queue = deque([]) # (loc, pri)
    for loc, pri in enumerate(priorities):
        queue.append((loc, pri))
    

    # - queue에서 프로세스 하나 꺼내기 (dequeue)
    # - 대기중인 queue 조회
    #   - 우선순위가 높은 프로세스가 있으면 (enqueue)
    #   - 없으면 실행하기  
    # - location에 해당하는 프로세스가 몇번째로 실행되는지 확인하기
    
    order = 0
    
    while queue:
        cur = queue.popleft()
        
        if any(cur[1] < q[1] for q in queue):
        # if cur_priority < max(queue_priority):
            queue.append(cur)
        else:
            order += 1
            if cur[0] == location:
                return order
            


# https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=python3
            """
문제이해
- 입력: 
  - progresses: 현재 작업의 진행상황 [리스트] 숫자
  - speeds: 각 작업의 수행 속도 [리스트] 숫자
- 출력:
  - 배포가 일어날 때 배포되는 기능의 수

아이디어
- 1기수마다 progresses의 현황을 업데이트하기 (speed 만큼)
- 배포 가능한 기능 배포하기 (queue)
  - 배포된 기능이 있다면 숫자세서 추가하기

제한사항
- n: 100
"""

# from collections import deque # queue를 사용하기 위해 deque 가져오기

def solution(progresses, speeds):
    # - 1기수마다 progresses의 현황을 업데이트하기 (speed 만큼)
    # - 배포 가능한 기능 배포하기 (queue)
    # - 배포된 기능이 있다면 숫자세서 추가하기
    answer = []
    # progresses = deque(progresses)
    # speeds = deque(speeds)
    
    while progresses: # 모든 작업이 완료될 때까지 반복
        # 작업상태 업데이트
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            if progresses[i] > 100:
                progresses[i] = 100
            
        cnt = 0
        
        while progresses and progresses[0] == 100: # peek
            progresses.pop(0) # dequeue
            speeds.pop(0)
            cnt += 1
        
        if cnt > 0:
            answer.append(cnt)
            
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=python3
"""
문제이해
- 올바른 괄호 -> (, )의 짝이 맞음
- 올바르지 괄호 -> 닫히는 괄호로 시작 or 열린 괄호가 닫히지 않거나

- 입력: [리스트] (, )
- 출력: 올바른 괄호 여부 [Bool]

아이디어
- Stack
  - "열린 괄호"를 만나면 push
  - "닫힌 괄호"를 만나면 pop
    - 닫히는 괄호로 시작: stack이 비어있는데 pop하는 경우
    - 열린 괄호가 닫히지 않거나: 반복이 종료되었는데 stack에 값이 있는 경우
  - case
    - ()()
      stack = [ :
    - (())()
      stack = [ :
    - )()(
      stack = [ : X
    - (()(
      stack = [ a a:
    
      
제한사항
- s: 100,000 100K
- O(n*n) = 100M 
"""
def solution(s):
#     stack = []
    
#     for pa in s:
#         if pa == "(":
#             stack.append("()")
#         else:
#             if not stack:
#                 return False
#             stack.pop()
    
#     if stack:
#         return False
    stack = 0
    for pa in s:
        if pa == "(":
            stack += 1
        else:
            if stack == 0:
                return False
            stack -= 1
    
    if stack:
        return False
            
    return True



# https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=python3
"""
문제이해
- 0에서 9로 이루어진 배열이 주어짐
- 연속된 숫자는 하나만 남기고 제거
- 입력: 숫자 [리스트]
- 출력: 연속이 제거된 [리스트]

아이디어
- 스택 필요
- arr을 반복 조회(순회)
  - if 스택에 현재 쌓여있는 요소의 값과 다르면 push
  - peek != arr -> push

제한사항
- arr: n: 1M
- O(n)
"""
def solution(arr):
    answer = [] # 스택
    
    for ar in arr:
        if not answer:
            answer.append(ar)
        else:
            if answer[-1] != ar:
                answer.append(ar)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/49191?language=python3
"""
권투 선수들의 게임 결과를 입력받음
-> 순위를 특정할 수 있는 권투 선수의 수를 찾아내는 문제 였습니다.

- 권투 선수들의 승패 -> 이 사람의 실력을 표현할 수 있는 수단

다익스트라 알고리즘을 변형한 플로이드-워셜 알고리즘을 사용
*기준 선수와 다른 선수 모두와의 관계가 연결되어 있다면 -> 내 순위를 알 수 있을 것이다.

> 다익스트라 알고리즘: 기준점에서부터 각 노드까지의 최단경로를 구해내는 알고리즘
기준점(a) -> 다른 노드(a, b, c, .., z)까지의 최단경로; 리스트 [0, 10, 20..] 
> 플로이드-워셜 알고리즘: 모든 노드 사이의 최단경로를 모두 구해내는 알고리즘
모든 노드 사이; 행렬/2차원 리스트
[
    [a-a, a-b, a-c, ..., a-z],
    [b-a, b-b, b-c, ..., b-z]
    ...
    [z-a, ..., z-z]

]
"""

def solution(n, results):
    
    # 그래프 만들기 / 인접 행렬로 구현 (n+1 * n+1 행렬)
    graph = []
    for i in range(n+1):
        graph.append([float("inf")]*(n+1))
    
    # 스스로에게 가는 거리는 0으로 초기화
    for i in range(1, n+1):
        graph[i][i] = 0
    
    # results를 통해서 결과를 업데이트
    for a, b in results:
        graph[a][b] = 1
    
    # 플로이드-워셜 알고리즘!
    # a, b, c -> a에서 c로 가는데 b를 거쳐가는 경우
    for b in range(1, n+1):
        for a in range(1, n+1):
            for c in range(1, n+1):
                if graph[a][c] > graph[a][b] + graph[b][c]:
                    graph[a][c] = graph[a][b] + graph[b][c]
    
    # print(graph)
    
    # graph를 활용해서 검증하기
    answer = 0
    
    for i in range(1, n+1):
        count = 0
        for j in range(1, n+1):
            if graph[i][j] != float("inf") or graph[j][i] != float("inf"):
                # 내가 승리했거나 간접적으로 승리한 경우 graph[i][j]가 숫자로 저장
                # 내가 패배했거나 간접적으로 패배한 경우 graph[j][i]가 숫자로 저장
                count += 1
    
        if count == n:
            # 만약에 1번 선수가 1, 2, 3, 4, 5번 선수에 대해서 모두 승리/패배를 알 수 있다면
            # 내 순위를 알 수 있을거야!
            # 1: 0 2:1 3:inf 4:-1 5:-2
            answer += 1
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/49189?language=python3
from collections import deque

def solution(n, edge):
    
    # 빈 그래프 만들기
    graph = []
    for _ in range(n+1):
        graph.append([])
    
    for a, b in edge: # graph : [node]
        graph[a].append(b)
        graph[b].append(a)
    
    # distance 업데이트
    dist = [float("inf")]*(n+1)
    dist[1] = 0
    
    # queue 초기화
    queue = deque([])
    queue.append((1, 0))
    
    while queue:
        cur_node, cur_dist = queue.popleft()
        
        for next_node in graph[cur_node]:
            tot_dist = cur_dist + 1
            if tot_dist < dist[next_node]:
                dist[next_node] = tot_dist
                queue.append((next_node, tot_dist))
        
    
    MAX = max(dist[1:])
    answer = 0
    
    for d in dist:
        if d == MAX:
            answer += 1
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/42626?language=python3
""" 10분까지 읽고 아이디어 생각해보기
- new_scov = min1 + min2*2
- 모든 음식의 scov >= K
- 몇 번이나 음식 조합을 반복해야할까?

- 입력: scoville 음식리스트 / K 최소 스코빌지수
- 출력: 모든 음식이 scoville 지수 K이상이 되기위한 조합 횟수

반복 : 모든 음식이 K보다 클 때까지
  - 음식리스트를 정렬 -> min1, min2 
  - min1 < K
  - new_scov = min1 + min2*2
  - new_scv -> 음식리스트

항상 정렬하는 대신 -> 음식 리스트를 Heap구조로 유지해서 min을 빠르게 찾아내자!


종료 조건: len(scoville) == 1
 -1

"""
import heapq

def solution(scoville, K):
    
    heap = []
    for scov in scoville:
        heapq.heappush(heap, scov)
    
    # heapq.heapify(scoville) # heapify를 사용하는 경우
    
    answer = 0
    while heap[0] < K:
        if len(heap) == 1:
            return -1
        
        min1 = heapq.heappop(heap)
        min2 = heapq.heappop(heap)
        
        new = min1 + min2*2
        
        heapq.heappush(heap, new)
        answer += 1
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/12978?language=python3
""" 23분까지 문제 읽어보기
다익스트라 알고리즘: 최단경로 탐색 활용
- 마을이랑 마을 사이의 소요시간(경로)가 주어지고
- 주어진 제한시간 K 안에 배달할 수 있는 마을의 숫자를 찾는 문제

- 입력
  - N: 마을 갯수 -> Node의 수
  - road: 경로 정보 -> Edge의 정보
  - K: 제한 시간
 - 출력
  - 기준마을 1번으로 부터 소요시간이 K 이하인 마을의 수
    
    자료구조 초기화
    # 경로가 저장되어있는 그래프
    # 각 노드까지 거리를 저장할 공간
    # 그래프를 순회할 큐
    
    다익스트라 알고리즘 수행
    -> distance 완성
    
    K 이하인 마을의 수 세기
    -> distance에서 조회

"""

from collections import deque

def solution(N, road, K):
    # 자료구조 만들기
    
    # 그래프 만들기 # 인접 리스트
    # N+1개의 빈 리스트 만들어짐
    graph = []
    for i in range(N + 1):
        graph.append([])
    
    for a, b, c in road: # from, to, dist
        graph[a].append((b, c)) # (node, dist)
        graph[b].append((a, c))
        # 방향성이 없으므로 양쪽 전부 더하기
    
    # 노드까지 거리를 저장
    distance = [float("inf")] * (N+1)
    distance[1] = 0 # 기준점 1번 노드
    
    # graph를 순회할 queue
    queue = deque([])
    queue.append((1, 0)) # node, dist # 1번 노드를 입력
    
    # 다익스트라 알고리즘을 실행!
    while queue:
        cur_node, cur_dist = queue.popleft()
        
        for node, dist in graph[cur_node]:
            new_dist = cur_dist+ dist
            if distance[node] > new_dist:
                distance[node] = new_dist
                queue.append((node, distance[node]))
                             
    # 문제 조건에 맞게 결과 출력
    answer = 0
    for d in distance:
        if d <= K:
            answer += 1
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/76501?language=python3
""" 40분까지 직접 문제 풀어보기
- absolutes: 정수의 절대값
- signs: 부호 ; True 양수 / False 음수

- result: signs를 적용한 absolutes의 총합
"""
def solution(absolutes, signs):
    answer = 0
    # for i in range(len(absolutes)):
    #     if signs[i]:
    #         answer += absolutes[i]
    #     else:
    #         answer -= absolutes[i]
    
    for value, sig in zip(absolutes, signs):
        if sig:
            answer += value
        else:
            answer -= value
            
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/87946?language=python3
"""46분까지 문제 읽어보기 & 아이디어 생각하기
문제이해
- 최소 필요 피로도: 던전에 입장하기 위해 최소한 필요한 피로도 / 입장 조건
- 소모 피로도: 던전을 탐험한 후에 소모되는 피로도 / 실제 소모되는 피로도
- 던전은 한 번씩만 탐험할 수 있음

- 입력:
  - k: 현재 피로도
  - dungeons: (최소, 소모) [리스트]
- 출력
  - 최대로 들어갈 수 있는 던전 수

아이디어
- 던전이 최대 8개임
- 8개짜리 순열!
- 순열을 반복
  - 최소 피로도를 넘는지
  - 넘으면 피로도 깎고
- 최대 탐험 던전 수

제한조건
- dungeons: n 8 8!

"""

from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    # 반복이 필요한 순열만큼 반복 -> 던전을 탐색하는 방법
    for perm in permutations(dungeons):
        tired = k
        count = 0
        
        # 각 던전에 대해서 피로도를 계산; 입장 가능한 던전 수를 계산
        for minimum, consumption in perm:
            if tired >= minimum:
                tired -= consumption
                count += 1
            else:
                break
        
        # 최대 값을 업데이트
        answer = max(answer, count)

    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/42840?language=python3
"""27분까지!
문제이해
- 수포자!
- #1: 1, 2, 3, 4, 5 반복
- #2: 2, 1, 2, 3, 2, 4, 2, 5 반복
- #3: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 반복

- 출력: 가장 높은 점수를 받은 사람 리스트

아이디어
- Brute Force!!!!!
- 문제랑 답이랑 다 비교하자!!!!!!
  - 패턴에 따라 답을 내니까 -> 문제번호 % 패턴 수 => 어떻게 답했는지 확인

n: 10,000 10K
O(n^2) -> 100M
"""
def solution(answers):
    supo = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    correct = [0] * 3
    
    for idx, ans in enumerate(answers):
        # idx: 문제번호 / ans: 정답
        for i in range(3):
            if ans == supo[i][idx%len(supo[i])]:
                correct[i] += 1
    
    MAX = max(correct) # 가장 많이 맞춘 정답 수
    answer = []
    
    for idx, cor in enumerate(correct):
        if cor == MAX:
            answer.append(idx+1)
            
    answer.sort()
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/12950?language=python3
"""
2차원 리스트(행렬) 더하기!
arr1, arr2

[
    [1, 2],
    [2, 3]
]
"""
def solution(arr1, arr2):
    len_row = len(arr1)
    len_col = len(arr1[0])
    
    answer = []
    for i in range(len_row):
        row = []
        for j in range(len_col):
            row.append(arr1[i][j] + arr2[i][j])
        answer.append(row)
        
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/12946?language=python3
"""15분까지 읽어보기
- 하노이 탑의 조건
  - 1. 한 번에 하나의 원판만 옮길 수 있음
  - 2. 큰 원판이 작은 원판 위에 있어서는 안됨

[1번 막대]--
[2번 막대]--
[3번 막대]--4321

hanoi(4) = hanoi(3)->2 + 4->3 + hanoi(3)->3
hanoi(3) = hanoi(2) + 3->2 + hanoi(2)

"""

answer = []
# n: 1 -> 3
def hanoi(n, a, b, c):
    if n == 1:
        answer.append([a, c]) # 원판 옮기기
        return
    
    # n: 원판의 갯수, a: 현재 위치, b: 거쳐갈 곳, c:목적지
    hanoi(n-1, a, c, b) # a->b
    answer.append([a, c]) # 원판 옮기기
    hanoi(n-1, b, a, c) # b->c
    

def solution(n):
    hanoi(n, 1, 2, 3)
    return answer



# [제목 없는 데이터베이스](https://www.notion.so/1a6c644ae2274f6082e83330ecc2fa48?pvs=21)

- ***알고리즘 문제 리스트***
    
    [알고리즘 문제리스트](https://www.notion.so/10902108b4174557847c4f9a0cf6510a?pvs=21)
"""
- 영역에 있는 모든 수가 같으면, 하나로 압축
- 다른 수가 있다면 4개로 나눠서 -> 압축 가능한지 확인

- 결과: 압축한 결과 0과 1의 갯수


아이디어 array, size
---
- 영역을 전체 검사해서 압축할 수 있는지 확인
  - 압축가능하면(모두 동일하면 압축)
  - 압축 불가능하면,
    - 영역을 넷으로 나누기
    - 각각 압축할 수 있는지 확인
---

"""

# recursive function 만들기
def quad_comp(arr, x, y, size, answer):
    
    # 압축 가능한지 확인
    value = arr[x][y]  # 네모의 첫 칸의 값을 확인
    
    same = True
    for i in range(size):
        for j in range(size):
            if arr[x+i][y+j] != value:
                same = False
                break
        if not same:
            break
            
    if same: # 종료 조건
        # 압축 가능
        answer[value] += 1
        
    else: # recursive call
        quad_comp(arr, x, y, size//2, answer)
        quad_comp(arr, x+size//2, y, size//2, answer)
        quad_comp(arr, x, y+size//2, size//2, answer)
        quad_comp(arr, x+size//2, y+size//2, size//2, answer)
        
    return

def solution(arr):
    answer = [0, 0]
    quad_comp(arr, 0, 0, len(arr), answer)
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/132267?language=python3
# 파이썬은 내부적으로 1,000회까지만 recursive call이 가능
# import sys
# sys.setrecursionlimit(100000)

"""33분까지
- 병을 2개 -> 1를 새로줌
- 빈병 20개 -> 몇개를 줄까?
- 20 -> 10 n//2 + n%2
- 10 -> 5
- 5 -> 2 + 1
- 3 -> 1 + 1
- 2 -> 1

- 입력:
  - a: 콜라를 받기위한 조건 (2)
  - b: 주는 콜라 수 (1)
  - n: 내가 가지고 있는 콜라 수 (20)
  
- n개의 콜라를 가지고 있을 때
  - 새로운 콜라: (n//a) * b
  - 빈병: n % a
  - 최종 빈병: (n//a) *b + n%a
  -> 다시 마트에 콜라 바꿔주세요!!
  -> 종료: n < a
"""

# recursive function
# def solution(a, b, n):
#     # 더이상 바꿀 수 있는 콜라가 없는 경우 종료
#     if n < a:
#         new_cola = 0
#         return new_cola
    
#     # 새로 받은 콜라를 마시고 난 후의 빈병 + 나머지
#     new_cola = (n//a) * b
#     empty_bottle = new_cola + n%a
    
#     return new_cola + solution(a, b, empty_bottle)

def solution(a, b, n):
    total_cola = 0
    
    while n >= a: # 종료 조건
        new_cola = (n//a) * b
        total_cola += new_cola
        
        n = new_cola + (n % a)
        
    return total_cola



# https://school.programmers.co.kr/learn/courses/30/lessons/150365?language=python3
"""
n*m: 격자 미로
x*y -> r*c

- 격자 밖으로 나갈 수 없음
- 목적지까지 이동거리가 k여야 함
- 같은 격자를 두 번이상 방문해도 됨 -> vistied 관리하지 않아도 되겠다.
- 탈출 경로가 문자열 오름차순이어야함
  - l, r, u, d > [d, l, r, u]
- 탈출 경로를 찾을 수 없을 때는 "impossible" 출력

- 기준 노드에서 각각 d, l, r, u 순으로 다음 스텝을 조회한다고 생각하기

- solution: # 종료조건, 성공조건
  - E에 도달 해야함 & k번 만에 도달해야 함
  
- validation: # 다음 노드로 이동할 수 있는 조건(이동할 수 없는)
  - 남은 거리를 r번 만에 도달할 수 없을 때
    - r < dist(남은 거리) (종료)
    - (dist - r)%2 != 0 (종료)
  # - k번 탐색했는데, E에 도달하지 못한 경우(종료)
  - 다음 탐색 범위가 미로를 벗어나면(종료) 1 <= x <= m, 1<= y <= n

    
- DFS 구현하기
  - 성공 조건 검증(종료)
  - 종료 조건 검증(종료)
  - dfs
    -> d, l, r, u 순으로 탐색(재귀 호출)
"""
import sys
sys.setrecursionlimit(10000) #default: 1000회

def dfs_maze(maze, cur, goal, k, cnt, path):
    # 남은 거리와 현재 스텝을 비교하여 종료
    dist = abs(goal[0] - cur[0]) + abs(goal[1] - cur[1])
    remains = k - cnt
    if remains < dist:
        return ''
    if (dist-remains) % 2 != 0:
        return ''
    
    # 현재 위치가 미로를 벗어나지 않았는지 확인하여 종료
    if not(1 <= cur[0] <= maze[0]) or not(1 <= cur[1] <= maze[1]):
        return ''
    
    # 성공: k번만에 목적지에 도달
    if cnt == k:
        if cur == goal:
            return path
    
    # 다음 노드를 (d, l, r, u) 순으로 탐색한다.
    direction = [("d", 1, 0), ("l", 0, -1), ("r", 0, 1), ("u", -1, 0)]
    for d, dx, dy in direction:
        new_path = dfs_maze(maze, (cur[0]+dx, cur[1]+dy), goal, k, cnt+1, path+d)
        # path가 있을 때(성공했을 때) 성공 path를 넘겨준다.
        if new_path:
            return new_path
        
    return ''


def solution(n, m, x, y, r, c, k):
    answer = dfs_maze((n, m), (x, y), (r, c), k, 0, "")
    # '' -> 실패한 경우
    # '' False
    # if not False: True
    if not answer:
        return "impossible"
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/43164?language=python3
"""DFS & Backtracking

그래프화 시켜야함
* (dep -> arr)
모든 엣지를 다 사용할 것

solution
  - answer의 갯수 -> 방문한 나라의 갯수가 몇개면?
  - ticket수 + 1
  - len(answer) == target + 1:
  
validation
backtracking
"""

def dfs_journey(journey, start, visited, answer, target):
    # solution: 종료 조건
    # 모든 탑승권을 사용한 경우
    if len(answer) == target + 1:
        return True
    
    # validation & backtracking
    if start in journey: 
        for i, arr in enumerate(journey[start]):
            if not visited[start][i]:
                visited[start][i] = True # 탑승권 사용
                answer.append(arr) # 여정에 추가
                
                # 다음 여정지로 이동
                if dfs_journey(journey, arr, visited, answer, target):
                    return True
                    # 다음 dfs가 정답 여정지를 포함하고 있다면 종료시키기
                    # 종료되면 상위에서 호출된 재귀함수까지 모두 종료됨
                
                # backtracking
                visited[start][i] = False
                answer.pop()
                
    return False

def solution(tickets):
    answer = []
    
    # 자료구조 전처리
    # 그래프와 방문데이터를 딕셔너리로 구성
    journey = {}
    visited = {}
    for dep, arr in tickets:
        if dep not in journey:
            journey[dep] = []
            visited[dep] = []
        
        journey[dep].append(arr) # 다음 노드에 대한 정보를 리스트로 저장
        visited[dep].append(False) # 다음 노드에 대한 방문 정보를 리스트로 저장
    
    for dep in journey:
        journey[dep].sort()
        # Backtracking을 실행할 때 알파벳 순서가 앞서는 경로를 먼저 선택하기 위함
        # Backtracking의 경우에는, 최적의 해를 찾으면 알고리즘이 종료
        # 알파벳 순서가 앞서는 경로를 찾으면, 다른 경로를 찾지 않고 알고리즘을 종료
    

    answer = ["ICN"]
    dfs_journey(journey, "ICN", visited, answer, len(tickets))
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=python3
""" 10분까지
- 연결되어있는 노드들끼리는 같은 네트워크다!
- 주어진 데이터에서 네트워크는 몇개?

- DFS 탐색을 시작!
- 탐색이 완료된 후에도 방문되지 않은 노드가 있다면, 서로 다른 네트워크에 위치

- computer: 2차원 -> 인접 행렬

** DFS는 완전탐색을 진행하니까 DFS를 완료하고나면 연결된 모든 노드를 방문한 상태가 된다.
"""

def dfs_network(computer, start, visited):
    visited[start] = True
    for i in range(len(computer[start])):
        if not visited[i] and computer[start][i] == 1:
            dfs_network(computer, i, visited)
    

def solution(n, computers):
    answer = 0
    visited = [False]*n
    
    for i in range(n):
        if not visited[i]:
            dfs_network(computers, i, visited)
            answer += 1
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/87946?language=python3
"""
- 금요일: 순열(permutations)을 활용한 완전 탐색
- 오늘: DFS를 활용해서 완전 탐색

- graph: 모든 던전이 연결되어있는 그래프라고 생각하자
- dfs -> 가장 깊숙히; 더 이상 들어갈 수 없을 때까지 던전을 방문하고 입장 횟수의 최댓값 찾기

- 종료 조건 -> 더 이상 들어갈 던전이 없거나 남은 던전의 최소 피로도가 현재 피로도보다 높다.

"""
def dfs_dungeons(k, dungeons, visited, cnt):
    max_count = cnt
    
    for i in range(len(dungeons)):
        req, con = dungeons[i]
        if not visited[i] and k >= req: # 다음 뎊스로 들어갈 수 있는 조건
            visited[i] = True
            new_count = dfs_dungeons(k-con, dungeons, visited, cnt+1)
            max_count = max(max_count, new_count) # 같은 레벨의 다른 결과들과 최대값 비교
            visited[i] = False # 백트래킹을 위해 방문 철회

    return max_count
    
def solution(k, dungeons):
    answer = -1
    
    visited = [False]*len(dungeons) # 방문여부를 저장하기
    answer = dfs_dungeons(k, dungeons, visited, 0)
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3
"""dfs; 15분까지 읽어보기
- 입력:
  - numbers: [리스트] 숫자
  - target: 만들어야하는 숫자
- 출력: 숫자를 만들 수 있는 가짓수

- 아이디어 각 노드가 + / -의 엣지를 갖는 트리라고 생각할 수 있지 않을까?
0: [0] -> 2
4: [0+4]               [0-4]
1: [0+4+1] [0+4-1]     [0-4+1] [0-4-1]
2: [0+4+1+2] [0+4+1-2]
1: [0+4+1+2+1]
r(4):  0 0  0 1 0 1 0 0 0 0 0 0 0 0 
"""

def dfs_number(numbers, index, target, cur_sum):
    if index == len(numbers):
        if cur_sum == target:
            return 1
        else:
            return 0
    
    add_sum = cur_sum + numbers[index]
    add_case = dfs_number(numbers, index+1, target, add_sum)
    
    sub_sum = cur_sum - numbers[index]
    sub_case = dfs_number(numbers, index+1, target, sub_sum)
    
    return add_case + sub_case
    
def solution(numbers, target):
    answer = dfs_number(numbers, 0, target, 0)
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/159993?language=python3
""" 40분까지 문제 읽어보기
시작 지점 -> 레버 -> 문을 열어라
- 벽은 통과 못함
- 최단 시간 찾기

시작: S
레버: L
종료: E
벽: X

bfs x 2
bfs(S -> L) 최단 경로
bfs(L -> E) 최단 경로

valid
- 미로 밖을 벗어났을 때
- 통료일 때
"""
from collections import deque

def bfs_maze(maps, start, goal):
    # visited, level을 저장할 구조 만들기
    # visited: 방문하지 않은 노드에는 -1을 저장하고
    # level: 방문한 노드에는 해당 노드에 도달하기 위한 level을 저장
    distance = []
    for m in maps:
        distance.append([-1]*len(maps[0]))
    distance[start[0]][start[1]] = 0
        
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    
    queue = deque([])
    queue.append(start) # 시작 노드 넣어주기
    
    # BFS 시작
    while queue:
        x, y = queue.popleft()
        if (x, y) == goal:
            return distance[x][y]
        
        for dx, dy in directions:
            # 미로 밖으로 벗어나면 탐색하지 않음
            if not(0 <= x+dx < len(maps)) or not(0 <= y+dy < len(maps[0])):
                continue
            
            # 벽인 경우 탐색하지 않음
            if maps[x+dx][y+dy] == "X":
                continue
            
            # 아직 방문하지 않은 노드라면 탐색을 진행
            if distance[x+dx][y+dy] == -1:
                distance[x+dx][y+dy] = distance[x][y] + 1 # level 추가하기
                queue.append((x+dx, y+dy))
    
    return -1

def solution(maps):
    # start, lever, exit 좌표를 찾아주기
    start = (0, 0)
    lever = (0, 0)
    exit = (0, 0)
    
    
    for i, row in enumerate(maps):
        for j, m in enumerate(row):
            if m == "S":
                start = (i, j)
            if m == "L":
                lever = (i, j)
            if m == "E":
                exit = (i, j)
    
    to_lever = bfs_maze(maps, start, lever)
    to_exit = bfs_maze(maps, lever, exit)
    
    if to_lever == -1 or to_exit == -1:
        return -1
    
    return to_lever + to_exit



# https://school.programmers.co.kr/learn/courses/30/lessons/1844?language=python3
# visited로 해결한 경우
# queue에서 level 정보를 함께 관리
"""
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
- 상대 진영에 갈 수 있는 최소 거리 구하기
- 상대 진영에 갈 수 없다면 -1 출력

- 벽: 0 / 통로: 1

- start: (1, 1) -> (0, 0)
- goal: (n, m) -> (n-1, m-1)

level을 같이 관리하면서 최단 거리(level)을 추적
- distance -> visited
- queue -> level

"""

from collections import deque

def solution(maps):
    answer = 0
    
    # 맵의 크기 저장하기
    n = len(maps)
    m = len(maps[0])
    
    # 시작점, 도착점 저장하기
    start = (0, 0)
    goal = (n-1, m-1)
    
    # visited: True, False
    visited = []
    for _ in range(n):
        visited.append([False]*m)
    
    # directions
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # 초기화
    visited[0][0] = True
    queue = deque([]) # 
    queue.append(((start), 1)) # ((x, y), level)
    
    flag = False
    
    # BFS
    while queue:
        pos, level = queue.popleft()
        x, y = pos
        
        if pos == goal:
            answer = level
            flag = True
            break
        
        
        for dx, dy in directions:
            if not(0 <= x+dx < n) or not(0 <= y+dy < m): # 미로 밖으로 나가는 경우
                continue
            
            if maps[x+dx][y+dy] == 0:
                continue
            
            if not visited[x+dx][y+dy]:
                visited[x+dx][y+dy] = True
                queue.append(((x+dx, y+dy), level+1))
    
    if not flag:
        return -1
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=python3
from collections import deque

def solution(n, computers):
    # computers # 이미 그래프: 인접 행렬
    visited = [False]*n # 방문리스트
    
    answer = 0
    
    for idx, v in enumerate(visited):
        if not v:
            answer += 1
            
            queue = deque([])
            queue.append(idx)

            # BFS 표준 코드
            while queue:
                node = queue.popleft()
                visited[node] = True

                for i in range(len(computers)): # 모든 노드를 순회
                    if not visited[i] and computers[node][i] == 1: # 연결된 노드인지, 미방문 노드인지 확인
                        queue.append(i)
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/49189?language=python3
""" 15분까지 문제 읽어보기
- 노드 번호가 1번부터 있으면, 0번 인덱스 버리고 데이터 구성하기
"""

from collections import deque

def solution(n, edge):
    
    # 주어진 입력을 graph로 만들기: 인접 리스트
    graph = []
    for _ in range(n+1):
        graph.append([])
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    # 방문리스트를 만들어준다. : DFS와 동일
    level = [-1]*(n+1) # [-1, -1, ..] # visited의 역할
    level[1] = 0
    
    # 그래프를 탐색할 queue를 만들어주고
    queue = deque([])
    queue.append(1) # 탐색을 시작할 기준 노드를 저장해준다.
    
    while queue:
        node = queue.popleft() # 노드를 빼주고
        
        for neighbor in graph[node]: # 인접 노드를 순회
            if level[neighbor] == -1: # 아직 방문한 적 없는 노드
                level[neighbor] = level[node] + 1 # 방문 여부를 업데이트
                queue.append(neighbor)
    
    # 최대값의 갯수 찾기
    answer = 0

    max_level = max(level)
    for l in level:
        if l == max_level:
            answer += 1
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/43163?language=python3
"""
보편적인 BFS 알고리즘에서
다음 노드의 탐색 조건을 추가하면 되는 문제
- 다음 노드: 방문하지 않은 모든 words
- 다음 노드의 탐색 조건: 하나의 문자만 바뀌었는지 확인


"""
from collections import deque

def chk_transform(word, target):
    cnt = 0
    for a, b in zip(word, target):
        if a != b:
            cnt += 1 
    
    if cnt == 1:
        return True
    
    return False

def solution(begin, target, words):
    answer = 0
    
    # 방문리스트 초기화
    visited = [False]*len(words)
    
    # queue 초기화
    queue = deque([])
    queue.append((begin, 0)) # word, level
    
    # bfs
    while queue:
        word, level = queue.popleft()
        if word == target:
            answer = level
            break
        
        for idx, trans in enumerate(words):
            # 방문하지 않았거나 변환 가능한 경우 탐색
            if not visited[idx] and chk_transform(word, trans):
                visited[idx] = True
                queue.append((trans, level + 1))
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/86053?language=python3
"""23분까지 읽어보기 & Binary Search로 접근해보기
필요한 자원: a, b
도시별 자원: g, s
트럭 1대: t, w

"주어진 시간 동안 최대한 옮길 수 있는 자원의 수를 찾는 문제"
- 주어진 시간 동안 옮길 수 있는 자원의 수
  - 주어진 시간 동안 트럭은 몇번 왔다갔다 할 수 있냐 -> 횟수 * w
  - move = total time // 2*t but 남은 시간이 t이상이면 한 번 더 움직일 수 있음
  - move * g
  - move * s
  - move * (g+s)

- 주어진 시간 동안 a, b에 해당하는 자원을 옮길 수 있는 최소 시간을 구하면 됨!
  - 더 많은 자원을 옮김 -> right = mid - 1
  - 더 적은 자원을 옮김 -> left = mid + 1
"""
def solution(a, b, g, s, w, t):
    left, right = 0, 4*10**15 # 4*10^15 # 충분히 큰 어떤 값
    answer = right # 최악의 경우로 초기화
    
    
    while left <= right:
        mid = (left + right) // 2
        
        total_gold = 0
        total_silver = 0
        total_res = 0
        
        # mid라는 시간 동안 옮길 수 있는 자원의 양
        for i in range(len(g)):
            move = mid // (2*t[i]) # 주어진 시간 동안 트럭이 왕복할 수 있는 수
            if mid % (2*t[i]) >= t[i]: # 한 번 더 움직일 수 있는 시간이 남았으면
                move += 1
                
            max_gold = min(g[i], move * w[i]) # 금만 옮겼을 때
            max_silver = min(s[i], move * w[i]) # 은만 옮겼을 때
            max_res = min(g[i] + s[i], move * w[i]) # 함께 옮겼을 때
        
            total_gold += max_gold
            total_silver += max_silver
            total_res += max_res
        
        # 옮긴 자원이 필요한 자원보다 많은 경우
        if total_gold >= a and total_silver >= b and total_res >= a + b:
            answer = mid # 최소값을 찾는 경우이므로 가능한 왼쪽 범위
            right = mid - 1
        # 옮긴 자원이 필요한 자원보다 적은 경우
        else:
            left = mid + 1
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/43238?language=python3
""" 53분까지 읽어보기
Binary Search로 어떻게 접근할까!!!
- 입국심사 해야하는 사람: n
- 심사원과 심사 기간: times
- result: n명이 심사를 완료하는데 걸리는 최소시간!

아이디어
- 심사하는데 걸리는 시간을 배열의 인덱스라고 생각하기
- 해당 시간 동안 최대한 심사 가능한 사람의 수 배열의 값이라고 생각하기

- mid에 해당하는 심사수가 n보다 크면 -> 시간을 줄이기
- mid에 해당하는 심사수가 n보다 작으면 -> 시간을 늘리기

"""
def solution(n, times):
    left, right = 1, max(times)*n
    answer = right # 최악의 케이스로 초기화
    
    while left <= right:
        mid = (left + right) //2
        
        # 심사 가능한 최대 인원
        total = 0
        for t in times:
            total += mid // t
        
        if total >= n:
            answer = mid
            right = mid - 1
        elif total < n:
            left = mid + 1
    

    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/86491?language=python3
"""
1. 가로형 명함과 세로형 명함의 타입을 통일 시킨다.
가로형 명함: w > h
세로형 명함: h < w

2. 전체 명함의 최대 가로 * 최대 세로 -> 지갑의 크기를 계산한다.
"""

def solution(sizes):
    answer = 0
    
    max_width = -1
    max_height = -1
    
    for s in sizes:
        s.sort() # 작은게 앞에, 큰게 뒤에 -> 세로형 명함
        
        max_width = max(max_width, s[1])
        max_height = max(max_height, s[0])
        
    answer = max_width*max_height
        
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/17686?language=python3
"""
img1.png
img10.png
img2.png

파일 이름을 3파트로 나누기
- head: 숫자가 나오기 전까지 텍스트
- number: 숫자파트
- tail: 숫자가 나온 이후의 모든 파트

정렬 기준
- 1. head # 대소문자 구분 안함
- 2. number
- tail: 무시
"""

# img12.png
def sort_key(filename):
    head = ''
    number = ''
    
    is_number = False # 숫자 등장 여부
    for i, f in enumerate(filename):
        if f.isdigit():
            is_number = True
            number += f
        else:
            # 숫자가 등장한 경우(Tail 영역인 경우)
            if is_number:
                break
            head += f
    
    head = head.lower()
    number = int(number)
    
    return head, number

def solution(files):
    answer = sorted(files, key=sort_key)

    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/42746?language=python3
""" 문제 읽어보기 & 전략 생각하기
- 10으로 나눈 몫으로 역정렬
[6, 10, 2]
[0, 1, 0]
[6, 2, 10]

[3, 30, 34, 5, 9]
[0, 3, 3, 0, 0]
[3, 5, 9, 30, 40]

- 
"""

def solution(numbers):
    numbers = list(map(str, numbers)) # 리스트 요소의 타입을 한 번에 변경하기
    
    numbers.sort(key=lambda x: x*4, reverse=True)
    # [3, 30, 34, 5, 9]
    # [9, 5, 3, 30, 34]
    # [9, 5, 3, 34, 30]
    
    # 34 | 3434
    # 3 | 33
    # 30 | 3030
    
    answer = ''.join(numbers) # 리스트를 앞에있는 문자열로 연결(join)하기
    # [0, 0, 0, 0]
    # "0"
    if answer[0] == "0":
        return "0"
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/42747?language=python3
"""
h-index
h번 이상 인용된 논문이 h편 이상이고, 나머지 논문이 h번 이하 인용되었다면 h의 최댓값

발행한 논문을 역으로 정렬
[6, 4, 3, 1, 0]
[1, 2, 3, 4, 5]
- 역으로 정렬한 경우 논문 목록의 (index+1)이 h이상 인용된 논문 수와 같음

"""
def solution(citations):
    answer = 0
    sorted_cit = sorted(citations, reverse=True)
    
    for i in range(len(sorted_cit)):
        if sorted_cit[i] >= i+1:
            answer = i + 1
        else:
            break
    
    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/12913?language=python3
""" 49분까지 문제읽고 점화식 생각하기

memo; 각 칸에서 얻을 수 있는 최대 점수
memo[i][j] = land[i][j] + max(memo[i-1]) except memo[i-1][j]
이전 칸에서 내 위치(열)를 제외한 값 들중에 최대값을 더해주기

"""

def solution(land):
    answer = 0
    
    memo = []
    for i in range(len(land)):
        memo.append([0]*4)
    
    memo[0] = land[0]
    
    for i in range(1, len(land)):
        for j in range(4):
            # cols = [memo[i-1][k] for k in range(4) if k != j]
            cols = []
            for k in range(4):
                if k != j: cols.append(memo[i-1][k])
            
            memo[i][j] = land[i][j] + max(cols)

    answer = max(memo[-1])

    return answer



# https://school.programmers.co.kr/learn/courses/30/lessons/12913?language=python3
"""23분까지 문제읽고 점화식 생각해보기
dp[1] = 1
dp[2] = 2
dp[3] = 3

..

dp[n] = dp[n-1] + dp[n-2]
"""

def solution(n):
    # 공간만들기
    dp = [-1]*n # [ , , , , ]
    # 초기화하기
    dp[0] = 1
    dp[1] = 2
    
    if n <= 2:
        return n
    
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] = dp[i] % 1_000_000_007
        
    return dp[i]