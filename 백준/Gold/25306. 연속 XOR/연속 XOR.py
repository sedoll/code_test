a, b = map(int, input().split())
def fn(v):
    if v%4==0:
        return v
    elif v%4==1:
        return (v-1)^v
    elif v%4==2:
        return (v-2) ^ (v-1) ^v
    else:
        return 0
print(fn(a-1) ^ fn(b))