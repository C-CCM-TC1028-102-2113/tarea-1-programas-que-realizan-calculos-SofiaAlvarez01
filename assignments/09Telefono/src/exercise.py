def main():
    #escribe tu código abajo de esta línea
    import math
    men=int(input("Dame el número de mensajes:"))
    meg=float(input("Dame el número de megas:"))
    minu=int(input("Dame el número de minutos:"))
    ment=men*.80
    megt=meg*.80
    minut=minu*.80
    total=ment+megt+minut
    print("El costo mensual es:",total)

    #Leer los datos
    pass


if __name__ == '__main__':
    main()
