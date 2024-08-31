# https://school.programmers.co.kr/learn/courses/30/lessons/181839
def solution(a, b):
    if a % 2 != 0 and b % 2 != 0:
        answer = a**2 + b**2
    elif a % 2 != 0 or b % 2 != 0:
        answer = 2 * (a + b)
    else:
        answer = abs(a - b)
    return answer


# https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3
def solution(nums):
    max_types = len(set(nums))
    max_selectable = len(nums) // 2
    
    answer = min(max_types, max_selectable)
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/81301?language=python3
def solution(s):
    num_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    
    for word, num in num_dict.items():
        s = s.replace(word, num)
    
    return int(s)


# https://school.programmers.co.kr/learn/courses/30/lessons/12931?language=python3
def solution(n):
    answer = sum(int(digit) for digit in str(n))
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/120817?language=python3
def solution(numbers):
    return sum(numbers) / len(numbers)

# https://school.programmers.co.kr/learn/courses/30/lessons/12928?language=python3
def solution(n):
    if n == 0:
        return 0
    return sum(i for i in range(1, n + 1) if n % i == 0)
