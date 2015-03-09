#lista con sucesion de los numero de fibonacci

a=1
b=1
lista=[]
lista.append(a)
lista.append(b)
n=1
while(n<30):
    c=a+b
    lista.append(c)
    a=b
    b=c
    n=n+1

for i in range (len(lista)):
    print lista[i]

print "Las maneras distintas para subir una escalera de 13 escalones son: " + str(lista[13])
print "Las maneras distintas para subir una escalera de 15 escalones son: " + str(lista[15]) 
print "Las maneras distintas para subir una escalera de 5 escalones son: " + str(lista[5])   

A=[4,4,5,5,1]
B=[3,2,4,3,1]

def escaleras(A,B):
    listan=[]
    for i in range(len(A)):
        c = A[i]% B[i]
        listan.append(lista[c])
    return listan


print escaleras(A,B)


