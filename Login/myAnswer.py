# 아이디와 패스워드가 담긴 배열 id_pw와
# 회원들의 정보가 담긴 2차원 배열 db가 주어질 때,
# 아이디와 비밀번호가 모두 일치하는 회원정보가 있으면 "login"을 return
# 로그인이 실패했을 때 아이디가 일치하는 회원이 없다면 “fail”를,
# 아이디는 일치하지만 비밀번호가 일치하는 회원이 없다면 “wrong pw”를 return 합니다.


def solution(id_pw, db):
    # id_pw = [id, pw]
    # db = [[id, pw], [id, pw],,,]
    for i in db:
        # i = [id, pw]
        if id_pw[0] == i[0]:
            return "login" if id_pw[1] == i[1] else "wrong pw"

    return "fail"

print(solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))
print(solution(["programmer01", "15789"], [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]))
print(solution(["rabbit04", "98761"], [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]))