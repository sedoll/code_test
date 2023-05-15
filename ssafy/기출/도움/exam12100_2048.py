import sys
import time
from copy import deepcopy

input = sys.stdin.readline

n = int(input())
# 초기 맵
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def up(board):
    for j in range(n):
        pointer = 0
        for i in range(1, n):
            if board[i][j]: # 현재 위치의 값이 0이 아닌 경우
                tmp = board[i][j] # 현재 값
                board[i][j] = 0
                # 포인터가 가리키는 수가 0일 때
                if board[pointer][j] == 0:
                    board[pointer][j] = tmp
                
                # 포인터가 가리키는 수와 현재 위치의 수가 같을 때
                elif board[pointer][i] == tmp:
                    board[pointer][i] *= 2
                    pointer += 1 # 포인터 이동
                
                # 포인터의 값과 현재 값이 다른경우
                else:
                    pointer += 1
                    board[pointer][j] = tmp
    return board

def down(board):
    for j in range(n):
        pointer = n-1
        for i in range(n-2, -1, -1):
            if board[i][j]:
                tmp = board[i][j] # 현재 값
                board[i][j] = 0
                
                if board[pointer][j] == 0:
                    board[pointer][j] = tmp
                
                # 포인터가 가리키는 수와 현재 위치의 수가 같을 때
                elif board[pointer][i] == tmp:
                    board[pointer][i] *= 2
                    pointer -= 1 # 포인터 이동
                
                # 포인터의 값과 현재 값이 다른경우
                else:
                    pointer -= 1
                    board[pointer][j] = tmp
    return board

def left(board):
    for i in range(n):
        pointer = 0
        for j in range(1, n):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                
                if board[i][pointer] == 0:
                    board[i][pointer] = tmp
                
                elif board[i][pointer] == tmp:
                    board[i][pointer] *= 2
                    pointer += 1
                
                else:
                    pointer += 1
                    board[i][pointer] = tmp
    return board

def right(board):
    for i in range(n):
        pointer = n-1
        for j in range(n-2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                
                if board[pointer][j] == 0:
                    board[pointer][j] = tmp
                
                elif board[pointer][j] == tmp:
                    board[pointer][j] *= 2
                    pointer -= 1
                
                else:
                    pointer -= 1
                    board[pointer][j] = tmp
    return board

def dfs(board, cnt):
    if cnt == 5:
        # 2차원 배열 요소 중 가장 큰 값 반환
        return max(map(max, board))
    
    return max(dfs(up(deepcopy(board)), cnt + 1), dfs(down(deepcopy(board)), cnt + 1), dfs(left(deepcopy(board)), cnt + 1), dfs(right(deepcopy(board)), cnt + 1))

t = time.time()
print(dfs(board, 0))
t = time.time() - t
print(t) # 걸린 시각