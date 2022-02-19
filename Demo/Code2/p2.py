import sys

fin = open(sys.argv[1])

n = int(fin.readline())
mat = [ fin.readline().strip().split() for i in range(n) ]
sum_main = 0
sum_secondary = 0
for i in range(n):
    sum_main += int(mat[i][i])
    sum_secondary += int(mat[i][n-i-1])

print(abs(sum_main-sum_secondary))