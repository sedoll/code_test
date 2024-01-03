# 이항 계수 1
from math import factorial as fa

a, b = map(int, input().split())
print(int(fa(a) / (fa(b) * fa(a-b))))


