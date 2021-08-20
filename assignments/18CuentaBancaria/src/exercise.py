def main():
    #escribe tu código abajo de esta línea
    import math
    sal= float(input("Dame el saldo del mes anterior: "))
    ing= float(input("Dame los ingresos: "))
    egr= float(input("Dame los egresos: "))
    num= int(input("Dame el número de cheques: "))
    saldo= (sal+ing)-(num*13)-(egr)
    saldofinal= saldo-(saldo*.075)
    saldofinal2= round(saldofinal,5)
    print("El saldo final de la cuenta es:",saldofinal2)
    pass

if __name__ == '__main__':
    main()
