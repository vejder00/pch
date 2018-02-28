 
#Zad 1
#Przez przypadek usunalem

#Zad 2
a = input('Podaj pierwsza liczbe: \n')
b = input('Podaj druga liczbe: \n')
c = input('Poda trzecia liczbe: \n')

lista = [a,b,c]

d=a

for i in range (len(lista)):
    if(int(lista[i]) > int(d)):
        d=int(lista[i])

print('Najwieksza liczba to:',d)


#Zad 3


i = 65

while(i<=90):
    print(chr(i+32))
    print(chr(i))
    i+=1
    
#Zad 4

n = input('Podaj co ktora litere alfabetu pokazac: \n')

i = 65

while(i<=90):
    if(int(n)>1):
        print(chr(i+32))
        print(chr(i))
        i+=int(n)
    elif(int(n)==0):
        print('Podales n = 0 wiec nie ma zadnego alfabetu')
        break
    else:
        print(chr(i+32))
        print(chr(i))
        i+=1
        
#Zad 5
# TEN Nie dziala (RESZTA ZADAN DZIALA)

N = input('Podaj N liczb do posortowania')

lista1 = [N]

i=0

while(i<int(N)):
    lista1[i] = input('Podaj liczbe')
    i+=1
    
print('Jesli chcesz posortowac rosnaco wybierz :1 \n')
print('Jesli malejaco wybierz : 0 \n')

liczba = input('Podaj liczbe')

a = input('Podaj dolny zakres: \n')
b = input('Podaj gorny zakres: \n')

if(liczba==1):
    lista1.sort()
elif(liczba==0):
    lista1.sort()
    lista1.reverse()
    c=a
    a=b
    b=c

    


i=0
while(i<N):
    if(lista1[i] >= int(a)):
        if(lista1[i]<= int(b)):
            print(lista1[i])

#Zad 6 

def fib(a):
    if(a==0):
        return 0
    elif(a==1):
        return 1
    elif(int(a)>1):
        return fib(int(a)-1)+fib(int(a)-2)
        
z = input('Podaj do ktorej liczby  ciagu fibonacciego wypisac: \n')



i = 0
while(int(i) <= int(z)):
    print(fib(i))
    i+=1


