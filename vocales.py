import sys

infile = open ('Sain.txt','r')

i=0
data=[]
n=sys.argv[1]

while (i<n):
    data.append(infile.readline())

c=0

for i in range (len(data))
    s= data[i]
    for j in range (len(s)):
        if (s[j]=="a" or s[j]=="e" or s[j]=="i" or s[j]=="o" or s[j]=="u"):
            c=c+1
     return c




