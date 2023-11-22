# https://contest.yandex.ru/contest/27393/problems/B/

def solution(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return "YES"
    else:
        return "NO"


a = int(input())
b = int(input())
c = int(input())

print(solution(a, b, c))

