# 연희튜터님 풀이!!

def solution(id_pw, db) :
    for id, password in db:
        # 구조분해 할당
        if id == id_pw[0]:
            if password == id_pw[1]:
                return "login"
            return "wrong pw"
        return "fail"
