b = input()
a = input()
n = len(a)+1
m = len(b)+1
opt = [[0 for i in range(m)] for j in range(n)]
for i in range(1,n):
    for j in range(1,m):
        if a[i-1] == b[j-1]:
            opt[i][j] = 1 + opt[i - 1][j - 1]
        else:
            opt[i][j] = max(opt[i - 1][j], opt[i][j - 1])

i = n-1
j = m-1
lcs_length = opt[i][j]
lcs_value = ""
while opt[i][j] != 0:
    if opt[i - 1][j] < opt[i][j] and opt[i][j - 1] < opt[i][j]:
        lcs_value = a[i-1] + lcs_value
        i = i - 1
        j = j - 1
    elif opt[i - 1][j] == opt[i][j]:
        i = i - 1
    else:
        j = j - 1
print(opt[n - 1][m - 1])
print(lcs_value)
