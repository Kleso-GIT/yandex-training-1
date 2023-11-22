# https://contest.yandex.ru/contest/27393/problems/C/

def normalizer(number):
    normalized_number = ''.join(char for char in number if char.isdigit())
    if len(normalized_number) == 7:
        normalized_number = "495" + normalized_number
    else:
        normalized_number = normalized_number[1:]
    return normalized_number


number_to_add = normalizer(input())
numbers = [normalizer(input()) for number in range(3)]

for number in numbers:
    if number_to_add == number:
        print("YES")
    else:
        print("NO")

