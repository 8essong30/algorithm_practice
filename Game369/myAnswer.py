# 3, 6, 9 의 개수만큼 박수
# 쳐야할 박수 횟수 return

def solution(order):
    order = str(order)
    order_list = list(order)
    count = 0
    for num in order_list:
        if num == "3":
            count += 1
        elif num == "6":
            count += 1
        elif num == "9":
            count += 1
    return count


print(solution(3))
print(solution(29423))
