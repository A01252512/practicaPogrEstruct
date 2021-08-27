def calculaCostoTotal(ts, cs):
    if ts == 'B':
        return cs*700
    elif ts == 'E':
        return cs*900
    elif ts == 'D':
        return cs*1500
    else:
        return 0

def calculaDescuento(total, tc):
    if tc == 'F':
        return total*0.20
    elif tc == 'N':
        if total >= 20000:
            return total * 0.15
        elif total >= 10000:
            return total*0.1
        else:
            return 0
    return 0

def pagoNeto(total, descuento):
    return total-descuento

def main():
    #escribe tu código abajo de esta línea
    cantidadSillas = int(input("¿Cuántas sillas? "))
    tipoSilla = input("Tipo de silla: (B)ásica, (E)stándar o (D)e lujo.\n")
    tipoCliente = input("Tipo de cliente: (N)ormal, (F)recuente\n")
    costoTotal = calculaCostoTotal(tipoSilla, cantidadSillas)
    descuento = calculaDescuento(costoTotal, tipoCliente)
    montoFinal = pagoNeto(costoTotal, descuento)
    #El precio antes de descuento
    #El descuento
    #El total a pagar por el cliente
    print(costoTotal)
    print(descuento)
    print(montoFinal)

if __name__=='__main__':
    main()
