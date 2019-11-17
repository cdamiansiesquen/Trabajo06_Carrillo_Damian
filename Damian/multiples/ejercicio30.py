import os
nombre, frappuccino, cupcakes, galletas = ",", 0, 0 ,0

#imput
nombre = os.sys.argv[1]
frappucicino = int(os.sys.argv[2])
cupcakes = int(os.sys.argv[3])
galletas = int(os.sys.argv[4])

#procesing
total = ( frappuccino + cupcakes + galletas )

#verificador
comprador_compulsivo = ( total >= 25 )

#output
print( "##############################")
print( "#DSCOFFEE")
print( "#variables:    cantidad:")
print( "nombre:",       nombre)
print( "#frappuccino:",     frappuccino)
print( "#cupcakes:",  cupcakes)
print( "#galletas:",     galletas)
print( "total:",        total)
print( "##############################")

#condicion simple
#si comprador compulsivo mostrar tarjeta visa
if ( comprador_compulsivo == True ):
    print("se gano un vale de descuento para un cappuccino de moca")
if ( 18 < comprador_compulsivo < 25 ):
    print("descuento de 10% en la promocion ")
if ( comprador_compulsivo <17 ):
    print("Gracias por su compra")
#fin_if
