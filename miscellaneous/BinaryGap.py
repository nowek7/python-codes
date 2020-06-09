def solution(number):
    maxGaps = 0
    gaps = -1
    while number != 0:
        number, res = divmod(number, 2)

        if res == 1:
            if gaps > maxGaps:
                maxGaps = gaps

            gaps = 0

        elif gaps > -1:
            gaps += 1

    return maxGaps


print(solution(1041))
print(solution(1))
print(solution(15))
print(solution(32))
print(solution(20))
print(solution(32))
print(solution(1376796946))
print(solution(2147483640))

print(format(2147483640, 'b'))
