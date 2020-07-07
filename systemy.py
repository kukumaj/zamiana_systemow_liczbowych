system =int(input('podaj system od 2 do 16 '))
liczba = int(input('podaj jaka liczbe zamienic '))
liczbazapas=liczba
lista = []
reszta = 4
while True:
    reszta = liczba % system
    if reszta==15:
        reszta='F'
    if reszta==14:
        reszta='E'
    if reszta==13:
        reszta='D'
    if reszta==12:
        reszta='C'
    if reszta==11:
        reszta='B'
    if reszta==10:
        reszta='A'
    wynik = int(liczba / system)
    liczba = wynik
    lista.append(reszta)
    if (liczba == 0):
        break
odwrocona=list(reversed(lista))
print('')
print(odwrocona)

pom=[]

wow=[]

for i in range(0,len(odwrocona)):

    wow.append(odwrocona[i])
    pom.append(len(odwrocona)-i-1)

    print(str(wow[i])+'*'+str(system)+'^'+str(pom[i]), end=' ')

    if len(odwrocona)-i-1==0:

        break
    else:

        print('+', end='')


