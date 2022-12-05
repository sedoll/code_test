#다리놓기

from math import comb as c
import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    print(c(b, a))