# 게임에는 up, down, left, right 방향키
# 각 키를 누르면 위, 아래, 왼쪽, 오른쪽으로 한 칸씩 이동
# [0,0]에서
# , up-> [0, 1]
# , down-> [0, -1]
# , left-> [-1, 0]
# , right-> [1, 0]

def solution(keyinput, board):
    x_boundary = board[0] // 2
    y_boundary = board[1] // 2
    result = [0,0]
    for i in keyinput:
        if i == "left" and result[0]-1 >= -(x_boundary):
            result[0]-=1
        elif i == "right" and result[0]+1 <= (x_boundary):
            result[0] += 1
        elif i == "up" and result[1] +1 <= (y_boundary):
            result[1] += 1
        elif i == "down" and result[1] -1 >= -(y_boundary):
            result[1] -= 1
    return result