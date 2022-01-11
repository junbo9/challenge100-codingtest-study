h,m,s = map(int,input().split())
sec = int(input())

s += sec % 60
sec = sec // 60
if s > 59:
    m += 1
    s -= 60
m += sec % 60
sec = sec // 60
if m > 59:
    h += 1
    m -= 60
h += sec % 24
if h > 23:
    h -= 24
print(h,m,s)
