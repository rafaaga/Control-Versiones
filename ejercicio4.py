producto_uno = input("Ingrese el valor del producto")
contador = 0
bool = True
while bool == True:
    resp = input("¿Va a facturar otro producto?  Sí = 1  No = 0")
    if(resp == '1'):
        bool = True
    elif(resp == '0'):
        bool = False
        break
    else:
        bool = False
        break
    precio_dos = input("Ingrese precio del producto")
    contador = (contador+int(precio_dos))
subtotal = (contador+int(producto_uno))
Iva = int(subtotal) * (8/100)
Total = float(subtotal+ Iva)
print ("El total de su compra es de $", Total)
print ("Subtotal = $", subtotal)
print ("IVA = $", Iva )


