n = int(input())
a = [int(input()) for _ in range(n)]
opt = [1 for _ in range(n)]
p = [0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            if 1 + opt[j] > opt[i]:
                p[i] = j
            opt[i] = max(opt[i], 1 + opt[j])
print(f"a = {a}")
# print(f"opt = {opt}")
print(f"length of lis = {max(opt)}")
# print(f"p = {p}")

g = opt.index(max(opt))
lis = [g]
while p[g] != g:
    g = p[g]
    lis.insert(0,g)

lis = [a[i] for i in lis]
print(f"lis = {lis}")
