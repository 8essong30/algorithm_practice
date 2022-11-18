# 범위 설정할 때는 숫자가 큰 순대로 설정하는게 좋음
# 범위가 큰거부터 설정을 해서 elif 대신 if만 사용해도 가능.
# 코드가 더 깔끔해 보임

def solution(angle):
    if angle >= 180:
        return 4

    if angle > 90:
        return 3

    if angle == 90:
        return 2

    if angle < 90:
        return 1