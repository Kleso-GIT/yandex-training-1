# https://contest.yandex.ru/contest/27393/problems/D/

def solution(a, b, c):
    if c < 0:
        return "NO SOLUTION"
    elif a == 0 and b != c ** 2:
        return "NO SOLUTION"
    elif a == 0 and b == c ** 2:
        return "MANY SOLUTIONS"
    else:
        if (c ** 2 - b) % a == 0:
            return (c ** 2 - b) // a
        else:
            return "NO SOLUTION"


a = int(input())
b = int(input())
c = int(input())
print(solution(a, b, c))

