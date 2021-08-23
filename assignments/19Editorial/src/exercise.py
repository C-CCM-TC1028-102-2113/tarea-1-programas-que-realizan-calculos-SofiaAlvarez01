def main():
    #escribe tu código abajo de esta línea
    import math
    num= int(input("Dame el número de palabras: "))
    if num>=475:
        total=(num/475)*60
        total2=total-(total*.10)
        print("El costo de la publicación:",total2)
    pass


if __name__ == '__main__':
    main()
