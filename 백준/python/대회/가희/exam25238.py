#가희와 방어율 무시

a, b = map(int, input().split())
print(0 if a - ((a / 100) * b) >= 100 else 1)