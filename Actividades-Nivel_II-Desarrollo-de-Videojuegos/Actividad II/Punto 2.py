import random

tiradas=int(input("Ingrese la cantidad de veces que va a tirar los dados: "))
resultado=0


while tiradas>0:
    print("Tirando dados...")
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    suma=dado1+dado2
    resultado+=suma
    tiradas-=1

print ("El resultado de las tirada es:", resultado)