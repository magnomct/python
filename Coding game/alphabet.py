import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

alphabet = '''a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'''.split(",")
string = ""
for x in range(n):
    string += alphabet[n-1]
print(string.upper())
