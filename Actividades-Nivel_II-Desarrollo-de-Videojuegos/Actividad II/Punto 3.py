for i in range (0,5):
    vida=int(input("Ingrese la cantidad de vidas que quiere tener (1-5): "))
    if vida >= 5:
        print ("Tu dificultad de juego será: fácil")
    elif vida == 3 or vida == 4:
        print ("Tu dificultad de juego será: media")
    elif vida < 3 and vida >= 1:
        print ("Tu dificultad de juego será: difícil")
    elif vida < 1:
        print ("Error, ingrese un número válido")