# 숫자가 큰 순서대로 범위 설정하는게 좋다.
# 순서를 바꾸고 else값을 설정했다.
# 훨씬 깔끔..

def solution(price):
    if price >= 500000:
        return int(price * 0.8)

    elif price >= 300000:
        return int(price * 0.)

    elif price >= 100000:
        return int(price * 0.95)
    else:
        return price