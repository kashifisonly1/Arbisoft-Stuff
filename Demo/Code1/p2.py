import sys

fin = open(sys.argv[1])
n = int(fin.readline().strip())
print( "YES" if n%2==0 else "NO" )