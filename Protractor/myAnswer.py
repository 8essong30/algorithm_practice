# 0도 초과 90도 미만은 예각,
# 90도는 직각,
# 90도 초과 180도 미만은 둔각
# 180도는 평각

# 각 angle이 매개변수로 주어질 때 예각일 때 1,
# 직각일 때 2,
# 둔각일 때 3,
# 평각일 때 4를 return


def solution(angle):
    if 0 < angle and angle < 90:
        return(1)
    elif angle == 90:
        return(2)
    elif angle > 90 and angle < 180:
        return(3)
    elif angle == 180:
        return(4)


print(solution(70))
print(solution(91))
print(solution(180))
