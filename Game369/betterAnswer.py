# 연희튜터님
# 오더리스트로 만든 리스트 자체에 3, 6, 9를 넣어버리네..와우
# 그리고 for문에 오더를 문자로 바꾼 상태로 넣는 방법이..

def solution(order) :
    match = ["3", "6", "9"]
    count = 0
    for o in str(order):
        if o in match:
            count += 1
    return count

print(solution(3))
print(solution(29423))
print(solution(369369))
