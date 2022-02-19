import sys

fin = open(sys.argv[1])

s = fin.readline().strip()
n = len(s)
i = 0
while i<int(n/2) and ( s[i]==s[n-i-1] or (ord(s[i]) ^ ord(s[n-1-i]))==32):
    i+=1
print( "TRUE" if ( s[i]==s[n-i-1] or (ord(s[i]) ^ ord(s[n-1-i]))==32) else "FALSE" )