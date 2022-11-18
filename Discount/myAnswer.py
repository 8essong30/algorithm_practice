# 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인
# 지불해야 할 금액을 return


def solution(price):
    if price >= 100000 and price < 300000:
        discount = price * 0.05
        sale_price = price - discount
        return int(sale_price)

    elif price >= 300000 and price < 500000:
        discount = price * 0.1
        sale_price = price - discount
        return int(sale_price)

    elif price >= 500000 and price <= 1000000:
        discount = price * 0.2
        sale_price = price - discount
        return int(sale_price)

# 처음에 디스카운트로 안하고 할인되는 가격 자체로 계산할 수 있게끔 설정했는데
# 100%의 정답이 나오지 않아서 혹시나 확실하게 하려고 디스카운트 변수를 설정하고 했는데
# 이게 문제가 아니였다..ㅎ
# 10만원 이하의 값들은 설정을 안해놨어