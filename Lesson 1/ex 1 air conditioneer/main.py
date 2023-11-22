# https://contest.yandex.ru/contest/27393/problems/A/
def solution(troom, tcond, cond_mode):
    if cond_mode == "fan":
        return troom
    elif cond_mode == "auto":
        return tcond
    elif cond_mode == "heat":
        if troom < tcond:
            return tcond
        else:
            return troom
    else:
        if troom > tcond:
            return tcond
        else:
            return troom


troom, tcond = map(int, input().split())
cond_mode = input()
print(solution(troom, tcond, cond_mode))
